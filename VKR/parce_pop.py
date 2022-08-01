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
        url = f'https://pop-music.ru/catalog/gitaryi/gitaryi-akusticheskie/?PAGEN_2={page}'
    if category == 'e':
        url = f'https://pop-music.ru/catalog/gitaryi/elektrogitaryi/?PAGEN_2={page}'
    if category == 'b':
        url = f'https://pop-music.ru/catalog/gitaryi/bas-gitaryi/?PAGEN_2={page}'

    async with session.get(url=url,headers = HEADERS) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text,'lxml')
        items = soup.find('div',class_ = 'products-grid js_ajax_data').find_all('div',class_ = 'products-grid__i')
        for item in items:
            name_finl = []
            name = item.find('div',class_ = 'product-card').find('a',class_ = 'product-card__name').text
            name= name.upper()
            for i in name.split(' '):
                if i not in ('АКУСТИЧЕСКАЯ','ГИТАРА','БАС-ГИТАРА','ЭЛЕКТРОГИТАРА','ТРЕВЕЛ','СИГАРБОКС','ЛЕВОРУКАЯ'):
                    name_finl.append(i)
            name_fin= ' '.join(name_finl)
            link = 'https://pop-music.ru'+ item.find('div',class_ = 'product-card').find('a',class_ = 'product-card__name')['href']
            print(f'Имя {name_fin} Cсылка  {link}')

            app_dict = {
                'name': name_fin,
                'link': link
            }
            if category == 'a':
                list_res['acoustic_links'].append(app_dict)
            if category == 'e':
                list_res['electro_links'].append(app_dict)
            if category == 'b':
                list_res['bass_links'].append(app_dict)
            # print(f'Название {name} Ссылка {link}')

async def gather():
    url1 = 'https://pop-music.ru/catalog/gitaryi/gitaryi-akusticheskie/'
    url2 = 'https://pop-music.ru/catalog/gitaryi/elektrogitaryi/'
    url3 = 'https://pop-music.ru/catalog/gitaryi/bas-gitaryi/'
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
            max_pages = int(soup.find('div',class_ = 'pagination__pages').find_all('a',class_ = 'pagination__page')[-1].text.strip())
            print(f'Страниц {max_pages}')
            for page in range(1,max_pages+1):
                task = asyncio.create_task(get_data(page,session,cat))
                tasks.append(task)
        await asyncio.gather(*tasks)
        print(f'Результат {list_res}')
        with open('res_pop.json','w') as j:
            json.dump(list_res,j,indent=4)


if __name__ == '__main__':
    asyncio.run(gather())