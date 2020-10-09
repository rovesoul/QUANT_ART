import re
import time
import csv
import requests
from bs4 import BeautifulSoup

def ten_guozhai():
    headers = {
        'Connection': 'keep-alive',
        'Content-Encoding': 'gzip',
        'Host':'cn.investing.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = "https://cn.investing.com/rates-bonds/china-10-year-bond-yield/"
    res = requests.get(url, headers=headers, )
    if res.status_code == 200:
        soup =BeautifulSoup(res.text,'html.parser')
        tens = soup.findAll(
            'span', id='last_last')
        tens = re.findall('>(.+)<',str(tens))
        return float(tens[0])

if __name__=='__main__':
    tens = ten_guozhai()  # 10年国债率
    print('十年国债收益率:',tens)