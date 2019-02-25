from django.utils.deprecation import MiddlewareMixin
import json
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse

class UserAuth(MiddlewareMixin):

    def process_request(self,request):
        if request.method == 'POST':
            token = request.META.get('HTTP_TOKEN')
            if token:
                user_id = token.split('-')[0]
                cache_token = cache.get(user_id)
                if not cache_token:
                    return JsonResponse({'msg':"请先登陆"})
                else:
                    if token != cache_token:
                        return JsonResponse({'msg':"您被踢出"})


    def process_response(self, request,response):
        print('2')
        return response