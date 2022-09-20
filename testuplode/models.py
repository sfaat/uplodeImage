from django.db import models

# Create your models here.

class Uplode(models.Model):
    name=models.CharField(max_length=200,null=True, blank=True)
    pic = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.name