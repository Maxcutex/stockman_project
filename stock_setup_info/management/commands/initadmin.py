from django.core.management.base import BaseCommand

from stock_profile_mgt.models import UserProfile


class Command(BaseCommand):

    def handle(self, *args, **options):
        if UserProfile.objects.count() == 0:
            username = "admin"
            email = "admin@stockman.com"
            password = 'admin'
            print('Creating account for %s (%s)' % (username, email))
            admin = UserProfile.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
