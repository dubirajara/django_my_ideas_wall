#!/usr/bin/env python

"""
Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
SECRET_KEY={}
DEBUG=True
ALLOWED_HOSTS=*

#EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
#EMAIL_HOST=localhost
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
#EMAIL_PORT=25
#EMAIL_USE_TLS=False

# SENDGRID SETTINGS
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.com
SENDGRID_API_KEY=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=587
EMAIL_USE_TLS=True


# DJANGO SOCIAL-AUTH SETTINGS
SOCIAL_AUTH_FACEBOOK_KEY=
SOCIAL_AUTH_FACEBOOK_SECRET=
SOCIAL_AUTH_TWITTER_KEY=
SOCIAL_AUTH_TWITTER_SECRET=
""".strip().format(get_random_string(50, chars))

# Writing our configuration file to '.env'
with open('myideas/.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
