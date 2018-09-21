# 练习1:
# 现有如下代码， 会输出什么：
# class People(object):
#       __name = "luffy"
#       __age = 18
#
# p1 = People()
# print(p1.__name, p1.__age)




#练习2:
#编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法



#练习3:
#模仿王者荣耀定义两个英雄类
#要求：
#
#英雄需要有昵称、攻击力、生命值等属性；
#实例化出两个英雄对象；
#英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡(提示:这里是函数)


#练习4:
#请编写一段符合多态特性的代码.

# 练习5:下面三种实现单例的方法,哪一种写法是正确的,为什么多线程
class Single(object):
    __instance = None
    def __new__(cls):
        if not cls.__instance:
        	#写法一
            # cls.__instance = Single() #

            # 写法二
            # cls.__instance = super(Single, cls).__new__(cls)

            # 写法三
            cls.__instance = object.__new__(cls)

        return cls.__instance
A = Single()
B = Single()
print(id(A))
print(id(B))
