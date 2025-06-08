from typing import Any
from blog.models import POST
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help = "Command"

    def handle(self, *args, **options):
        title=["1 tittle","2 tittle"]
        content=["1 content","2 content"]
        for tittle , content in zip(title,content):
         POST.objects.create(title=title,content=content)
        self.stdout.write(self.style.SUCCESS("completed"))
