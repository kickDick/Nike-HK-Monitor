import requests
from datetime import datetime
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    'Referer':'https://www.nike.com.hk/'
    }

def parse_html():
    for url in url_list:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            html = BeautifulSoup(response.text,'lxml')
            page_items = html.find_all('dl', {'class':'product_list_content'})
            for i in page_items:
                item = i.get('code') + ' - https://www.nike.com.hk'+ i.get('pdpurl')
                if len(item.split(' - ')) != 2:
                    print('Error')
                else:
                    new_data.append(item)
    return new_data

def init_parse_html():
    for url in url_list:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            html = BeautifulSoup(response.text,'lxml')
            page_items = html.find_all('dl', {'class':'product_list_content'})
            for i in page_items:
                item = i.get('code') + ' - https://www.nike.com.hk'+ i.get('pdpurl')
                if len(item.split(' - ')) != 2:
                    print('Error')
                else:
                    old_data.append(item)
    return old_data

def main(start_item):
    old_data = start_item
    while True:
        new_data = parse_html
        difference = set(new_data) - set(old_data)
        if difference:
            print(difference)
        else:
            print(str(datetime.now()))

url_list = ['https://www.nike.com.hk/special_editions/list.htm?order=onShelvesTime_desc','https://www.nike.com.hk/man/all/list.htm?order=onShelvesTime_desc',]
new_data = []
old_data = []

if __name__ == "__main__":
    start_items = init_parse_html()




