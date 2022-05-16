# 元祖用()定义，数据之间用,分割，索引从0开始
info_tuple = ('Zhangsan', 18, 1.77)

# 使用迭代遍历元祖
for my_info in info_tuple:
    print(my_info)

# 元祖中保存的数据类型一般是不一样的

# 格式化字符串后面的'()'本质上就是元祖
print("%s的年龄是 %d, 身高是 %.2f" % info_tuple)

# 元祖中的内容不可被修改
