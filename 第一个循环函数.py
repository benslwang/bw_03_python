# 1.利用while函数打印hello python 5次

i = 'hello Python'
# 定义一个变量j来记录循环次数
j = 0
# 开始循环
while j < 5:
    # 希望在循环内执行的变量
    print(i)
    # 处理计数器
    j += 1
    if i == 3:
        continue



# 2.计算0-100之间所有数字累计求和结果

# 定义整数变量i 计算结果变量result.
i = 0
result = 0
# 开始循环
while i <= 100:
    # 设置j的取值范围
    result += i
# 设置计数器
    i += 1
print(result)
print('0-100之间的数字求和结果为 %d' % result)


# 3.计算0-100之间的所有偶数累计求和结果
# 定义整数变量i
i = 0
# 定义求和结果result
result = 0
# 开始循环
while i <= 100:
    # 判断i取值是否为偶数
    if i % 2 == 0:
        # 当i这个变量是偶数时，才进行相加
        result += i
# 设置计数器
    i += 1
print(result)
print('0-100之间所有偶数求和结果为 %d' % result)
