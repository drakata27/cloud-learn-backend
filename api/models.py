from django.db import models

def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.title), filename])

# Create your models here.
class Topic(models.Model):
    title = models.TextField(null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path, default='media/covers/default.jpg')