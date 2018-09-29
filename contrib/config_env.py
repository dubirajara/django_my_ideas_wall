from django.core.management import utils


CONFIG_ENV = f"""
SECRET_KEY={utils.get_random_secret_key()}
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=postgres://postgresuser:postgrespass@db:5432/ideasdb

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

#DJANGO RECAPTCHA
RECAPTCHA_PUBLIC_KEY=
RECAPTCHA_PRIVATE_KEY=
"""

# Writing our configuration file to '.env'
with open('myideas/.env', 'w') as configfile:
    configfile.write(CONFIG_ENV)
    print('Created the .env file successfully.')
