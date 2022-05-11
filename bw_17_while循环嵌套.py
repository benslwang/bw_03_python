"""
用python代码编辑"*"，如下图
*
**
***
****
*****
"""

# 定义一个变量row，计数从1开始.
row = 1
# 开始循环
while row <= 5:

    # 定义另一变量col，在循环里面开始新的循环，计数从1开始
    col = 1
    # 开始循环
    while col <= row:
        print("*", end="")
        col += 1
    print("")  # print("")只要求换行，并无打印实际内容

    row += 1
