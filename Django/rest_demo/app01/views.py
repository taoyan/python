from django.shortcuts import render, HttpResponse

# Create your views here.

from django.views import View
from .models import Publisher, Book
from .serializer import PublisherSerializers, BookModelSerializers, BookSerializers, PublisherModelSerializers


import json
from rest_framework.views import APIView
class PublishView(APIView):
    def get(self, request):
        # 方式一
        # publish_list = list(Publisher.objects.all().values("name", "addr"))
        # print(publish_list)
        # return HttpResponse(json.dumps(publish_list))

        # 方式二
        # publish_list = Publisher.objects.all()
        # temp = []
        # for obj in publish_list:
        #     temp.append({
        #         "name":obj.name,
        #         "addr":obj.addr
        #     })
        # return HttpResponse(json.dumps(temp))

        # 方式三
        # from django.forms.models import model_to_dict
        # publish_list = Publisher.objects.all()
        # temp = []
        # for obj in publish_list:
        #     temp.append(model_to_dict(obj))
        # return HttpResponse(json.dumps(temp))


        # 方式四
        # from django.core import serializers
        # publish_list = Publisher.objects.all()
        # return HttpResponse(serializers.serialize("json",publish_list))

        # 方式五reset_framework
        # publish_list = Publisher.objects.all()
        # ps = PublisherSerializers(publish_list,many=True)
        # return HttpResponse(ps.data)
        # print(request.body)
        # print("aaaa",request.data)
        # print(request.GET)
        # return HttpResponse("ok123")

        publisher_list = Publisher.objects.all()
        # ps = BookSerializers(book_list, many=True)
        ps = PublisherModelSerializers(publisher_list, many=True)
        return Response(ps.data)

    def post(self, request):
        # print(type(request))
        # print(type(request._request))
        # print(request.body)
        print(request.data)     #json,urlencode都会转出来
        print(request.POST)     #只能弄出来urlencode的
        # # print(request._request.body)
        # return HttpResponse("ok")

        ps = PublisherModelSerializers(data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.errors)



from rest_framework.response import Response
class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        # ps = BookSerializers(book_list, many=True)
        bs = BookModelSerializers(book_list, many=True, context={"request":request})
        return Response(bs.data)


    def post(self, request):
        bs = BookModelSerializers(data=request.data)
        if bs.is_valid():
            print(bs.validated_data)
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)


class BookDetailView(APIView):
    def get(self, request, id):
        book = Book.objects.filter(pk=id).first()
        bs = BookModelSerializers(book)
        return Response(bs.data)


    def put(self, request, id):
        book = Book.objects.filter(pk=id).first()
        bs = BookModelSerializers(book, data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self, request, id):
        Book.objects.filter(pk=id).delete()
        return Response()




class PublishViewDetail(APIView):
    def get(self, request, pk):
        publish = Publisher.objects.filter(pk=pk).first()
        ps = PublisherModelSerializers(publish)
        return Response(ps.data)


    def put(self, request, pk):
        publish = Book.objects.filter(pk=pk).first()
        ps = PublisherModelSerializers(publish, data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.errors)

    def delete(self, request, pk):
        Publisher.objects.filter(pk=id).delete()
        return Response()