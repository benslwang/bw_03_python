x = ["apple", "banana", "cherry"]  # list列表
print(type(x))
x = ("apple", "banana", "cherry")  # tuple元祖
print(type(x))
x = {"apple", "banana", "cherry"}  # set集合
print(type(x))


def hello_world():
    print('hello world')


hello_world()

a = "Hello, World!"
print(a[1])  # 切片，获取位置1处的字符（从0开始计数）

# 循环遍历单词“hello world”中的字母
for x in 'hello world':
    print(x)

# len()函数返回一个字符串的长度，标点符号和空格也算一个长度
a = "hello, world"
print(len(a))

# 要检查字符串中是否存在某个短语或者字符，我们可以使用关键字in
txt = "the best things in life are free."
print('free' in txt)

# 切片 获取从位置3到位置9（不包括在内）的字符，从0开始计数
b = "Hello, World!"
print(b[3:9])

# 从头开始切 获取从开始到位置5（不包括在内）的字符，从0开始计数
b = "Hello, World!"
print(b[:5])

# 切到最后 获取从2开始到最后的字符，从0开始计数
b = "Hello, World!"
print(b[2:])

# 小写转大写 upper()以大写形式返回字符串
b = "Hello, World!"
print(b.upper())


# 大写转小写 lower()以小写形式返回字符串
b = "Hello, World!"
print(b.lower())

# 空白是指实际文本之前和之后的空间，通常需要删除这个空间
# 删除空格 strip()从开头或结尾删除任何空格
b = " Hello, World! "
print(b.strip())

# 字符串替换 replace()用一个字符串替换另一个字符串
b = "hello, world!"
print(b.replace('world', 'python'))

# 拆分字符串 split()方法返回一个列表，其中指定分隔符之间的文本成为列表项。split()如果找到分隔符的实例，该方法会将字符串拆分为子字符串。
a = "hello, world!"
print(a.split(","))

# 字符串连接 连接或组合两个字符串，可使用运算符+
a = 'hello'
b = 'world'
c = a + ' ' + b  # c = a + b
print(c)

# 格式化字符串 format()方法接受传递的参数，格式化它们，并将它们放在占位符{}所在的字符串中
age = 20
price = 3000
cost = 49.95
my_order = "川川今年 {}岁 买了个华为手机 {} 每个月花费 {} 元."
print(my_order.format(age, price, cost))


# 也可以使用索引号{0}来确保参数放置在正确的占位符中
age = 20
price = 3000
cost = 49.95
my_order = "川川今年 {1}岁 买了个华为手机 {2} 每个月花费 {0} 元."
print(my_order.format(age, price, cost))

x = "Hello World"
print(len(x))


