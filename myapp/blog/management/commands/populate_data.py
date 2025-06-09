from typing import Any
from blog.models import POST
from django.core.management.base import BaseCommand
from django.db import connection 


class Command(BaseCommand):
    help = "Command"

    def handle(self, *args, **options):
        #POST.objects.all().delete()
        #cursor = connection.cursor()
        #cursor.execute("ALTER TABLE blog_post AUTO_INCREMENT = 1")

        titles = ["1 tittle", "2 tittle","3 tittle"]
        contents = ["1 content", "2 content", "3 content"]

        for t, c in zip(titles, contents):
            POST.objects.create(title=t, content=c)

        self.stdout.write(self.style.SUCCESS("completed"))
