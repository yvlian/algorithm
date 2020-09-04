# 声明形参的时候是父类对象，实际运行的时候是子类对象
# 其实在Python中，列表，字典都是多态的体现
class Pay():
    def pay(self,money):
        pass

class Alipay(Pay):
    '支付宝支付'
    def pay(self,money):#Overrides
        print('使用了支付宝支付了%s元'%money)

class Applepay(Pay):
    '苹果支付'
    def pay(self,money):#Overrides
        print('使用了applepay支付了%s元'%money)

class Customer():
    def consumption(self,pay,money):
        pay.pay(money)

alipay=Alipay()
applepay=Applepay()
customer_1=Customer()
#使用支付宝支付
customer_1.consumption(alipay,100)
#使用苹果支付'
customer_1.consumption(applepay,98)