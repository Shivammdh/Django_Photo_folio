from django.db import models
from tinymce.models import HTMLField

class MyNews(models.Model):
    news_title=models.CharField(max_length=200)
    news_description=HTMLField()

    def __str__(self):
        return self.news_title

