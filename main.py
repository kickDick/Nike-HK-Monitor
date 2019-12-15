import time
import requests
from dhooks import *
from datetime import datetime
from bs4 import BeautifulSoup

# Your webhook url for error message
error_webhook = ''
#Your Webhook url for monitor message
monitor_webhook = ''


headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    'Referer':'https://www.nike.com.hk/'
    }


def post_discord(sku,link):
    image = 'https://img.nike.com.hk/resources/product/%s/%s_BL1.png'% (sku,sku)
    hook = Webhook(monitor_webhook)
    embed = Embed(description='SKU: '+str(sku),color=0x36393F,timestamp='now')
    try:
        title_response = requests.get(link,headers=headers)
        title_html = BeautifulSoup(title_response.text,'lxml')
        title = title_html.title.text
        embed.set_title(title=' '+title,url=link)
    except:
        embed.set_title(title=str(sku),url=link)
    embed.set_title(title=' '+title,url=link)
    embed.set_footer(text='dev by @zyx898',icon_url='https://pbs.twimg.com/profile_images/1118878674642714624/lNXTIWNT_400x400.jpg')
    embed.set_image(image)
    hook.send(embed=embed)
    print('Successfully Posted to Discord ------------ ')


def error_message(message):
    hook = Webhook(error_webhook)
    embed = Embed(description='Nike HK Monitor',color=0x36393F,timestamp='now')
    embed.set_title(title=message)
    embed.set_footer(text='@zyx898',icon_url='https://pbs.twimg.com/profile_images/1118878674642714624/lNXTIWNT_400x400.jpg')
    hook.send(embed=embed)
    print('Successfully Posted to Error Message to  Discord ------------ ')


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
                    error_message('Error at parsing new data')
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
                    error_message('Error at init parse')
                else:
                    old_data.append(item)
    return old_data

def main(start_item):
    old_data = start_item
    while True:
        new_data = parse_html()
        if len(new_data) > 60:
            difference = set(new_data) - set(old_data)
            if difference:
                for i in difference:
                    print(i)
                    message = i.split(' - ')
                    post_discord(message[0],message[1])
                    old_data = new_data
            else:
                print(str(datetime.now())+ ' Monitroing [NIke-HK] ------- ------ ----- ----')
                old_data = new_data
                time.sleep(5)
        else:
            error_message('Error with one site, items list less than 60 ')
#Using this two url
url_list = ['https://www.nike.com.hk/special_editions/list.htm?order=onShelvesTime_desc','https://www.nike.com.hk/man/all/list.htm?order=onShelvesTime_desc']
new_data = []
old_data = []

if __name__ == "__main__":
    start_items = init_parse_html()
    main(start_items)
