import requests
import prettytable as pt

headers = {
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1650422896; _ga=GA1.2.514309076.1650422896; _gid=GA1.2.1326405570.1650422896; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1650425381; kw_token=UPPNR6MTSQD'
    'csrf': 'UPPNR6MTSQD',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E7%A8%BB%E9%A6%99',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
url = "https://hm.baidu.com/hm.gif?hca=153A139CC2395B4E&cc=1&ck=1&cl=24-bit&ds=1440x900&vl=394&ep=3931%2C1803&et=3&ja=0&ln=zh-cn&lo=0&lt=1650422896&rnd=895676755&si=cdb524f42f0ce19b169a8071123a4797&su=http%3A%2F%2Fwww.kuwo.cn%2Fsearch%2Flist%3Fkey%3D%25E7%25A8%25BB%25E9%25A6%2599&v=1.2.92&lv=2&sn=57472&r=0&ww=1434&u=http%3A%2F%2Fwww.kuwo.cn%2Fsearch%2Flist%3Fkey%3D%25E7%25A8%25BB%25E9%25A6%2599"

response = requests.get(url, headers=headers)
print(response)
