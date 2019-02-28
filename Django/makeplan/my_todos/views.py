from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import user.my_tool
from .models import Todo
import json
from django.utils import timezone
import datetime
from django.core import serializers

def synchronize_todo(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        last_modified = params.get("lastModified")
        todo_list = params.get('dirtyData')
        uid = params.get("userId")
        if len(todo_list) > 0:
            for todo_dict in todo_list:
                ident = todo_dict["ident"]
                desc = todo_dict["desc"]
                group = todo_dict["group"]
                schedule_date = todo_dict["scheduleDate"]
                finish_date = todo_dict["finishDate"]
                remind_type = todo_dict["remindType"]
                remind_date = todo_dict["remindDate"]
                icon_index = todo_dict["iconIndex"]
                status = todo_dict["status"]
                finish_type = todo_dict["finishType"]
                user_id = todo_dict["userId"]

                todo = Todo(ident, desc, group, schedule_date, finish_date, remind_type,
                            remind_date,icon_index,status,finish_type,user_id,
                            last_modified = timezone.now())
                todo.save()
        #返回所有lastmodified大于参数lastmodified的数据
        todos = []
        if last_modified == None:
            todos_queryset = Todo.objects.filter(user_id=uid)
            todos = list(todos_queryset)
        else:
            todos_queryset = Todo.objects.filter(user_id=uid, last_modified__gt=datetime.datetime.strptime(last_modified,"%Y-%m-%d %H:%M:%S.ssssZ"))
            todos = list(todos_queryset)

        dict_list = []
        for todo in todos:
            dict = todo.to_dict()
            dict_list.append(dict)
        return user.my_tool.json_response(data=dict_list)