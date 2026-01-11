import getpass
import hashlib
from django.core.management.base import BaseCommand
from django.core.management import call_command
from decouple import config

PASSWORD_HASH_FILE = config('PASSWORD_HASH_FILE')


class Command(BaseCommand):
    help = 'Access the Django shell only after entering a master PIN.'

    def handle(self, *args, **options):
        password = getpass.getpass('Enter Shell Access Password: ')
        input_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if input_hash == PASSWORD_HASH_FILE:
            self.stdout.write(self.style.SUCCESS('Access GRANTED. Launching shell...'))
            call_command('shell')
        else:
            self.stdout.write(self.style.ERROR('Access DENIED. Password is incorrect.'))