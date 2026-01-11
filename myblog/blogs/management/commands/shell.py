from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        raise CommandError('Standard shell is disabled for security reasons. Use "secure_shell" instead.')