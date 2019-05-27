

from django import forms
from django.core.exceptions import ValidationError
from . import models

class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label="用户名",
        label_suffix=":",
        error_messages={
            "max_length":"用户名最长16位",
            "requred":"用户名不能为空",
        },
        widget=forms.widgets.TextInput(
            attrs={
                "class":"form-control"
            }
        ),
    )
    password = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class":"form-control"}
        ),
        error_messages={
            "min_length": "密码最短6位",
            "requred": "密码不能为空",
        }
    )
    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class":"form-control"}
        ),
        error_messages = {
            "min_length": "确认密码最短6位",
            "requred": "确认密码不能为空",
        }
    )
    email = forms.EmailField(
        label="邮箱",
        widget=forms.widgets.EmailInput(
            attrs={"class": "form-control"}
        ),
        error_messages={
            "invalid": "邮箱格式不正确",
        }
    )

    # 重写username的局部钩子
    def clean_username(self):
        print("username的钩子")
        username = self.cleaned_data.get("username")
        user = models.UserInfo.objects.filter(username = username)
        if user:
            self.add_error("username",ValidationError("用户名已存在"))
        else:
            return username

    def clean(self):
        print("总的钩子")
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password",ValidationError("两次密码不一致"))

        return self.cleaned_data
