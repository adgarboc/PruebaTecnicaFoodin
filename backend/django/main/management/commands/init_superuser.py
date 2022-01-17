from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates an super user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--username', help="Superuser's username")
        parser.add_argument('--email', help="Superuser's email")
        parser.add_argument('--password', help="Superuser's password")

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))
            return
        if User.objects.filter(username=options['username']).exists():
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))
            return
        User.objects.create_superuser(
            username=options['username'],
            email=options['email'],
            password=options['password']
        )
        self.stdout.write(self.style.SUCCESS("Superuser created"))
