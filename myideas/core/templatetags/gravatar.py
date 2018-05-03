import hashlib
from urllib.parse import urlencode

from django import template

register = template.Library()


@register.filter
def gravatar(email, size="75"):
    url = "//www.gravatar.com/avatar/" + \
        hashlib.md5(email.encode('utf-8')).hexdigest() + "?"
    url += urlencode({'d': 'retro', 's': str(size)})

    return url
