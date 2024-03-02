from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default profile.jpg',upload_to='media')
    location=models.CharField(max_length=100,null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='profile_model'
        verbose_name_plural='profile'
    def __str__(self):
        return self.user.username
