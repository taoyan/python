from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from user import my_tool
from .models import Todo, Goal, TimeRecord
import json
from django.utils import timezone
import datetime

def synchronize(request):
    if request.method == 'POST':
        current_user_id = request.user_id

        params = json.loads(request.body)
        todo_params = params.get("todo")
        goal_params = params.get("goal")
        timerecord_params = params.get('timeRecord')

        todo_last_modified = todo_params["lastModified"]
        todo_list = todo_params['dirtyData']
        goal_last_modified = goal_params["lastModified"]
        goal_list = goal_params['dirtyData']
        timerecord_last_modified = timerecord_params["lastModified"]
        timerecord_list = timerecord_params['dirtyData']

        # todo
        # 返回所有lastmodified大于参数lastmodified的数据
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

                todo = Todo(ident, desc, group, schedule_date, finish_date, remind_type,
                            remind_date, icon_index, status, user_id=current_user_id)
                todo.save()

        #返回所有lastmodified大于参数lastmodified的数据
        todos = []
        if todo_last_modified == None:
            todos_queryset = Todo.objects.filter(user_id=current_user_id)
            todos = list(todos_queryset)
        else:
            todos_queryset = Todo.objects.filter(user_id=current_user_id, last_modified__gt=todo_last_modified)
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
                content = goal_dict["content"]
                status = goal_dict["status"]

                goal = Goal(ident, title, content,
                            status, user_id=current_user_id)
                goal.save()

        goals = []
        if goal_last_modified == None:
            goals_queryset = Goal.objects.filter(user_id = current_user_id)
            goals = list(goals_queryset)
        else:
            goals_queryset = Goal.objects.filter(user_id=current_user_id, last_modified__gt=goal_last_modified)
            goals = list(goals_queryset)

        goal_dict_list = []
        for goal in goals:
            dict = goal.to_dict()
            goal_dict_list.append(dict)


        # timerecord
        if len(timerecord_list) > 0:
            for timerecord_dict in timerecord_list:
                ident = timerecord_dict["ident"]
                date = timerecord_dict["date"]
                time_counts = timerecord_dict["timeCounts"]
                goal_id = timerecord_dict["goalId"]

                time_record = TimeRecord(ident, date, time_counts, user_id=current_user_id, goal_id=goal_id)
                time_record.save()

        records = []
        if timerecord_last_modified == None:
            records_queryset = TimeRecord.objects.filter(user_id = current_user_id)
            records = list(records_queryset)
        else:
            records_queryset = TimeRecord.objects.filter(user_id=current_user_id, last_modified__gt=timerecord_last_modified)
            records = list(records_queryset)

        records_dict_list = []
        for record in records:
            dict = record.to_dict()
            records_dict_list.append(dict)


        return my_tool.json_response(data={"todo":todo_dict_list, "goal":goal_dict_list,
                                                "timeRecord":records_dict_list})