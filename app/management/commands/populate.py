from django.core.management.base import BaseCommand
from app.models import Language, User, Exchange
from django.utils.timezone import now
import random

class Command(BaseCommand):
    help = "Populate database with test data"

    def handle(self, *args, **kwargs):
        # Kreiranje jezika
        languages = ['English', 'German', 'Spanish', 'French', 'Italian']
        for lang in languages:
            Language.objects.get_or_create(name=lang)

        # Kreiranje korisnika
        for i in range(1, 11):
            User.objects.get_or_create(
                username=f"user{i}",
                email=f"user{i}@example.com"
            )

        # Kreiranje razmjena
        all_languages = list(Language.objects.all())
        all_users = list(User.objects.all())
        for _ in range(20):
            Exchange.objects.get_or_create(
                language=random.choice(all_languages),
                user=random.choice(all_users),
                date=now()
            )

        self.stdout.write(self.style.SUCCESS("Test data created successfully."))
