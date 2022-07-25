from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.png', upload_to='DPs')
    
    def __str__(self):
        return f'{self.user.username}'
    
    def save(self):
        super().save()
        
        resize_image = Image.open(self.profile_pic.path)
        
        if resize_image.height > 300 and resize_image.width > 720:
            output_size = (300, 300)
            resize_image.thumbnail(output_size)
            resize_image.save(self.profile_pic.path)