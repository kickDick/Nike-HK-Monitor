import time
from doohks import *
import requests
from datetime import datetime
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    'Referer':'https://www.nike.com.hk/'
    }



def post_discord(sku,link):
    image = 'https://img.nike.com.hk/resources/product/%s/%s_BL1.png'% (sku,sku)
    hook = Webhook('')
    embed = Embed(description='SKU: '+str(sku),color=0x5CDBF0,timestamp='now')
    try:
        title_response = requests.get(link,headers=headers)
        title_html = BeautifulSoup(title_response.text,'lxml')
        title = title_html.title.text
        embed.set_title(title=' '+title,url=link)
    except:
        embed.set_title(title=str(sku),url=link)
    embed.set_title(title=' '+title,url=link)
    embed.set_footer(text='@zyx898',icon_url='https://pbs.twimg.com/profile_images/1118878674642714624/lNXTIWNT_400x400.jpg')
    embed.set_thumbnail(image)
    hook.send(embed=embed)


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
    old_data = ['378040-061 - https://www.nike.com.hk/product/fair/iHgvfECI.htm?pdpRecommend=false&preSkuCode=', 'CI6165-100 - https://www.nike.com.hk/product/CI6165-100/detail.htm?pdpRecommend=false&preSkuCode=', 'CV5574-403 - https://www.nike.com.hk/product/CV5574-403/detail.htm?pdpRecommend=false&preSkuCode=', 'BV5841-800 - https://www.nike.com.hk/product/fair/Xnvzw3Ba.htm?pdpRecommend=false&preSkuCode=', 'CQ6566-700 - https://www.nike.com.hk/product/fair/aqNCHAA6.htm?pdpRecommend=false&preSkuCode=', '378037-061 - https://www.nike.com.hk/product/fair/lCDITj5E.htm?pdpRecommend=false&preSkuCode=', '378038-061 - https://www.nike.com.hk/product/fair/KAJ3BmVk.htm?pdpRecommend=false&preSkuCode=', 'CD8180-400 - https://www.nike.com.hk/product/fair/mN6mzqEd.htm?pdpRecommend=false&preSkuCode=', 'CJ3295-600 - https://www.nike.com.hk/product/fair/MiLbSPyk.htm?pdpRecommend=false&preSkuCode=', 'CT3467-001 - https://www.nike.com.hk/product/fair/59nabgyb.htm?pdpRecommend=false&preSkuCode=', 'CT5050-500 - https://www.nike.com.hk/product/fair/qd6dAE8L.htm?pdpRecommend=false&preSkuCode=', 'AO4568-600 - https://www.nike.com.hk/product/fair/u1KTmwm1.htm?pdpRecommend=false&preSkuCode=', 'CD0383-700 - https://www.nike.com.hk/product/CD0383-700/detail.htm?pdpRecommend=false&preSkuCode=', 'BV1052-001 - https://www.nike.com.hk/product/fair/trkVSo41.htm?pdpRecommend=false&preSkuCode=', 'BQ1896-002 - https://www.nike.com.hk/product/BQ1896-002/detail.htm?pdpRecommend=false&preSkuCode=', 'CK2630-700 - https://www.nike.com.hk/product/fair/uVZiifwU.htm?pdpRecommend=false&preSkuCode=', '130690-014 - https://www.nike.com.hk/product/fair/TemKWP4g.htm?pdpRecommend=false&preSkuCode=', 'BQ3685-706 - https://www.nike.com.hk/product/fair/1DKA5L2o.htm?pdpRecommend=false&preSkuCode=', 'CK1906-400 - https://www.nike.com.hk/product/fair/havUM1zv.htm?pdpRecommend=false&preSkuCode=', 'BQ4737-002 - https://www.nike.com.hk/product/BQ4737-002/detail.htm?pdpRecommend=false&preSkuCode=', 'CI0919-400 - https://www.nike.com.hk/product/CI0919-400/detail.htm?pdpRecommend=false&preSkuCode=', 'BQ4421-100 - https://www.nike.com.hk/product/BQ4421-100/detail.htm?pdpRecommend=false&preSkuCode=', 'CJ9179-200 - https://www.nike.com.hk/product/CJ9179-200/detail.htm?pdpRecommend=false&preSkuCode=', '555088-062 - https://www.nike.com.hk/product/fair/qmUa37t1.htm?pdpRecommend=false&preSkuCode=', '575441-062 - https://www.nike.com.hk/product/fair/05Ef3nla.htm?pdpRecommend=false&preSkuCode=', 'CU7623-002 - https://www.nike.com.hk/product/fair/Ql3Bj3Hx.htm?pdpRecommend=false&preSkuCode=', 'BQ4424-100 - https://www.nike.com.hk/product/BQ4424-100/detail.htm?pdpRecommend=false&preSkuCode=', 'CJ9574-100 - https://www.nike.com.hk/product/fair/0X0wpWwL.htm?pdpRecommend=false&preSkuCode=', 'CD2053-106 - https://www.nike.com.hk/product/CD2053-106/detail.htm?pdpRecommend=false&preSkuCode=', 'BQ3610-100 - https://www.nike.com.hk/product/BQ3610-100/detail.htm?pdpRecommend=false&preSkuCode=', 'BQ3178-600 - https://www.nike.com.hk/product/fair/i5kWrJaM.htm?pdpRecommend=false&preSkuCode=', 'BQ7669-401 - https://www.nike.com.hk/product/BQ7669-401/detail.htm?pdpRecommend=false&preSkuCode=', 'BQ7670-401 - https://www.nike.com.hk/product/BQ7670-401/detail.htm?pdpRecommend=false&preSkuCode=', 'CV3469-001 - https://www.nike.com.hk/product/fair/vYX1FLc0.htm?pdpRecommend=false&preSkuCode=', 'CZ6361-097 - https://www.nike.com.hk/product/fair/V3CbykSA.htm?pdpRecommend=false&preSkuCode=', 'CZ6362-907 - https://www.nike.com.hk/product/fair/9OEYzv86.htm?pdpRecommend=false&preSkuCode=', 'BV4584-400 - https://www.nike.com.hk/product/BV4584-400/detail.htm?pdpRecommend=false&preSkuCode=', 'CQ6569-100 - https://www.nike.com.hk/product/fair/jXwHJmhg.htm?pdpRecommend=false&preSkuCode=', 'CD8178-700 - https://www.nike.com.hk/product/fair/5MsNKzPT.htm?pdpRecommend=false&preSkuCode=', '553558-126 - https://www.nike.com.hk/product/553558-126/detail.htm?pdpRecommend=false&preSkuCode=', '889712-687 - https://www.nike.com.hk/product/889712-687/detail.htm?pdpRecommend=false&preSkuCode=', 'AQ2219-402 - https://www.nike.com.hk/product/AQ2219-402/detail.htm?pdpRecommend=false&preSkuCode=', 'AQ2222-002 - https://www.nike.com.hk/product/AQ2222-002/detail.htm?pdpRecommend=false&preSkuCode=', 'AR5677-403 - https://www.nike.com.hk/product/AR5677-403/detail.htm?pdpRecommend=false&preSkuCode=', 'AT2863-009 - https://www.nike.com.hk/product/AT2863-009/detail.htm?pdpRecommend=false&preSkuCode=', 'AT3493-222 - https://www.nike.com.hk/product/AT3493-222/detail.htm?pdpRecommend=false&preSkuCode=', 'AT3496-222 - https://www.nike.com.hk/product/AT3496-222/detail.htm?pdpRecommend=false&preSkuCode=', 'BA5953-010 - https://www.nike.com.hk/product/BA5953-010/detail.htm?pdpRecommend=false&preSkuCode=', 'BA6447-110 - https://www.nike.com.hk/product/BA6447-110/detail.htm?pdpRecommend=false&preSkuCode=', 'BQ5190-400 - https://www.nike.com.hk/product/BQ5190-400/detail.htm?pdpRecommend=false&preSkuCode=', 'BV0980-010 - https://www.nike.com.hk/product/BV0980-010/detail.htm?pdpRecommend=false&preSkuCode=', 'BV4814-010 - https://www.nike.com.hk/product/BV4814-010/detail.htm?pdpRecommend=false&preSkuCode=', 'BV9289-063 - https://www.nike.com.hk/product/BV9289-063/detail.htm?pdpRecommend=false&preSkuCode=', 'CD0188-004 - https://www.nike.com.hk/product/CD0188-004/detail.htm?pdpRecommend=false&preSkuCode=', 'CD0887-201 - https://www.nike.com.hk/product/CD0887-201/detail.htm?pdpRecommend=false&preSkuCode=', 'CI1991-010 - https://www.nike.com.hk/product/CI1991-010/detail.htm?pdpRecommend=false&preSkuCode=', 'CI3708-001 - https://www.nike.com.hk/product/CI3708-001/detail.htm?pdpRecommend=false&preSkuCode=', 'CK6357-004 - https://www.nike.com.hk/product/CK6357-004/detail.htm?pdpRecommend=false&preSkuCode=', 'CT6140-100 - https://www.nike.com.hk/product/CT6140-100/detail.htm?pdpRecommend=false&preSkuCode=', 'SK0122-011 - https://www.nike.com.hk/product/SK0122-011/detail.htm?pdpRecommend=false&preSkuCode=', 'SK0160-100 - https://www.nike.com.hk/product/SK0160-100/detail.htm?pdpRecommend=false&preSkuCode=', 'BV5841-800 - https://www.nike.com.hk/product/fair/Xnvzw3Ba.htm?pdpRecommend=false&preSkuCode=', 'CQ7960-010 - https://www.nike.com.hk/product/CQ7960-010/detail.htm?pdpRecommend=false&preSkuCode=', '378037-061 - https://www.nike.com.hk/product/fair/lCDITj5E.htm?pdpRecommend=false&preSkuCode=', 'CU1495-010 - https://www.nike.com.hk/product/CU1495-010/detail.htm?pdpRecommend=false&preSkuCode=', 'CT5228-010 - https://www.nike.com.hk/product/CT5228-010/detail.htm?pdpRecommend=false&preSkuCode=', 'CK1540-657 - https://www.nike.com.hk/product/CK1540-657/detail.htm?pdpRecommend=false&preSkuCode=', 'CT3467-001 - https://www.nike.com.hk/product/fair/59nabgyb.htm?pdpRecommend=false&preSkuCode=', 'CT5050-500 - https://www.nike.com.hk/product/fair/qd6dAE8L.htm?pdpRecommend=false&preSkuCode=', 'AO4568-600 - https://www.nike.com.hk/product/fair/u1KTmwm1.htm?pdpRecommend=false&preSkuCode=', 'CD0383-700 - https://www.nike.com.hk/product/CD0383-700/detail.htm?pdpRecommend=false&preSkuCode=', 'AT8086-200 - https://www.nike.com.hk/product/fair/z8dqWqOi.htm?pdpRecommend=false&preSkuCode=', 'BV7406-001 - https://www.nike.com.hk/product/fair/HDED4DKV.htm?pdpRecommend=false&preSkuCode=', 'BV7725-500 - https://www.nike.com.hk/product/BV7725-500/detail.htm?pdpRecommend=false&preSkuCode=', 'BV1052-001 - https://www.nike.com.hk/product/fair/trkVSo41.htm?pdpRecommend=false&preSkuCode=', 'AV0765-400 - https://www.nike.com.hk/product/fair/H4xojRrd.htm?pdpRecommend=false&preSkuCode=', 'BQ2752-001 - https://www.nike.com.hk/product/fair/JQZlNxnd.htm?pdpRecommend=false&preSkuCode=', 'BQ0579-700 - https://www.nike.com.hk/product/fair/8HEBMuPP.htm?pdpRecommend=false&preSkuCode=', 'CD2717-001 - https://www.nike.com.hk/product/fair/foezSJ5t.htm?pdpRecommend=false&preSkuCode=']
    while True:
        new_data = parse_html()
        difference = set(new_data) - set(old_data)
        if difference:
            for i in difference:
                print(difference)
                old_data = new_data
        else:
            print(str(datetime.now())+ ' Monitroing [NIke-HK] ------- ------ ----- ----')
            old_data = new_data
            time.sleep(5)

url_list = ['https://www.nike.com.hk/special_editions/list.htm?order=onShelvesTime_desc','https://www.nike.com.hk/man/all/list.htm?order=onShelvesTime_desc']
new_data = []
old_data = []

if __name__ == "__main__":
    start_items = init_parse_html()
    main(start_items)




