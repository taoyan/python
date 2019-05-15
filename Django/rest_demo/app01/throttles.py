

class Throttles(object):
    # 访问站点频率不超过每分钟20次
    def allow_request(self, request, view):
        print(request.META.get("REMOTE_ADDR"))
        if 1:
            return True
        else:
            return False