from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField(primary_key=True,default=0)
    bio=models.TextField(blank=True,default='')
    profileimg=models.ImageField(upload_to='profile_images',default='def_pimg.png')
    location=models.CharField(max_length=100,blank=True,default='')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images')
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)
    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Followers(models.Model):
    follower=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    def __str__(self):
        return f"{self.follower} -> {self.user} ({self.status})"
