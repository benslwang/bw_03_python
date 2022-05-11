"""
在控制台连续输出五行'*'，要求每一行'*'数量依次递增
*
**
***
****
*****

# 定义一个计数变量row，从1开始计数.
row = 1
# 开始循环
while row <= 5:
    print('*' * row)
    row += 1
"""
# 定义一个行计数变量row，从1开始计数
row = 1
# 开始行循环
while row <= 5:
    # 开始列循环
    # 定义一个列计数变量col，从1开始计数
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1
