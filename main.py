import os
import requests
import os
import time
from urllib.parse import unquote

def crate_new_folder():
    path = "new_folder/sub_folder/child_folder"
    os.makedirs(path)

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
url = 'https://www.curseforge.com/minecraft/mc-mods/sodium/download/5284882'
path = 'new_folder/sub_folder/child_folder'

def get_file_name(url, headers):
    filename = ''
    if 'Content-Disposition' in headers and headers['Content-Disposition']:
        disposition_split = headers['Content-Disposition'].split(';')
        if len(disposition_split) > 1:
            if disposition_split[1].strip().lower().startswith('filename='):
                file_name = disposition_split[1].split('=')
                if len(file_name) > 1:
                    filename = unquote(file_name[1])
    if not filename and os.path.basename(url):
        filename = os.path.basename(url).split("?")[0]
    if not filename:
        return time.time()
    return filename

def start(url, thread_num):
    get_file = requests.get(url=url, headers=headers, stream=True, allow_redirects=False, timeout=10)
    content_length = get_file.headers['Content-Length']
    file_name = get_file_name(url, get_file.headers)
    print("文件大小：", content_length, "文件名称：" + file_name)
    print(int(content_length) / int(thread_num))

start(url,20)