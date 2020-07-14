'''
继承的优点：提升代码的复用程度,避免重复操作。
继承的特点：
1、 同时支持单继承与多继承，当只有一个父类时为单继承，当存在多个父类时为多继承。
2、子类会继承父类所有的属性和方法，子类也可以覆盖父类同名的变量和方法。
3、在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。有别于C#
4、在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
5、Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。
    （先在本类中查找调用的方法，找不到才去基类中找）。
'''

class A(object):
    def __init__(self):
        print('A')

    def display(self):
        print('A dis')

class B(object):
    def __init__(self):
        print('B')

    def display(self):
        print('B dis')
class C(A,B):
    def __init__(self):
        # A.__init__(self)
        # B.__init__(self)
        super(A,self).__init__()
        super(B,self).__init__()
        print('C')
    def dis(self):
        A.display(self)
        B.display(self)

c = C()
print('++++++++++++++++++++++++++++++++++++++++++')
c.display()
print('++++++++++++++++++++++++++++++++++++++++++')
c.dis()

