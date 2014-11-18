from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
import markdown2

register = Library()


@register.filter(is_safe=True)
@stringfilter
def markdown(value):
    return mark_safe(markdown2.markdown(force_unicode(value),
                                        use_file_vars=True,
                                        extras={'code-friendly': True}))
