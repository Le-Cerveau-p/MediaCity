from django.forms import ModelForm
from .models import MediaItem

class MediaForm(ModelForm):
    class Meta:
        model = MediaItem
        fields = "__all__"