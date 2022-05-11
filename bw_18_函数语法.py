"""
1.
def printme( str ):
    "打印传入的字符串到标准显示设备上 "
    print(str)
    return
printme("我要调用用户自定义函数！")
printme("再次调用同一函数！")

2.
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return

3.
#调用printme函数
printme(str ='自学 Python')

# 可写函数说明
def printinfo( name, age ):
    "打印任何传入的字符串"
    print('姓名：', name)
    print('年龄：', age)
# 调用printinfo函数
printinfo(name ='python', age = 666)
"""

# 4.可写函数说明
def printinfo( name, age = 666 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return

#调用printinfo函数
printinfo( age=24, name="Python" )
print ("------------------------")
printinfo( name="Python" )
