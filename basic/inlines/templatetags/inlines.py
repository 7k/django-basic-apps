from django import template
from django.db import models

from basic.inlines.parser import inlines
from basic.inlines.models import InlineType

register = template.Library()


@register.filter
def render_inlines(value):
    """
    Render inlines in a string by passing them through inline templates.

    Template Syntax::

        {{ object.text|render_inlines }}

    Inline Syntax (singular)::

        <inline type="<app_name>.<model_name>" id="<id>" class="pull-left" />

    Inline Syntax (plural)::

        <inline type="<app_name>.<model_name>" ids="<id>, <id>, <id>" />
        <inline type="<app_name>.<model_name>" count="<count>"
                [sort="<field>" filter="<filter>"] />

    An inline template will be used to render the inline. Templates will be
    locaed in the following maner:

        ``inlines/<app_name>_<model_name>.html``

    The template will be passed the following context:

        ``object``
            An object for the corresponding passed id.

    or

        ``object_list``
            A list of objects for the corresponding ids.

    It would be wise to anticipate both object_list and object unless
    you know for sure one or the other will only be present.

    ``filter`` is a comma separated list of QuerySet-like lookup parameters,
    with colons instead of the equal sign.
    """
    return inlines(value)


@register.filter
def extract_inlines(value):
    """ Extract the inlines from ``value``. """
    return inlines(value, True)


@register.simple_tag
def get_inline_types():
    """
    Gets all inline types.

    Syntax::

        {% get_inline_types as [var_name] %}

    Example usage::

        {% get_inline_types as inline_list %}
    """
    return InlineType.objects.all()


@register.simple_tag(takes_context=True)
def show_object(context, obj, **kwargs):
    """ Render an object or an object list using inline templates. """
    template_context = {}
    template_context.update(context.__dict__)
    if isinstance(obj, models.Model):
        template_context['object'] = obj
        app = obj._meta.app_label
        model = obj._meta.module_name
    elif isinstance(obj, models.query.QuerySet):
        template_context['object_list'] = obj
        app = obj.model._meta.app_label
        model = obj.model._meta.module_name
    elif isinstance(obj, list) and obj:
        template_context['object_list'] = obj
        app = obj[0]._meta.app_label
        model = obj[0]._meta.module_name
    else:
        return ''
    templates = [
        'inlines/%s_%s.html' % (app, model),
        'inlines/default.html'
    ]
    serialized = [('%s-%s' % (k, kwargs[k])) for k in kwargs]
    template_context.update({
        'app_label': app,
        'model': model,
        'cache_key': '_'.join([app, model] + serialized)
    })
    template_context.update(kwargs)
    return template.loader.render_to_string(templates, template_context)
