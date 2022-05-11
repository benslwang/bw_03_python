"""
作者：Ben Wang
时间：2022/4/21
"""
a = 2
b = 3
c = a - b
d = a - b
print(c, d)


def sum_2_num(num1, num2):
    """对两个数字的求和"""

    result = num1 + num2

    # 可以使用返回值告诉调用方计算的结果
    return result

# 可以使用变量，来接收函数执行的返回结果

sum_result = sum_2_num(60, 80)

print("计算结果：%d" % sum_result)

mylist = ["bw一号", "bw二号", "bw三号"]
print(mylist)
mylist = ["bw一号", "bw二号", "bw三号", "bw二号", "bw三号"]
print(mylist)