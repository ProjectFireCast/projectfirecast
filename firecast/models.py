from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.db.models import CharField, Model
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your models here.
from users.models import CustomUser


class Podcast(models.Model):
    author = models.CharField(max_length=100)
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, max_length=500)
    slug = AutoSlugField(populate_from='title')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.png', blank=True)
    audio = models.FileField(upload_to='audio/', validators=[FileExtensionValidator(allowed_extensions=['wav', 'mp3', 'ogg'])])

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:400] + '...'



