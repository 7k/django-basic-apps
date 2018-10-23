from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.template import TemplateSyntaxError
from django.template.loader import render_to_string
from django.utils.encoding import smart_text
from django.utils.safestring import mark_safe


def inlines(value, return_list=False):
    """ Return ``value`` with all <inline/> tags rendered. """
    try:
        from BeautifulSoup import BeautifulStoneSoup as bs1
        BS = bs1
    except ImportError:
        try:
            from beautifulsoup import BeautifulStoneSoup as bs2
            BS = bs2
        except ImportError:
            try:
                from bs4 import BeautifulSoup as bs4
                BS = bs4
            except ImportError:
                return ''

    content = BS(value, "html.parser")
    inline_list = []

    if return_list:
        for inline in content.findAll('inline'):
            rendered_inline = render_inline(inline)
            inline_list.append(rendered_inline['context'])
        return inline_list
    else:
        for inline in content.findAll('inline'):
            rendered_inline = render_inline(inline)
            if rendered_inline:
                string = BS(
                    render_to_string(
                        rendered_inline['template'],
                        rendered_inline['context']),
                    "html.parser")
                inline.replaceWith(string)
            else:
                inline.replaceWith('')
        return mark_safe(str(content))


def render_inline(inline):
    """
    Replace inline markup with template markup that matches the
    appropriate app and model.

    """

    # Look for inline type, 'app.model'
    try:
        app_label, model_name = inline['type'].split('.')
    except:
        if settings.DEBUG:
            raise TemplateSyntaxError(
                "Couldn't find the attribute 'type' in the <inline> tag.")
        else:
            return ''

    # Look for content type
    try:
        content_type = ContentType.objects.get(
            app_label=app_label, model=model_name)
        model = content_type.model_class()
    except ContentType.DoesNotExist:
        if settings.DEBUG:
            raise TemplateSyntaxError("Inline ContentType not found.")
        else:
            return ''

    # Check for an inline class attribute
    try:
        inline_class = smart_text(' '.join(inline['class']))
    except:
        inline_class = ''

    try:
        count = int(inline['count'])
        try:
            qs_name = inline['queryset']
            obj_list = model.objects.__getattribute__(qs_name)()
        except (KeyError, AttributeError):
            # Use the default queryset
            obj_list = model.objects.all()
        try:
            order_by = inline['sort']
            obj_list = obj_list.order_by(order_by)
        except KeyError:
            # 'sort' is optional
            pass
        try:
            filtering = inline['filter']
            filters = filtering.split(',')
            query_dict = {}
            for f in filters:
                pair = f.split(':')
                if not len(pair) == 2:
                    continue
                key = pair[0]
                if pair[1].lower() == "true":
                    value = True
                elif pair[1].lower() == "false":
                    value = False
                else:
                    value = pair[1]
                query_dict[key] = value
            obj_list = obj_list.filter(**query_dict)
        except KeyError:
            # 'filter' is optional
            pass
        except:
            if settings.DEBUG:
                raise ValueError('Invalid query string: %s' % filtering)
            else:
                return ''
        context = {'object_list': obj_list[:count], 'class': inline_class}
    except ValueError as e:
        if settings.DEBUG:
            raise ValueError(
                "The <inline> `count` and/or `sort` attributes "
                "are missing or invalid: %s" % e)
        else:
            return ''
    except KeyError:
        try:
            id_list = [int(i) for i in inline['ids'].split(',')]
            obj_list = model.objects.in_bulk(id_list)
            obj_list = list(obj_list[int(i)] for i in id_list)
            context = {'object_list': obj_list, 'class': inline_class}
        except ValueError:
            if settings.DEBUG:
                raise ValueError(
                    "The <inline> ids attribute is missing or invalid.")
            else:
                return ''
        except KeyError:
            try:
                obj = model.objects.get(pk=inline['id'])
                context = {
                    'content_type': "%s.%s" % (app_label, model_name),
                    'object': obj,
                    'class': inline_class,
                    'settings': settings
                }
            except model.DoesNotExist:
                if settings.DEBUG:
                    raise model.DoesNotExist(
                        "%s with pk of '%s' does not exist" % (
                            model_name, inline['id']))
                else:
                    return ''
            except:
                if settings.DEBUG:
                    raise TemplateSyntaxError(
                        "The <inline> id attribute is missing or invalid.")
                else:
                    return ''
    template = [
        "inlines/%s_%s.html" % (app_label, model_name), "inlines/default.html"]
    rendered_inline = {
        'template': template,
        'context': context
    }
    return rendered_inline
