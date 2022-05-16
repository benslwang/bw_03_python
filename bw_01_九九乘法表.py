# 分析九九乘法表构成（观察发现，乘法表中，乘号左边的数字是列号，乘号右边的数字是行号）
# 1.while循环版九九乘法表
def multiple_table():

    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            # \t 在控制台输出一个字符表，协助在输出文本时，垂直方向保持对齐。
            col += 1
        print("")
        row += 1


"""
for循环版九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # print(j, "*", i, "=", j * i, end='  ')
        print("%d * %d = %d" % (j, i, j * i), end="\t")
    print('\n')
"""
