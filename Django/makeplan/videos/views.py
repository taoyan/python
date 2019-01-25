from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Video
from django.http import HttpResponseRedirect, HttpResponse

def index(request):

    videos = Video.objects.all()

    return render(request, 'videos/index.html',{'videos':videos})
    # return HttpResponse("index")