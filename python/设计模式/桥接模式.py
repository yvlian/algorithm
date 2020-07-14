#形状（圆形、三角形）、颜色（红黄蓝）

#桥接模式前：
#形状类-->(圆形类、三角形类)  对于圆形类，还要创建（红色圆形类、黄色圆形类、蓝色圆形类）
#形状和颜色两个属性的高度耦合，造成类的数量特别多，而且不容易扩展。

#桥接模式
class ShapeAbstraction(object):
    def __init__(self,shape):
        self.shape = shape
    def set_color(self,color_object):
        self.color_object = color_object
    def draw(self):
        print(self.color_object.color + '_'+ self.shape)
class CircleShapeAbstraction(ShapeAbstraction):
    def __init__(self):
        super(CircleShapeAbstraction,self).__init__('Circle')
class TriangleShapeAbstraction(ShapeAbstraction):
    def __init__(self):
        super(TriangleShapeAbstraction,self).__init__('Triangle')

class ColorAbstarction(object):
    def __init__(self,color):
        self.color = color
class RedColorAbstarction(ColorAbstarction):
    def __init__(self):
        super(RedColorAbstarction,self).__init__('Red')
class YellowColorAbstarction(ColorAbstarction):
    def __init__(self):
        super(YellowColorAbstarction,self).__init__('Yellow')
class BlueColorAbstarction(ColorAbstarction):
    def __init__(self):
        super(BlueColorAbstarction,self).__init__('Blue')

circle = CircleShapeAbstraction()
circle.set_color(RedColorAbstarction())
circle.draw()

'''
优点：分离抽象接口与实现部分，提高系统可扩展性
缺点：增加系统的理解和设计难度，使用范围比较局限
'''