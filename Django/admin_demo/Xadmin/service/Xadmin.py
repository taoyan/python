
from django.conf.urls import url
from django.shortcuts import HttpResponse, render

class ModelXadmin(object):
    list_display = ["__str__",]

    def __init__(self, model, site):
        self.model = model
        self.site = site


    @property
    def urls2(self):
        return self.get_urls2(), None, None

    def get_urls2(self):
        temp = []

        temp.append(url(r'^$', self.list_view))
        temp.append(url(r'^add/$', self.add_view))
        temp.append(url(r'^(\d+)/change/$', self.change_view))
        temp.append(url(r'^(\d+)/delete/$', self.delete_view))

        return temp

    def list_view(self, request):
        data_list = self.model.objects.all()
        model_name = self.model._meta.model_name


        # 表头
        header_list = []
        for field in self.list_display:
            if isinstance(field, str):
                if field=="__str__":
                    header = self.model._meta.model_name.upper
                    print(field)
                else:
                    # 获取字段，及字段属性
                    header = self.model._meta.get_field(field).verbose_name
            else:
                header = field(self, is_header = True)
            header_list.append(header)



        new_data_list = []
        for obj in data_list:
            temp = []
            for field in self.list_display:
                if isinstance(field, str):
                    # 反射，通过字符串找属性
                    temp.append(getattr(obj, field))
                else:
                    temp.append(field(self, obj))

            new_data_list.append(temp)

        return render(request, 'list_view.html', {"data_list":new_data_list, "model_name":model_name, "header_list":header_list})

    def add_view(self, request):
        return render(request, 'add_view.html')

    def change_view(self, request, id):
        return render(request, 'change_view.html')

    def delete_view(self, request, id):
        return render(request, 'delete_view.html')








class XadminSite(object):

    def __init__(self, name='admin'):
        self._registry = {}  # model_class class -> admin_class instance


    def register(self, model, admin_class=None, **options):
        if not admin_class:
            admin_class = ModelXadmin

        self._registry[model] = admin_class(model, self)

    @property
    def urls(self):
        return self.get_urls(), None, None

    def get_urls(self):
        temp = []

        for model, admin_class_obj in self._registry.items():
            app_name = model._meta.app_label
            model_name = model._meta.model_name
            temp.append(url(r'^{0}/{1}/'.format(app_name, model_name),admin_class_obj.urls2), )

        return temp

'''
r'app01/book', ModelXadmin(Book, site).urls2
r'app02/order', ModelXadmin(Order, site).urls2

'''


site = XadminSite()
