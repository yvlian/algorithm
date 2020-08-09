def m():
    try:
        # raise IndentationError('haha')   #如果想要让上层函数处理异常，可以raise
        3/h
        print('try')
    except:
        print('excepghjgjt')
        return 1
    else:
        print('else')
        return 2
    finally:
        print('finally')
    print('after finally')
    return 3
print(m())

#with...语句相当于try-finally语句的简写，可以替代try-finally的功能。
# finally的作用是，无论except是否捕捉到异常，finally后面的代码都会执行，try获取了资源，finally释放资源，保证了收尾工作。
#若return 在finally前面的位置，且被执行了，finally仍会执行

# 语法错误：是指代码不符合解释器或者编译器语法
# 异常：是指不完整、不合法输入，或者计算出现错误


#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。