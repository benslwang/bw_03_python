url = "https://lb-sycdn.kuwo.cn/8dfd0e471cd98b240db4d201d12b19a3/625585d7/resource/n2/83/48/3581721986.mp3"

import requests

r = requests.get(url)

music = r.content
with open("./柳叶刀.mp3", "wb") as f:
    f.write(music)
# ./ 放在当前目录下
# wb 代表二进制的写入方式
