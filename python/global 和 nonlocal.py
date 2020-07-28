# global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量；
# 而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，只能用在嵌套函数中，
# 如果上一级函数中不存在该局部变量，nonlocal位置会发生错误（最上层的函数使用nonlocal修饰变量必定会报错）。
def scope_test():
    # 此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。
    # 此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam  # 使用外层的spam变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)