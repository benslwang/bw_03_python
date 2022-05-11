name = "小明"


def say_hello():
    print("hello1")
    print("hello2")
    print("hello3")


print(name)
# 只有在调用函数时，之前的函数才会被执行
# 函数执行完成后，会重新回到之前的程序中，继续执行后续的代码
say_hello()



