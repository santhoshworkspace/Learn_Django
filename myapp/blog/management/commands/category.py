from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand
from django.db import connection 


class Command(BaseCommand):
    help = "Category"

    def handle(self, *args, **options):
        #POST.objects.all().delete()
        #cursor = connection.cursor()
       # cursor.execute("ALTER TABLE blog_post AUTO_INCREMENT = 1")

        category = ['sport','gym','news','market']

        for t in category:
            Category.objects.create(name=t)

        self.stdout.write(self.style.SUCCESS("completed"))
