"""
获取所有的歌手信息
"""
import requests
from bs4 import BeautifulSoup
# from music_163 import sql

headers = {
    'authority': 'music.163.com',
    'method': 'GET',
    'path': '/discover/artist/cat',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'JSESSIONID-WYYY=rzJv2AYVnahxQOCYq9aPONF0jXNUBE7qrlQsIuF5N9KhSeAXaRIIiHb7QJa8Htk%2B0OE4X%2BUVjMrBkOpNgWRTnhWvvDUm7E1UhrwgFg2MJvlaWNrXhYl2NCmTivNbw8ZTyype%5CxRCQQ2Ct4MFTv5dDK4Qn4uzsrrnuN5JO8gcK2D5%2F3we%3A1607521063957; _iuqxldmzr_=32; _ntes_nnid=70802b3da94c287c0329d11493794ede,1607519264053; _ntes_nuid=70802b3da94c287c0329d11493794ede; NMTID=00O1RwL2I-5zln_AkwlqAt1zECWlG8AAAF2R50cGQ; WEVNSM=1.0.0; WNMCID=wqfaqh.1607519264904.01.0; WM_NI=wW02N%2FRqTC58k1ia4h5bEuFisfLNgnp7218eq9kTcEi4atBft3QaTPhisIw7Tfhqpx60Nmxwajh3rBIR9zqeJN8ApB6jvqYm1j3TSsrW8l7v7WQi9VD2k%2FUK74pu4HWPS3g%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed0cc6083ba9b8fae7ee98a8ea7c55b928a8babae6f988ee589aa429b899ad2cc2af0fea7c3b92ab58900d3cd2592af9ca4b834a9efa782b764f7be8b96c563b1ba84afe666b4e9fed2bb6fb3e7a5b5e24fabecaf95c16eb8ed9f82d75cacb7bdaaf63d98baa892f374f6f0828efb7da3b6a8d4f14a8b8ef79bf46f8a92f8a2f34af6b6ba92dc67f3b6fdb5d279b289f88db67ef5899f8abc5e88eea5d0d841f5ecc096b74495909dd4e637e2a3; WM_TID=9sAehU4gyp1BUUAQQFcuKWE6g7IMHVgZ',
    'referer': 'https://music.163.com/',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
params={
    'params': 'iHKIgGt4CJAl4TcDmckW69aHYbmjSoFQJEkIEQMTBlGJgzUVbh1GmvyGPI867eORa08k0weHz26+VQRFvTWkr1mfCfTfHr61qaKSuv3cDyOqOWTK/AWByTx/ZGpjpIM8',
    'encSecKey': 'd4e7bb7d102221a96000dc501f3c08fcce823612afa011fa64fc30a73b174260d5f2dc8d755a3fe8ca12e6a71c13a9ceb34210f9f4f42de4602959b00d8a5b824f97f37daeb89b67f4f9760a6b5aee551a91300413c326ffe325e2c394084bf30de496a345cfad95359a428bcd068e7687de61403c000c63043127de550ecee4'
}

def save_artist():
    r = requests.get('https://music.163.com/discover/artist',headers=headers)

    # 网页解析
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body

    hot_artists = body.find_all('a', attrs={'class': 'msk'})
    artists = body.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    for artist in hot_artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            print(artist_name,artist_id)
            # sql.insert_artist(artist_id, artist_name)
        except Exception as e:
            # 打印错误日志
            print(e)

    for artist in artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            # sql.insert_artist(artist_id, artist_name)
            print(artist_name, artist_id)
        except Exception as e:
            # 打印错误日志
            print(e)

def getallSinger():
    url = "https://music.163.com/weapi/artist/top?csrf_token="
    all = requests.get(url,params=params)
    print(all.text)

# 执行程序
# save_artist()
getallSinger()