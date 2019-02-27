from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.http import JsonResponse
from .. import my_tool

class UserAuth(MiddlewareMixin):

    def process_request(self,request):
        if request.method == 'POST':
            token = request.META.get('HTTP_TOKEN')
            if token:
                user_id = token.split('-')[0]
                cache_token = cache.get(user_id)
                if not cache_token:
                    return my_tool.json_response(outcome=3, message="您还未登录，请先登录")
                else:
                    if token != cache_token:
                        return my_tool.json_response(outcome=2, message="您被踢出，请重新登录")
                    else:
                        cache.set(user_id, token, 3600 * 24 * 10)
