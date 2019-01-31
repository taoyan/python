from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Video
from django.http import HttpResponseRedirect, HttpResponse
from django.http import StreamingHttpResponse

def index(request):

    videos = Video.objects.all()

    return render(request, 'videos/index.html',{'videos':videos})
    # return HttpResponse("index")


def add_video(request):
    if request.method == 'GET':
        return render(request,'videos/add_video.html')
    else:
        file = request.FILES['myfile']
        if not file:
            return HttpResponse("sorry")
        else:
            with open('Media/%s' % file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return HttpResponse('success')


def download(request, file_name):

    def file_iterator(file, chunk_size = 512):
        with open(file, encoding='utf-8') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break;

    response = StreamingHttpResponse(file_iterator(file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
    return response