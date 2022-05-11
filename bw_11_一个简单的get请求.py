# 导入请求模块:
import urllib.request
url = "http://www.baidu.com"
# 发起请求，设置超时为1秒
response = urllib.request.urlopen(url, timeout=1)
# 使用read()读取整个页面内容，使用decode("utf-8")对获取的内容进行编码.
print(response.read().decode('utf-8'))
print(response.status)  # 状态码，判断是否成功，200
print(response.getheader('name'))  # 响应头，得到的一个元组组成的列表
print(response.getheader('server'))  # 得到特定的响应头
