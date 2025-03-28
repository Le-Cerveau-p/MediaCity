from django.db import models

# Create your models here.

class MediaCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    categorycover = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.name}"

class MediaItem(models.Model):
    category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
