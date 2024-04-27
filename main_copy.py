import requests
import wget
import hashlib
import os
from urllib.parse import urlparse


# 新建下载文件夹
def crate_new_folder():
    path = "download"
    os.makedirs(path)

# 计算文件SHA256值
def count_SHA256(SHA256_path):
    SHA256_path = 'fast-ip-ping-mc1.20.4-fabric-v1.0.1.jar' 
    algorithm = hashlib.sha256()
    size = os.path.getsize(SHA256_path)
    with open(SHA256_path, 'rb') as f:
        while size >= 1024 * 1024:
            algorithm.update(f.read(1024 * 1024))
            size -= 1024 * 1024
        algorithm.update(f.read())
    print(algorithm.hexdigest(), SHA256_path)

#获取文件名
def get_file_information(url):
    a = urlparse(url)
    file_path = a.path
    file_name = os.path.basename(a.path)
    _,file_suffix = os.path.splitext(file_name)
    return file_name,file_suffix

''' 请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'officecdn-microsoft-com.akamaized.net',
    'Pragma': 'no-cache',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
'''

url = 'https://cdn.modrinth.com/data/9mtu0sUO/versions/U5CYxkEG/fast-ip-ping-mc1.20.4-fabric-v1.0.1.jar'
download_path = 'download'
# wget.download(url, out=file_name+file_suffix)

print(get_file_information(url))


