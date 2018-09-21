#练习1.创建自定义模块second_module
#second_module模块定义了全局变量,类(属性为私有,固定为(sex="男")),函数

#(1)列举不同导入的方式(注释说明不同)
#(2)#在主模块中只想使用econd_module中的类,其他不使用如何导入
#(3)在主模块利用second_module模块中的类创建对象,
# 创建对象之后:将私有属性修改为("女")(利用两种方式修改)

import second_moudle
print(second_moudle.g_num)

from second_moudle import show_info
show_info()


#练习2:
# (1)简述包中__init__.py的作用:
# (2)__all__方法在init.py模块和在其他模块中使用有什么不同


