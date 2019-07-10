from django.shortcuts import render

# Create your views here.
from user import my_tool
from .models import Version
def check_version(request):

    if request.method == 'POST':
        version = Version.objects.order_by('-id').first()
        return my_tool.json_response(data = version.to_dict())

