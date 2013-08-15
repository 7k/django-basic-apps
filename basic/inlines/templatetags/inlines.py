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
    """
    return inlines(value)


@register.filter
def extract_inlines(value):
    """ Extract the inlines from ``value``. """
    return inlines(value, True)


@register.assignment_tag
def get_inline_types():
    """
    Gets all inline types.

    Syntax::

        {% get_inline_types as [var_name] %}

    Example usage::

        {% get_inline_types as inline_list %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return InlineTypes(var_name)