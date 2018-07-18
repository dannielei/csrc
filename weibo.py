import requests
import json
from datetime import datetime

class weibo(object):

    def get_weibo(self,page):
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value=3802136340&containerid=1076033802136340&page={}'.format(page)
        response=requests.get(url)
        ob_json=json.loads(response.text)
        list_crads0=ob_json.get('data')
        list_crads=list_crads0.get('cards')
        return list_crads

    def get_products(self,page):
        list_cards=self.get_weibo(page)
        for card in list_cards:
            if card.get('card_type')==9:
                url = card.get('scheme')
                print(url)
                date_str=card.get('mblog').get('created_at')
                print(date_str)
                text = card.get('mblog').get('text')
                print(text)

    def get_products2(self,page):
        list_cards=self.get_weibo(page)
        for card in list_cards:
            if card.get('card_type')==9:
                date_str=card.get('mblog').get('created_at')
                return date_str

    def next_page(self,date_start_str,page):
        try:
            date_str = self.get_products2(page)
            date = datetime.strptime(date_str, "%m-%d")
            date_start = datetime.strptime(date_start_str, "%m-%d")
            if date >= date_start:
                self.get_products(page)
                return True
        except:
            return False

    def main(self,date_start_str):
        self.get_products(1)
        print('click next page: 1')
        for i in range(2, 4):
            check = self.next_page(date_start_str,i)
            if not check:
                break
            print('click next page: {}'.format(i))

if __name__=='__main__':
    weibo=weibo()
    weibo.main('07-01')


# https://m.weibo.cn/api/container/getIndex?type=uid&value=3802136340&containerid=1076033802136340
# type:uid
# value:3802136340
# containerid:1076033802136340
#
# https://m.weibo.cn/api/container/getIndex?type=uid&value=3802136340&containerid=1076033802136340&page=2
# type:uid
# value:3802136340
# containerid:1076033802136340
# page:2