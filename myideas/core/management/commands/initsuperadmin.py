from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            email = 'admin@mail.com'
            user = 'admin'
            password = 'admin123456'
            admin = User.objects.create_superuser(email=email, username=user, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            print('Admin accounts successfully created.')

        else:
            print('Admin accounts can only be initialized if no Accounts exist')
