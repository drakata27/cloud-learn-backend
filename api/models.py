from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.title), filename])

# Create your models here.
class Section(models.Model):
    title = models.TextField(null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)

    def __str__(self):
        return self.title or "Untitled Section"

class Topic(models.Model):
    title = models.TextField(null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
    section = models.ForeignKey(Section, related_name='topics', on_delete=models.CASCADE)

    def __str__(self):
        return self.title or "Untitled Topic"

class Subtopic(models.Model):
    title = models.TextField(null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
    body = models.TextField(null=True, blank=True)
    topic = models.ForeignKey(Topic, related_name='subtopics', on_delete=models.CASCADE)

    def __str__(self):
        return self.title or "Untitled Subtopic"

# Custom User
class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username

# Profile for each user 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    image = models.ImageField(default="default.jpg", upload_to='user_images')
    verified = models.BooleanField(default=False)

    def __str__(self) -> str:
            return self.full_name
    
def create_user_profile(sender, instance, created, **kwargs):
     if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

# def upload_path(instance, filename):
#     return '/'.join(['covers', str(instance.title), filename])