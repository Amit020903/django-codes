from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Book
import random

class Command(BaseCommand):
    help = 'Generate fake books for the database'

    def handle(self, *args, **kwargs):
        faker = Faker()

        for _ in range(200):  # Generate 10 fake books
            Book.objects.create(
                title=faker.sentence(nb_words=4),
                author=faker.name(),
                published_date=faker.date()
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 200 fake books!'))
