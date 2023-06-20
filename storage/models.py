from django.db import models

# Create your models here.

class Storage(models.Model):
    Notes = models.TextField()
    Files = models.FileField(upload_to='files/', max_length=300, blank=True, null=True)