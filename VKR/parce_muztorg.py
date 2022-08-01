import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
import time
import sys

list_res = {'acoustic_links':[],'electro_links':[],'bass_links':[]}
HEADERS = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
        }
async def get_data(page,session,category):
    print(f'Парсим страницу {page}')
    if category == 'a':
        url = f'https://www.muztorg.ru/category/akusticheskie-gitary?in-stock=1&pre-order=1&per-page=96&page={page}'
    if category == 'e':
        url = f'https://www.muztorg.ru/category/elektrogitary?in-stock=1&pre-order=1&page={page}&per-page=96'
    if category == 'b':
        url = f'https://www.muztorg.ru/category/bas-gitary?in-stock=1&pre-order=1&page={page}&per-page=96'

    async with session.get(url=url,headers = HEADERS) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text,'lxml')
        items = soup.find_all('section',class_ = 'product-thumbnail')
        for item in items:
            name = item.find('div',class_ = 'product-header').find('div',class_ = 'title').find('a').text
            link = 'https://www.muztorg.ru'+ item.find('div',class_ = 'product-header').find('div',class_ = 'title').find('a')['href']
            print(f'Имя {name} Cсылка {link}')
            app_dict = {
                'name': name,
                'link': link
            }
            if category == 'a':
                list_res['acoustic_links'].append(app_dict)
            if category == 'e':
                list_res['electro_links'].append(app_dict)
            if category == 'b':
                list_res['bass_links'].append(app_dict)
            print(f'Название {name} Ссылка {link}')

async def gather():
    url1 = 'https://www.muztorg.ru/category/akusticheskie-gitary?in-stock=1&pre-order=1&per-page=96&page=1'
    url2 = 'https://www.muztorg.ru/category/elektrogitary'
    url3 = 'https://www.muztorg.ru/category/bas-gitary'
    async with aiohttp.ClientSession() as session:
        for cat in ('a','e','b'):
            if cat == 'a':
                url = url1
            if cat == 'e':
                url = url2
            if cat == 'b':
                url = url3
            response = await session.get(url=url,headers=HEADERS)
            soup = BeautifulSoup(await response.text(),'lxml')
            tasks = []
            max_pages = int(soup.find('ul',class_ = 'pagination').find_all('li')[-2].find('a').text)
            print(f'Страниц {max_pages}')
            for page in range(1,max_pages+1):
                task = asyncio.create_task(get_data(page,session,cat))
                tasks.append(task)
            await asyncio.gather(*tasks)
        print(f'Результат {list_res}')
        with open('res_muztorg.json','w') as j:
            json.dump(list_res,j,indent=4)


if __name__ == '__main__':
    asyncio.run(gather())