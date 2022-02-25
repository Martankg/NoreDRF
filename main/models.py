from pyexpat import model
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField('Title',max_length=50)
    content = models.TextField('Content')

    creatd_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title