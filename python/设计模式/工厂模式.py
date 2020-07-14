'''
工厂模式分为：
简单工厂模式（并不在23中模式之中），工厂方法模式以及抽象工厂模式，
其中我们通常所说的工厂模式指的是工厂方法模式，工厂方法模式是日常开发中使用频率最高的一种设计模式。
'''

class Triangle2D(object):
    def __init__(self):
        print('Triangle_2D')
    def __repr__(self):
        print('Triangle_2D')
class Circle2D(object):
    def __init__(self):
        print('Circle_2D')
    def __repr__(self):
        print('Circle_2D')

#简单工厂：
# （1）需要创建的对象较少；　
# （2）客户端不关心对象的创建过程
class SimpleShapeFactory(object):
    @staticmethod
    def get_shape(shape_type='Circle'):
        if shape_type == 'Circle':
            return Circle2D()
        elif shape_type == 'Triangle':
            return Triangle2D()
        return None
print('---------------简单工厂----------')
circle = SimpleShapeFactory().get_shape()
triangle = SimpleShapeFactory().get_shape('Triangle')

#工厂方法
# （1）客户端不需要知道它所创建的对象的类。例子中我们不知道每个形状的类具体叫什么名，只知道创建它的工厂名就可以创建形状。
# （2）客户端可以通过子类来指定创建对应的对象。
import abc
class AbstractShapeFactory(object):
    __metaclass = abc.ABCMeta
    @abc.abstractmethod
    def get_shape(self):
        pass
class TriangleFactory(AbstractShapeFactory):
    def get_shape(self):
        return Triangle2D()
class CircleFactory(AbstractShapeFactory):
    def get_shape(self):
        return Circle2D()

print('---------------工厂方法----------')
circle = CircleFactory().get_shape()
triangle = TriangleFactory().get_shape()

#抽象工厂
# （1）和工厂方法一样客户端不需要知道它所创建的对象的类。
# （2）需要一组对象共同完成某种功能时。并且可能存在多组对象完成不同功能的情况。
# （3）系统结构稳定，不会频繁的增加对象。（因为一旦增加就需要修改原有代码，不符合开闭原则）
#共两种三角形，两种圆形
class Triangle3D(object):
    def __init__(self):
        print('Triangle_3D')
    def __repr__(self):
        print('Triangle_3D')
class Circle3D(object):
    def __init__(self):
        print('Circle_3D')
    def __repr__(self):
        print('Circle_3D')

class AbstractShapeFactory1(object):
    __metaclass = abc.ABCMeta
    @abc.abstractmethod
    def get_triangle(self):
        pass
    @abc.abstractmethod
    def get_circle(self):
        pass
class Shape2DFactory(AbstractShapeFactory1):
    def get_triangle(self):
        return Triangle2D()
    def get_circle(self):
        return Circle2D()
class Shape3DFactory(AbstractShapeFactory1):
    def get_triangle(self):
        return Triangle3D()
    def get_circle(self):
        return Circle3D()
print('---------------抽象方法----------')
circle_2D = Shape2DFactory().get_circle()
triangle_3D = Shape3DFactory().get_triangle()

