from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()  # Use TinyMCE for content
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_add_post", "Can add post"),
        ]

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
   

    def __str__(self):
        return self.user.username