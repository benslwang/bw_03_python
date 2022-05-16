"""
字典用{}表示
通常用于存储描述一个物体的相关信息
字典使用键值对存储数据，键值对之间使用,分隔
键key是索引
键value是数据，且只能使用字符串，数字或者元祖
键和值之间使用:分隔
键是唯一的，值可以取任意数据类型，
"""
xiaoming = {"name": "小明",
            "age": 18}
# 取值
print(xiaoming["name"])
# 增加，如果key不存在，会新增键值对
xiaoming["weight"] = 80
# 修改，如果key存在，会修改键值对
xiaoming["name"] = "小小明"
# 删除
xiaoming.pop("age")
# 统计键值对数量
print(len(xiaoming))
# 合并字典
xiaoming1 = {"gender": True,
             "height": 1.77,
             "age": 22}
# 如果被合并的字典中包含已经存在的键值对时，会覆盖原来的键值对
xiaoming.update(xiaoming1)
# 清空字典
xiaoming.clear()
print(xiaoming)
# 字典迭代遍历
xiaoming2 = {"gender": False,
             "height": 1.87,
             "age": 32}
for k in xiaoming2:
    print("%s - %s" % (k, xiaoming2[k]))

card_list = [
    {"name": "zhangsan",
     "qq": 363111516,
     "phone": 123123},
    {"name": "lisi",
     "qq": 363121516,
     "phone": 12341234}
]

for card_info in card_list:
    print(card_info)
