import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post',null=True)
    post_title = models.CharField(max_length=120)
    post_image = models.ImageField(upload_to='posts/',blank=False,null=True)
    post_content = models.TextField(null=True)
    today_date = models.DateTimeField(auto_now_add=True, null=True)

    def publish(self):
        self.today_date = timezone.now()
        self.save()
