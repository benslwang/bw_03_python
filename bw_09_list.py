# list（列表）是python中使用最频繁的数据类型，专门用于存储一串信息
# 列表用[]定义，数据之间用,分割，索引从0开始
name_list = ["zhangsan", "lisi", "wangwu", "zhaoliu"]
# 列表长度
print(len(name_list))
# 计次
print(name_list.count("zhangsan"))
# 调用
print(name_list[3])
# 索引
print(name_list.index("wangwu"))
# 修改
name_list[1] = "李四"
print(name_list)
# 增加 append可以向列表末尾增加数据
name_list.append("王小二")
print(name_list)
# 插入
name_list.insert(2, "sunqi")
print(name_list)
# 合并
temp_list = ["孙悟空", "猪八戒", "沙和尚"]
name_list.extend(temp_list)
print(name_list)
# 删除 如列表中有重复数据，remove删除第一次出现的数据
name_list.remove("王小二")
print(name_list)
# pop方法默认可以把列表中最后一个元素删除
name_list.pop()
print(name_list)
# pop方法可以指定要删除元素的索引
name_list.pop(-4)
print(name_list)
# del关键字本质是将一个变量从内存中删除 可以删除列表元素，但不建议使用del
del name_list[3]
print(name_list)
# 清空列表
name_list.clear()
print(name_list)
# 列表排序
num_list = [3, 2, 19, 6, 9, 10, 8]
# 升序
num_list.sort()
print(num_list)
# 降序
num_list.sort(reverse=True)
print(num_list)
# 逆序
num_list.reverse()
print(num_list)
