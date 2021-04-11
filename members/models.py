from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='def.jpg', upload_to='images/profile')
    biography = models.TextField()
    personal_website = models.CharField(max_length=255, null=True, blank=True)
    facebook_account = models.CharField(max_length=255, null=True, blank=True)
    twitter_account = models.CharField(max_length=255, null=True, blank=True)
    instagram_account = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


"""
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    biography = models.TextField()
    my_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    personal_website = models.CharField(max_length=255, null=True, blank=True)
    facebook_account = models.CharField(max_length=255, null=True, blank=True)
    twitter_account = models.CharField(max_length=255, null=True, blank=True)
    instagram_account = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('blog:homepage')
"""
