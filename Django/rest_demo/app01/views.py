from django.shortcuts import render, HttpResponse

# Create your views here.

from django.views import View
from .models import Publisher, Book, Author, User, Token
from .serializer import PublisherSerializers, BookModelSerializers,\
    BookSerializers, PublisherModelSerializers, AuthorModelSerializers


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


from rest_framework import exceptions
# class TokenAuth(object):
#     def authenticate(self, request):
#         token = request.GET.get("token")
#         token_obj = Token.objects.filter(token=token).first()
#         if not token_obj:
#             raise exceptions.AuthenticationFailed("验证失败")
#         else:
#             return token_obj.user, token_obj.token
#
#     def authenticate_header(self, request):
#         pass


# from rest_framework.authentication import BaseAuthentication
# class TokenAuth(BaseAuthentication):
#     def authenticate(self, request):
#         token = request.GET.get("token")
#         token_obj = Token.objects.filter(token=token).first()
#         if not token_obj:
#             raise exceptions.AuthenticationFailed("验证失败")
#         else:
#             return token_obj.user, token_obj.token

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = "page"
    page_size_query_param = "size"
    max_page_size = 3

class MyLimitPageNumberPagination(LimitOffsetPagination):
    default_limit = 2




from .auth import TokenAuth
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
class BookView(APIView):
    # authentication_classes = [TokenAuth,]
    # permission_classes = []
    # throttle_classes = []

    parser_classes = [JSONParser]

    def get(self, request):
        # print(request.body)
        book_list = Book.objects.all()
        # ps = BookSerializers(book_list, many=True)
        # 序列集合,many=True
        # HyperlinkedIdentityField  context={"request":request}

        # 分页
        # from rest_framework.pagination import PageNumberPagination
        # pnp = PageNumberPagination()
        # pnp.page_size = 2
        # pnp = MyPageNumberPagination()
        pnp = MyLimitPageNumberPagination()
        books_page = pnp.paginate_queryset(book_list, request, self)

        bs = BookModelSerializers(books_page, many=True, context={"request":request})
        return Response(bs.data)


    def post(self, request):
        # 序列化数据转model
        bs = BookModelSerializers(data=request.data)
        if bs.is_valid():
            print(bs.validated_data)
            # 自定义时候重写create()
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
            # 自定义时候重写update()
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






from rest_framework import mixins
from rest_framework import generics

# class AuthorView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class AuthorDetailView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializers
#
#     def get(self, request, pk, *args, **kwargs):
#         return self.retrieve(request,pk, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers




from rest_framework.response import Response
from .permission import SVIPPermission
from .throttles import Throttles
from rest_framework import viewsets
class AuthorModelView(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuth, ]
    # permission_classes = [SVIPPermission, ]
    # throttle_classes = [Throttles,]

    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializers
    pagination_class = MyPageNumberPagination



class LoginView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        user = User.objects.filter(name = request.data.get("name"), pwd=request.data.get("pwd")).first()
        res = {"state_code":1000, "msg":None}
        if user:
            random_str = get_random_str(user.name)
            token = Token.objects.update_or_create(user=user, defaults={"token":random_str})
            res["token"] = token[0].token
        else:
            res["state_code"] = 1001
            res["msg"] = "用户名或密码错误"
        return Response(json.dumps(res))



def get_random_str(user):
    import hashlib,time
    ctime = str(time.time())

    md5 = hashlib.md5(bytes(user, encoding="utf8"))
    md5.update(bytes(ctime, encoding="utf8"))

    return md5.hexdigest()