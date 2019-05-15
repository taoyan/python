from .models import User

class SVIPPermission(object):
    message = "只有超级用户才能访问"
    def has_permission(self, request, view):
        # user_name = request.user
        # print(user_name)
        # user_type = User.objects.filter(name = user_name).first().user_type
        # auth未通过会返回匿名用户
        if request.auth == None:
            return False

        user_type = request.user.user_type
        if user_type == 3:
            return True
        else:
            return False