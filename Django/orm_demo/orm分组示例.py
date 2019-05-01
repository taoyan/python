import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_demo.settings")
    import django
    django.setup()


    from app01 import  models

    # orm分组查询
    # select dept, AVG(salary) from employee group by dept;
    # 每个部门名称以及平均工资

    # ret = models.Employee.objects.all()
    # print(ret)
    # '''
    # SELECT `employee`.`id`, `employee`.`name`, `employee`.`age`, `employee`.`salary`, `employee`.`provice`, `employee`.`dept` FROM `employee` LIMIT 21; args=()
    # '''


    # ret = models.Employee.objects.all().values('dept')
    # print(ret)
    # '''
    # SELECT `employee`.`dept` FROM `employee` LIMIT 21; args=()
    # '''


    # ret = models.Employee.objects.values('dept').annotate()
    # print(ret)


    # annotate按照前面的字段分组
    # from django.db.models import Avg
    # ret = models.Employee.objects.values('dept').annotate(a = Avg('salary')).values('dept', 'a')
    # print(ret)
    # '''
    # SELECT `employee`.`dept`, AVG(`employee`.`salary`) AS `a` FROM `employee` GROUP BY `employee`.`dept` ORDER BY NULL LIMIT 21; args=()
    # '''


    from django.db.models import Avg
    # ret = models.Employee.objects.values('provice').annotate(a=Avg('salary')).values('provice', 'a')
    # print(ret)
    # '''
    # SELECT `employee`.`provice`, AVG(`employee`.`salary`) AS `a` FROM `employee` GROUP BY `employee`.`provice` ORDER BY NULL LIMIT 21; args=()
    # '''


    # ret = models.Person.objects.values('dept_id').annotate(a =Avg('salary')).values('dept__name', 'a')
    # print(ret)
    # '''
    # SELECT `dept`.`name`, AVG(`person`.`salary`) AS `a` FROM `person` INNER JOIN `dept` ON (`person`.`dept_id` = `dept`.`id`) GROUP BY `person`.`dept_id`, `dept`.`name` ORDER BY NULL LIMIT 21; args=()
    # '''

    # ret = models.Person.objects.values('dept_id')
    # print(ret)
    # '''
    # SELECT `person`.`dept_id` FROM `person` LIMIT 21; args=()
    # '''


#     查询person表，判断每个人工资是否大于两千
#     额外执行sql
#     '''
#     SELECT (salary > 2000) AS `gt`, `person`.`id`, `person`.`name`, `person`.`salary`, `person`.`dept_id` FROM `person` LIMIT 21; args=()
#     '''
#     ret = models.Person.objects.all().extra(
#         select={"gt":"salary > 2000"}
#     )
#     print(ret)
#     for i in ret:
#         print(i.name, i.gt)



#     执行原生的sql
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("""select * from person where id = %s""",[1])
    row = cursor.fetchone()
    print(row)
