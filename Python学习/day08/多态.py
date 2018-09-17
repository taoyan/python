#python本质上不存在多态（约定俗成）
#多态，关注的是同一个方法，但是会出现不同形式

class Text(object):
    def show(self):
        print('显示文字')


class Image(object):
    def show(self):
        print('显示图片')

class Video(object):
    def show(self):
        print('显示视频')

class Person():
    def show(self):
        print('我在跳舞')


#显示数据的方法
def show_data(data):
    #关心的是同一个方法，会有不同的表现形式
    #在python里面多态只关心对象方法，不关心对象类型
    data.show()

image = Image()
text = Text()
video = Video()

show_data(image)
show_data(video)


    