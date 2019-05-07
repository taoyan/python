from django.shortcuts import render, HttpResponse

# Create your views here.

from django.views import View
from .models import Publisher


from rest_framework import serializers
class PublisherSerializers(serializers.Serializer):
    name = serializers.CharField()
    addr = serializers.CharField()


import json
class PublishView(View):
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
        publish_list = Publisher.objects.all()
        ps = PublisherSerializers(publish_list,many=True)
        return HttpResponse(ps.data)


    def post(self, request):
        pass