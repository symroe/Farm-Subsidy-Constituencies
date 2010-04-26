from django.template import Library, Node
import urlparse
import urllib
register = Library()

@register.inclusion_tag('sort_link.html', takes_context=True)
def sort_link(context, link_name="", k=None, v=None):
    qs = context['request'].GET.copy()

    active = False
    if qs.get(k) == v:
        active=True

    if k:
        qs[k] = v
    
    # Normally, we don't want to keep the page element of the string
    if 'page' in qs:
        del qs['page']

    qs = "?%s" % urllib.urlencode(qs)

    return {
        'link_name' : link_name,
        'active' : active,
        'qs' : qs,
    }