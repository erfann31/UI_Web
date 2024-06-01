from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a default superuser'

    def handle(self, *args, **kwargs):
        username = 'admin'
        password = 'admin123'
        email = 'admin@example.com'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Successfully created default superuser'))
        else:
            self.stdout.write(self.style.WARNING('Default superuser already exists'))
