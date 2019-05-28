from django.utils.deprecation import MiddlewareMixin
from .. import my_tool
from makeplan import settings

class UserAuth(MiddlewareMixin):

    def process_request(self,request):
        print(request.META)
        print(request.COOKIES)
        if request.path in settings.AUTH_WHITE_LIST:
            return
        if request.user.pk == None:
            return my_tool.json_response(outcome=1, message="请先登录")

    def process_response(self, request,response):
        print(response)
        return

