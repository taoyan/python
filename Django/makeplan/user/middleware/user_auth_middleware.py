from django.utils.deprecation import MiddlewareMixin
from .. import my_tool
from makeplan import settings

class UserAuth(MiddlewareMixin):

    def process_request(self,request):
        print(request.COOKIES)
        print(request.path)
        if request.path not in settings.AUTH_LIST:
            return
        if request.user.pk == None:
            return my_tool.json_response(outcome=1, message="请先登录")
        if request.user.is_authenticated() == False:
            return my_tool.json_response(outcome=-1, message="回话过期，请重新登录")


    # def process_response(self, request,response):
    #     pass

