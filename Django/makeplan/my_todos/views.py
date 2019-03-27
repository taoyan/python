from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import user.my_tool
from .models import Todo, Goal
import json
from django.utils import timezone
import datetime
from django.core import serializers

def synchronize(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        uid = params.get("userId")
        todo_params = params.get("todo")
        goal_params = params.get("goal")
        todo_last_modified = todo_params["lastModified"]
        todo_list = todo_params['dirtyData']
        goal_last_modified = goal_params["lastModified"]
        goal_list = goal_params['dirtyData']

        # todo
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

                if uid == user_id:
                    todo = Todo(ident, desc, group, schedule_date, finish_date, remind_type,
                            remind_date,icon_index,status,finish_type,user_id,
                            last_modified = timezone.now().strftime('%Y-%m-%d %H:%M:%S'))
                    todo.save()
        #返回所有lastmodified大于参数lastmodified的数据
        todos = []
        if todo_last_modified == None:
            todos_queryset = Todo.objects.filter(user_id=uid)
            todos = list(todos_queryset)
        else:
            last_modified_time = datetime.datetime.strptime(todo_last_modified, "%Y-%m-%d %H:%M:%S")
            new_last_modified_time = timezone.make_aware(last_modified_time, timezone.utc)
            todos_queryset = Todo.objects.filter(user_id=uid , last_modified__gt = new_last_modified_time)
            todos = list(todos_queryset)

        todo_dict_list = []
        for todo in todos:
            dict = todo.to_dict()
            todo_dict_list.append(dict)



        # goal
        if len(goal_list) > 0:
            for goal_dict in goal_list:
                ident = goal_dict["ident"]
                title = goal_dict["title"]
                start_date = goal_dict["startDate"]
                end_date = goal_dict["endDate"]
                content = goal_dict["content"]
                completeness = goal_dict["completeness"]
                status = goal_dict["status"]
                user_id = goal_dict["userId"]

                if uid == user_id:
                    goal = Goal(ident, title, start_date, end_date, content,
                                completeness,status,user_id,
                            last_modified = timezone.now().strftime('%Y-%m-%d %H:%M:%S'))
                    goal.save()
        goals = []
        if goal_last_modified == None:
            goals_queryset = Goal.objects.filter(user_id=uid)
            goals = list(goals_queryset)
        else:
            last_modified_time = datetime.datetime.strptime(goal_last_modified, "%Y-%m-%d %H:%M:%S")
            new_last_modified_time = timezone.make_aware(last_modified_time, timezone.utc)
            goals_queryset = Goal.objects.filter(user_id=uid, last_modified__gt=new_last_modified_time)
            goals = list(goals_queryset)

        goal_dict_list = []
        for goal in goals:
            dict = goal.to_dict()
            goal_dict_list.append(dict)

        return user.my_tool.json_response(data={"todo":todo_dict_list, "goal":goal_dict_list})