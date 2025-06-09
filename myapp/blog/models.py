from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
# Create your models here.
class POST(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return  self.title

