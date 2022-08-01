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
    global list_res
    print(f'Парсим страницу {page}')
    if category == 'a':
        url = f'https://skifmusic.ru/catalog/akusticheskie-gitaryi-13/page{page}'
    if category == 'b':
        url = f'https://skifmusic.ru/catalog/bas-gitaryi-14/page{page}'
    if category == 'e':
        url = f'https://skifmusic.ru/catalog/elektrogitaryi-12/page{page}'

    async with session.get(url=url,headers=HEADERS) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text,'lxml')
        items = soup.find_all('div',class_ = 'product-box')
        #
        for item in items:
            name_fin = []
            name = item.find('div',class_ = 'product-box__name').find('a').text
            for i in name.split(' '):
                if i not in ('Электроакустическая','гитара','Трансакустическая','Акустическая','Резонаторная','Гитара','шестиструнная','бас-гитара','фолк','сайлент-гитара','трэвел-гитара',',','','гиатра','электроакустическая','12-струнная','в', 'комплекте', 'с', 'аксессуарами','Бас-гитара','7-струнная','Электро-акустическая','-','Электрогитара',''):
                    name_fin.append(i)
            name_fin = ' '.join(name_fin)

            link = 'https://skifmusic.ru'+(item.find('div',class_ = 'product-box__name').find('a')['href'])
            app_dict = {
                'name':name_fin.upper(),
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
    url1 = 'https://skifmusic.ru/catalog/akusticheskie-gitaryi-13'
    url2 = 'https://skifmusic.ru/catalog/elektrogitaryi-12'
    url3 = 'https://skifmusic.ru/catalog/bas-gitaryi-14'
    async with aiohttp.ClientSession() as session:
        for cat in ('a','e','b'):
            if cat == 'a':
                url = url1
            if cat == 'e':
                url = url2
            if cat == 'b':
                url = url3
            response = await session.get(url=url)
            soup = BeautifulSoup(await response.text(),'lxml')
            tasks = []
            pages_c = int((soup.find('li', class_='last').find('a')['href']).split('/')[-1].split('page')[-1])
            for page in range(1,pages_c+1):
                task = asyncio.create_task(get_data(page,session,cat))
                tasks.append(task)
            await asyncio.gather(*tasks)
        print('Res')
        print(list_res)
        with open ('res_skif.json','w') as j:
            json.dump(list_res,j,indent=4,ensure_ascii=True)
        print('Сбор произведён')
        time.sleep(5)
        sys.exit()





if __name__ == '__main__':
    asyncio.run(gather())
# def get_data(page,session):
#     r = requests.get(url='https://skifmusic.ru/catalog/akusticheskie-gitaryi-13')
#
#     soup = BeautifulSoup(r.text,'lxml')
#
#     pages_c = (soup.find('li',class_ = 'last').find('a')['href']).split('/')[-1].split('page')[-1]
#
#     print(pages_c)
#

#
# def gather():
#
#         res =  requests.get(url='https://skifmusic.ru/catalog/akusticheskie-gitaryi-13')
#
#         soup = BeautifulSoup(res.text, 'lxml')
#
#         pages_c = int((soup.find('li', class_='last').find('a')['href']).split('/')[-1].split('page')[-1])
#
#         for page in range(1,pages_c+1):
#             task = asyncio.create_task(get_data(page,sez))
# if __name__ == '__main__':
#     gather()
