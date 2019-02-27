from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import user.my_tool
from .models import Todo
import json
import time

def synchronize_todo(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        last_modified = params.get("lastModified")
        todo_list = params.get('dirtyData')
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
                                           last_modified=int(time.time()*1000))
                todo.save()
        #返回所有lastmodified大于参数lastmodified的数据
        return user.my_tool.json_response()