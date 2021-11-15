import datetime

from django.db import models


class Post(models.Model):
    title_text = models.CharField(max_length=120);
    content_text = models.CharField(max_length=1000);
    today_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_text
