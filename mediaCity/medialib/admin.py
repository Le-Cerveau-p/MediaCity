from django.contrib import admin
from .models import MediaItem, MediaCategory

# Register your models here.
admin.site.register(MediaItem)
admin.site.register(MediaCategory)
# Compare this snippet from mediaCity/medialib/admin.py:
