from django.shortcuts import render
from django.http import HttpResponse
from .models import MediaItem, MediaCategory
from .forms import MediaForm

# Create your views here.
def index(request):
    allCategory = MediaCategory.objects.all()
    context = {
        "allCategories": allCategory
    }
    return render(request, "categories.html", context)

def details(request, media_id):
    citems = MediaCategory.objects.get(pk=media_id)
    pitems = MediaItem.objects.filter(category=citems)
    context = {
        "pitems": pitems,
        "citems": citems,
        # "print": print
    }
    print(citems)
    return render(request, "media_items.html", context)

def crud(request):
    form = MediaForm()
    mediaItems = MediaItem.objects.all()
    context = {
        "mediaItems": mediaItems,
        "title": "Manage Items"}
    if request.method == "POST":
        if "save" in request.POST:
            pk = request.POST.get("save")
            if not pk:
                form = MediaForm(request.POST)
            else:
                item = MediaItem.objects.get(id=pk)
                form = MediaForm(request.POST, instance=item)                
            form.save()            
            form = MediaForm()
        elif "delete" in request.POST:
            pk = request.POST.get("delete")
            item = MediaItem.objects.get(id=pk)
            item.delete()
        elif "edit" in request.POST:
            pk = request.POST.get("edit")
            item = MediaItem.objects.get(id=pk)
            form = MediaForm(instance=item)
            
    context["form"] = form
    return render(request, "crud.html", context)