import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post',null=True)
    post_title = models.CharField(max_length=120)
    post_image = models.ImageField(upload_to='posts/',blank=False,null=True)
    post_content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        ordering = ['created','-updated']

    def publish(self):
        self.created = timezone.now()
        self.updated = timezone.now()
        self.save()
