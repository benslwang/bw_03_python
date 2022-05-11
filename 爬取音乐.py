# 导入库
import requests

# 需求路径
url = "https://other-web-nf01-sycdn.kuwo.cn/100666d2e5d251952c7c087a7e6a82c8/625fac99/resource/n2/25/44/97165461.mp3"

# 获取音乐内容
r = requests.get(url)

music = r.content

# 设置保存路径，并下载音乐.
"""
with open("保存路径和文件名", "以什么形式写入“) as 文件对象:
    文件对象.方法(文件)
./ 放在当前目录下
wb 以二进制的形式写入
"""
with open("./稻香.mp3", "wb") as f:
    f.write(music)

