from django.utils.deprecation import MiddlewareMixin
from .. import my_tool
from makeplan import settings

class UserAuth(MiddlewareMixin):

    def process_request(self,request):
        print(request.COOKIES)
        print(request.path)
        if request.path in settings.AUTH_LIST:
            token = request.META.get('HTTP_AUTHORIZATION')
            if not token:
                return my_tool.json_response(outcome=3, message="请先登录")
            result, payload = my_tool.verify_jwt_token(token)
            if result == True:
                print(payload)
                request.user_id = payload["userId"]
                request.mobile = payload["mobile"]
                return
            else:
                return my_tool.json_response(outcome=2, message="请重新登录")
        # if request.user.pk == None:
        #     return my_tool.json_response(outcome=1, message="请先登录")
        # if request.user.is_authenticated() == False:
        #     return my_tool.json_response(outcome=-1, message="回话过期，请重新登录")


    # def process_response(self, request,response):
    #     pass

