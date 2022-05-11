# 计算0-10之间所有偶数的总和
# 定义一个变量i
i = 0
# 定义一个变量result
result = 0
# 开始循环
while i <= 100:
    # 判断i是否为偶数，如i为奇数，跳过当前数值，继续重复循环.
    if i % 2 != 0:
        # print(i)
        i += 1
        continue
    result += i
    i += 1
print(result)
