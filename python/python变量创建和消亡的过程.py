class a:
    def __init__(self):
        print("a()")

    def __del__(self):
        print("~a()")


class b:
    def __init__(self):
        print("b()")

    def hello(self):
        print("hello world")

    def __del__(self):
        print("~b()")


if __name__ == '__main__':
    print("let's begin test:")
    c = a()
    c = b()
    print("after c=b()")
    d = c
    print("after d=c")
    c.hello()
    d.hello()
    print(c, d)
    del c
    print("after del c")
    print(d)
    del d
    print("after del d")