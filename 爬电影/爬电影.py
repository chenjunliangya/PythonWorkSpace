import re
import time

import requests

headers = {
    'authority': 'youku.cdn4-okzy.com',
    'method': 'GET',
    'path': '/20201115/11611_e6c1d52b/1000k/hls/index.m3u8',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer':'https://youku.cdn4-okzy.com/share/433a6ea5429d6d75f0be9bf9da26e24c',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

def downVideo():
    downUrl = 'https://youku.cdn4-okzy.com/20201115/11611_e6c1d52b/1000k/hls/'
    getAllFileName()
    allname = readAllFileName()
    for i in allname:
        time.sleep(1)
        video = requests.get(downUrl+i).content
        file = open("F:\\Down\\"+i+".mp4", "wb")
        file.write(video)
        file.flush()
        file.close()
        print(i+"文件下载成功")


def readAllFileName():
    filename = "F:\\Down\\da.txt"
    allName = []
    # 将文件内容读取出来转为list
    with open(filename, 'r') as f:
        for line in f.readlines():
            linestr = line.strip()
            # 正则匹配字母和数字
            name = re.match('[a-z0-9.]', linestr, flags=0)
            # 如果那么不是None则放到名称数组中
            if not name is None:
                allName.append(linestr)
    return allName

def getAllFileName():
    url = "https://youku.cdn4-okzy.com/20201115/11611_e6c1d52b/1000k/hls/index.m3u8"
    allname = requests.get(url).content
    file = open("F:\\Down\\da.txt", "wb")
    file.write(allname)
    file.flush()
    file.close()
    print("请求名称文件写入成功")

# getAllFileName()
# readAllFileName()
downVideo()