"""
1.自定义函数sum_2_num()，求和
def sum_2_num():


    num1 = 10
    num2 = 20
    result = num1 + num2

    print("%d + %d = %d" % (num1, num2, result))


sum_2_num()
"""
# 2.函数参数的使用（在函数名后面的小括号内部填写参数，多个参数之间使用, 分割）
def sum_2_num(num1, num2):  # num1, num2是形参

    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))


sum_2_num(100, 50)  # 100, 50是实参
