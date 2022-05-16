str1 = "我的外号是'狒狒'"
print(str1)

str2 = 'hello python'
# 索引
print(str2[2:9])

# 遍历字符串
for c in str2:
    print(c)

# 统计字符串长度
print(len(str2))

# 统计某个字符串出现的次数
print(str2.count("o"))

# 某个字符串出现的位置
print(str2.index("p"))
# print(str2.find("p"))

# 判断字符串中是否只包含空格或空白字符（\t、\n、\r）
print(str2.isspace())

str_space = "   \t\n\r"
print(str_space.isspace())

# 判断字符串中是否都是字母
print(str2.isalpha())

# 判断字符串中是否都是字母和数字
print(str2.isalnum())

# 判断字符串中每个单词的首字母是否大写（即标题化）
print(str2.istitle())

# 判断字符串中所有的字符都是小写
print(str2.islower())

# 判断字符串中所有的字符都是大写
print(str2.isupper())

num_str = "3\u00b3"
print(num_str)

# 检查字符串是否已str开头(区分大小写)，是则返回True
print(str2.startswith("hello"))

# 检查字符串是否已str结束，是则返回True
print(str2.endswith("python"))

# 查找指定字符串
print(str2.find("llo"))
# 如果指定的字符串不存在，会返回-1
print(str2.find("lol"))
# 从右侧开始查找字符串
print(str2.rfind("llo"))

# 替换字符串
# replace方法执行完成之后，会返回一个新的字符串，
# 不会修改原有字符串的内容
print(str2.replace("python", "world"))

# 字符串文本对齐
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    # print(poem_str.center(10))
    # 居中对齐
    print("|%s|" % poem_str.center(10, "　"))  # 全角空格对齐效果最佳
    # 向左对齐
    print("|%s|" % poem_str.ljust(10, "　"))
    # 向右对齐
    print("|%s|" % poem_str.rjust(10, "　"))

# 去除空白字符
str2.strip()  # 截掉左右两边的空白字符
str2.lstrip()  # 截掉左边的空白字符
str2.rstrip()  # 截掉右边的空白字符

poem1 = ["\t\n登鹳雀楼",
         "王之涣",
         "白日依山尽",
         "黄河入海流\t\n",
         "欲穷千里目",
         "更上一层楼"]
for poem_str in poem1:
    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10, "　"))


# 字符串拆分和拼接
poem2 = "\t\n登鹳雀楼 王之涣\t\n 白日依山尽\t\n 黄河入海流\t\n 欲穷千里目\t\n 更上一层楼\t\n"
# 拆分字符串
poem_list = poem2.split()
# 拼接字符串
result = "　".join(poem_list)
print(result)

# 字符串切片
# 切片方法适用于字符串、列表、元祖
# 切片使用索引值来限定范围，从一个大的字符串中切出一个小的字符串
# 字典是一个无序的组合，是使用键值对保存数据
# 字符串[开始索引:结束索引:步长]

str_num = "0123456789"
# 截取从2~5位置的字符串
print(str_num[2:6])
# 截取从2~末尾的字符串
print(str_num[2:])
# 截取从开始~5位置的字符串
print(str_num[:6])
# 截取完整的字符串
print(str_num[:])
# 从开始位置，每隔一个字符截取字符串
print(str_num[::2])
# 从索引1开始，每隔一个取一个
print(str_num[1::2])
# 截取从2~末尾-1的字符串
print(str_num[2:-1])
# 截取字符串末尾两个字符
print(str_num[-2:])
# 字符串的逆序
print(str_num[-1::-1])
# 或者：
print(str_num[::-1])

