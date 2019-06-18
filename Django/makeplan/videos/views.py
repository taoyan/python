from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.http import StreamingHttpResponse
from django.core import serializers
import json
from user import my_tool

from django.db.models import F
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
        page = json.loads(request.body).get('page')

        videos = Video.objects.all().values()
        paginator = Paginator(videos, per_page_count)
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



def detail2(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        video_id = params.get('ident')
        video = Video.objects.filter(pk=video_id).first()
        if not video:
            return my_tool.json_response(outcome=1, message="没有所请求的内容")

        bookmark = VideoBookmark.objects.filter(video=video).first()
        is_bookmark = True if bookmark != None else False
        data_dict = {"content": video.content.content,"isBookmark": is_bookmark}
        return my_tool.json_response(data=data_dict)




def bookmark(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        video_id = params.get('videoId')
        is_bookmark = params.get('isBookmark', True)
        bookmark = VideoBookmark.objects.filter(user=request.user, video_id=video_id).first()
        if not bookmark:
            bookmark = VideoBookmark(user=request.user, video_id=video_id, is_bookmark=is_bookmark)
            bookmark.save()
        else:
            bookmark.is_bookmark = is_bookmark
            bookmark.save()
        return my_tool.json_response(data={})



def my_bookmarks(request):
    if request.method == 'POST':
        videos = VideoBookmark.objects.filter(user=request.user, is_bookmark=True)\
            .values("video__nid","video__resource_url").extra('nid', 'resource_url')
        data_dict = {"videos":list(videos)}
        return my_tool.json_response(data=data_dict)





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


