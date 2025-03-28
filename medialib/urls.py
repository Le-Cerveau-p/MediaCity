
from django.urls import path
from . import views


urlpatterns = [
    # medislib/ is the root of the media library app
    path("", views.index, name="index"),
    # media/i
    path("<int:media_id>", views.details, name="details"),
    # crude
    path("crud", views.crud, name="crud")
    
]