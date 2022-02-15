'''
Author: KOneLane
Date: 2022-02-13 16:43:20
LastEditors: KOneLane
LastEditTime: 2022-02-15 14:40:41
Description: 
version: V
'''
import requests
from bs4 import BeautifulSoup as bs
import re
import os

class quanminksong:
    def __init__(self, url) -> None:
        
        self.url = url

        pass

    def __soupGet(self):
        """获得信息文字源代码"""
        # url = f'https://kg.qq.com/node/play?s=KuCG43K_O6KWxKZM'
        page = requests.get(self.url)
        soup = bs(page.content, 'html.parser')  #解析网页
        kk = str(soup)
        idx1 = re.search('playurl":"', kk).span()[1]
        # idx0 = re.search('', kk).span()[0]
        # print(kk[idx0:idx1])
        playurl = kk[idx1:].split('",')[0]
        return playurl

    def m4aDownload(self):
        playurl = self.__soupGet()
        print('下载链接：\n',playurl)

        res = requests.get(playurl)
        
        # music = res.content

        with open(self.GetDesktopPath()+'/1.mp3', 'ab') as file: #保存到本地的文件名
            file.write(res.content)
            file.flush()

    
    def GetDesktopPath(self):
        return os.path.join(os.path.expanduser("~"), 'Desktop')

if __name__ == "__main__":
    url = input('请把k歌页面网址复制在此后，按下回车\n')
    if url is not None:
        test = quanminksong(url)
        test.m4aDownload()
        print('下载完成')
        input('按任意键退出')
    else:
        input('地址输入前不要按回车，请重新运行程序')

