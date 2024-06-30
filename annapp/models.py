from django.db import models

# Create your models here.
class Ann(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ann_images')
    description = models.TextField()
    date = models.DateField(auto_now=True)
