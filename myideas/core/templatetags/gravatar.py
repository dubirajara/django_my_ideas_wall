import hashlib
from urllib.parse import urlencode

from django import template

register = template.Library()


@register.filter
def gravatar(email, size="75"):
    hash_email = hashlib.md5(email.encode('utf-8')).hexdigest()
    url = f'//www.gravatar.com/avatar/{hash_email}?'
    url += urlencode({'d': 'retro', 's': str(size)})

    return url
