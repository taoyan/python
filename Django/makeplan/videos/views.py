from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Video
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.http import StreamingHttpResponse
from django.core import serializers
import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def videos(request):
    per_page_count = 6
    if request.method == 'GET':
        videos = Video.objects.all()
        if not videos:
            return HttpResponse("sorry, no videos available")
        else:
            paginator = Paginator(videos, per_page_count)
            page = request.GET.get('page')
            try:
                videos = paginator.page(page)
            except PageNotAnInteger:
                videos = paginator.page(1)
            except EmptyPage:
                videos = paginator.page(paginator.num_pages)
            return render(request, 'videos/index.html', {'videos': videos})
    else:
        videos = Video.objects.all().values()
        paginator = Paginator(videos, per_page_count)
        page = json.loads(request.body).get('page')
        try:
            videos_page = paginator.page(page)
        except PageNotAnInteger:
            videos_page = paginator.page(1)
        except EmptyPage:
            videos_page = paginator.page(paginator.num_pages)
        dict = {}
        dict['videos'] = list(videos_page)
        dict['total'] = videos.__len__()
        return JsonResponse(dict, safe=False)



def detail(request, video_id):
    if request.method == 'GET':
        video = get_object_or_404(Video, pk = video_id)
        return render(request, 'videos/detail.html', {'video': video})
    else:
        video = get_object_or_404(Video, pk=video_id)
        if not video:
            return HttpResponse("sorry, no video available")
        else:
            json_data = serializers.serialize('json',(video,))
            return JsonResponse(json.loads(json_data), safe=False)



def add_video(request):
    if request.method == 'GET':
        return render(request,'videos/add_video.html')
    else:
        name = request.POST['name']
        detail = request.POST['detail']
        url = request.POST['url']
        pic_url = request.POST['pic_url']

        video = Video()
        video.name = name
        video.detail = detail
        video.url = url
        video.pic_url = pic_url
        video.save()
        return HttpResponseRedirect('/videos/index')

        # url = ""
        # file = request.FILES['myfile']
        # if not file:
        #     return HttpResponse("sorry, no file")
        # else:
        #     with open('Media/%s' % file.name, 'wb+') as destination:
        #         for chunk in file.chunks():
        #             destination.write(chunk)
        #     url = 'http://127.0.0.1:8000/videos/download/Media/%s' % file.name
        #
        #     video = Video()
        #     video.name = name
        #     video.detail = detail
        #     video.url = url
        #     video.save()
        #     return HttpResponseRedirect('/videos/index')

def delete_video(request):
    if request.method == 'POST':
        # video_id = eval(request.body.decode()).get('video_id')
        video_id = json.loads(request.body).get('video_id')
        video = get_object_or_404(Video, pk=video_id)
        if not video:
            return HttpResponse("sorry, no this video")
        else:
            video.delete()
            return HttpResponseRedirect('/videos/index')

def update(request, video_id):
    if request.method == 'GET':
        video = get_object_or_404(Video, pk=video_id)
        return render(request, 'videos/update_video.html', {'video':video})
    else:
        name = request.POST['name']
        detail = request.POST['detail']
        url = request.POST['url']

        video = get_object_or_404(Video, pk=video_id)
        video.name = name
        video.detail = detail
        video.url = url
        video.save()
        return HttpResponseRedirect('/videos/detail/%s' % video_id)


def download(request, file_name):

    def file_iterator(file, chunk_size = 512):
        with open(file, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break;

    path = 'media/%s' % file_name
    response = StreamingHttpResponse(file_iterator(path))
    response['Content-Type'] = 'video/mp4'
    # response['Content-Length'] = '1665024'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
    return response


