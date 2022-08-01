import sys
import platform
import webbrowser
import pyperclip
import json
import threading
import requests
import socket
import random
import time
import datetime
import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from bs4 import BeautifulSoup


# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMaximumSize(1500,1000)
        self.settings()
        self.setWindowIcon(QtGui.QIcon('pictures/icon.jpg'))
        self.setWindowTitle('API-интерфейс для сбора данных')
        self.ui.Pages_Widget.setCurrentWidget(self.ui.page_start)
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_toggle.clicked.connect(lambda : UIFunction.toggleMenu(self,250,True))
        ## PAGES
        ########################################################################
        self.ui.Btn_Menu_2.clicked.connect(self.acoustic)
        self.ui.Btn_Menu_1.clicked.connect(self.electro)
        self.ui.Btn_Menu_3.clicked.connect(self.bass)
        self.ui.button_author.clicked.connect(lambda : self.ui.Pages_Widget.setCurrentWidget(self.ui.page_author))
        self.ui.but_instr.clicked.connect(lambda : self.ui.Pages_Widget.setCurrentWidget(self.ui.page_instruction))
        ##ССЫЛКИ
        #############
        self.ui.vk_but.clicked.connect(lambda: webbrowser.open("https://vk.com/saint_karas",new=1))
        self.ui.telega_but.clicked.connect(lambda : webbrowser.open('https://t.me/Pokulord',new=1))
        self.ui.but_mail.clicked.connect(self.mail)
        self.ui.checkBox_muz.clicked.connect(lambda : self.change_settings('MuzTorg'))
        self.ui.checkBox_skif.clicked.connect(lambda: self.change_settings('SkifMusic'))
        self.ui.checkBox_pop.clicked.connect(lambda: self.change_settings('PopMusic'))




        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    def open_json(self):
        global data, links_skif,links_muztorg,links_pop
        with open('guitars.json', 'r') as j:
            data = json.load(j)
            print(data)
        with open('res_skif.json','r') as ls:
            links_skif = json.load(ls)
        with open('res_muztorg.json','r') as lm:
            links_muztorg = json.load(lm)
        with open('res_pop.json','r') as lp:
            links_pop = json.load(lp)
    def change_settings(self,to_change):
        print(f"Аргумент {to_change}")
        if settings[to_change] == 'True':
            settings[to_change] = 'False'
        elif settings[to_change] == 'False':
            settings[to_change] = 'True'
        print(f"Новые настройки {settings}")

        with open ('parce_settings.json','w') as js:
            json.dump(settings,js,indent=4)
            js.close()
        self.settings()



    def settings(self):
        global settings,magazines
        magazines = []
        with open('parce_settings.json', 'r') as j:
            settings = json.load(j)
            print(f"Настройки парсинга : {settings}")
        if settings['MuzTorg'] == 'True':
            self.ui.checkBox_muz.setChecked(True)
            magazines.append('MuzTorg')
        if settings['SkifMusic'] == 'True':
            self.ui.checkBox_skif.setChecked(True)
            magazines.append('SkifMusic')
        if settings['PopMusic'] == 'True':
            self.ui.checkBox_pop.setChecked(True)
            magazines.append('PopMusic')

    #Проверяем интернет-соединение
    def check_internet(self):
        try:
            socket.create_connection(("www.google.com", 80))
            print('Success')
            return True
        except:
            print('error')
            return False
    def rewrite_JSON(self):
        with open('guitars.json', 'w') as j_add:
            json.dump(data, j_add, indent=4)
    def choose_img(self):
        global img_path
        img_path = QFileDialog\
        .getOpenFileName(self,"Открыть файл","guitars/","JPG File(*.jpg);;PNG File(*.png)")
        if img_path[0] != '':
            img_path = img_path[0].split("/")[-2] + "/" + img_path[0].split("/")[-1]
            print(f'Путь {img_path}')
            self.ui.check_img.setEnabled(True)
            self.ui.check_img.setChecked(True)
            self.ui.check_img.setEnabled(False)
        else:
            img_path = ''
            return
    def remove_guitar(self,arg=None):
        if flag == 'a':
            spis_g = [i['name'] for i in data['acoustic']['guitars']]
            print(spis_g)
            print(f'Индекс {spis_g.index(arg)}')
            del (data['acoustic']['guitars'])[spis_g.index(arg)]
            print(data)
            # self.acoustic()
            for i in reversed(range(self.ui.gridLayout_2.count())):
                self.ui.gridLayout_2.itemAt(i).widget().setParent(None)
            self.acoustic()
            self.rewrite_JSON()
        if flag == 'e':
            spis_g = [i['name'] for i in data['electric']['guitars']]
            print(spis_g)
            print(f'Индекс {spis_g.index(arg)}')
            del (data['electric']['guitars'])[spis_g.index(arg)]
            print(data)
            # self.acoustic()
            for i in reversed(range(self.ui.gridLayout_3.count())):
                self.ui.gridLayout_3.itemAt(i).widget().setParent(None)
            self.electro()
            self.rewrite_JSON()
        if flag == 'b':
            spis_g = [i['name'] for i in data['bass']['guitars']]
            print(spis_g)
            print(f'Индекс {spis_g.index(arg)}')
            del (data['bass']['guitars'])[spis_g.index(arg)]
            print(data)
            # self.acoustic()
            for i in reversed(range(self.ui.gridLayout_4.count())):
                self.ui.gridLayout_4.itemAt(i).widget().setParent(None)
            self.bass()
            self.rewrite_JSON()
    def is_valid_url(self,url):
        import re
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url is not None and regex.search(url)

    def add_guitar(self):
        #Проверка вводимых значений
        a_check = [i['name'] for i in data['acoustic']['guitars']]
        e_check = [i['name'] for i in data['electric']['guitars']]
        b_check = [i['name'] for i in data['bass']['guitars']]
        # img_path = '123'
        if (self.ui.comboBox_name.currentText()).strip() != '' and (self.ui.skif_add.text()).strip() != '' and (self.ui.pop_add.text()).strip() != '':
            if img_path != '':
                muztorg_link_add = self.ui.muztorg_add.text()
                skif_link_add = self.ui.skif_add.text()
                pop_link_add = self.ui.pop_add.text()
                print(f'Аргумент {muztorg_link_add}')

                if flag == 'a':
                    if self.ui.comboBox_name.currentText() not in a_check:
                        dict_add = {
                            'name': self.ui.comboBox_name.currentText(),
                            'link_muztorg': muztorg_link_add,
                            'link_skif': skif_link_add,
                            'link_popmusic': pop_link_add,
                            'image': img_path
                        }
                        data['acoustic']['guitars'].append(dict_add)
                        print(f'На экспорт {data}')
                        with open('guitars.json','w') as j_add:
                            json.dump(data,j_add,indent=4)
                        QtWidgets.QMessageBox.information(self, 'Внимание', 'Товар успешно добавлен')

                    else:
                        QtWidgets.QMessageBox.warning(self, 'Внимание', 'Данный товар уже есть в списке!')
                        return

                if flag == 'e':
                    print("Добавляю электро")
                    if self.ui.comboBox_name.currentText() not in e_check:
                        dict_add = {
                            'name': self.ui.comboBox_name.currentText(),
                            'link_muztorg': muztorg_link_add,
                            'link_skif': skif_link_add,
                            'link_popmusic': pop_link_add,
                            'image': img_path
                        }
                        data['electric']['guitars'].append(dict_add)
                        print(f'На экспорт {data}')
                        with open('guitars.json', 'w') as j_add:
                            json.dump(data, j_add, indent=4)
                        QtWidgets.QMessageBox.information(self, 'Внимание', 'Товар успешно добавлен')

                    else:
                        QtWidgets.QMessageBox.warning(self, 'Внимание', 'Данный товар уже есть в списке!')
                        return

                if flag == 'b':
                    print("Добавляю бас")
                    if self.ui.comboBox_name.currentText() not in b_check:
                        dict_add = {
                            'name': self.ui.comboBox_name.currentText(),
                            'link_muztorg': muztorg_link_add,
                            'link_skif': skif_link_add,
                            'link_popmusic': pop_link_add,
                            'image': img_path
                        }
                        data['bass']['guitars'].append(dict_add)
                        print(f'На экспорт {data}')
                        with open('guitars.json', 'w') as j_add:
                            json.dump(data, j_add, indent=4)
                        QtWidgets.QMessageBox.information(self, 'Внимание', 'Товар успешно добавлен')

                    else:
                        QtWidgets.QMessageBox.warning(self, 'Внимание', 'Данный товар уже есть в списке!')
                        return

            else:
                QtWidgets.QMessageBox.warning(self, 'Внимание', 'Выберите изображение')
                return
        else:
            QtWidgets.QMessageBox.warning(self,'Внимание','Заполните все поля формы!')
            return


    def find(self):
        link_skif = 'empty'
        link_muz = 'empty'
        link_pop = 'empty'
        name_f = self.ui.comboBox_name.currentText().strip()
        if name_f == '':
            QtWidgets.QMessageBox.warning(self, 'Внимание', 'Введите название товара')
            return
        self.ui.muztorg_add.setEnabled(True)
        self.ui.skif_add.setEnabled(True)
        self.ui.pop_add.setEnabled(True)
        self.ui.muztorg_add.setText('')
        self.ui.skif_add.setText('')
        self.ui.pop_add.setText('')

        print(f'Флаг {flag}')

        if flag == 'a':

            for item in links_skif['acoustic_links']:
                if item['name'] == name_f: link_skif = item['link']
            for item in links_muztorg['acoustic_links']:
                if item['name'] == name_f: link_muz = item['link']
            for item in links_pop['acoustic_links']:
                if item['name'] == name_f: link_pop = item['link']
            self.ui.skif_add.setText(link_skif)
            self.ui.muztorg_add.setText(link_muz)
            self.ui.pop_add.setText(link_pop)

        if flag == 'e':

            for item in links_skif['electro_links']:
                if item['name'] == name_f: link_skif = item['link']
            for item in links_muztorg['electro_links']:
                if item['name'] == name_f: link_muz = item['link']
            for item in links_pop['electro_links']:
                if item['name'] == name_f: link_pop = item['link']
            self.ui.skif_add.setText(link_skif)
            self.ui.muztorg_add.setText(link_muz)
            self.ui.pop_add.setText(link_pop)

        if flag == 'b':

            for item in links_skif['bass_links']:
                if item['name'] == name_f: link_skif = item['link']
            for item in links_muztorg['bass_links']:
                if item['name'] == name_f: link_muz = item['link']
            for item in links_pop['bass_links']:
                if item['name'] == name_f: link_pop = item['link']
            self.ui.skif_add.setText(link_skif)
            self.ui.muztorg_add.setText(link_muz)
            self.ui.pop_add.setText(link_pop)



    def add_guitar_page(self):
        global for_combobox
        if flag == 'a':
            for_combobox = [i['name'] for i in links_skif['acoustic_links']]+[i['name'] for i in links_muztorg['acoustic_links']] + [i['name'] for i in links_pop['acoustic_links']]
            for_combobox = set(for_combobox)
            for_combobox = list(for_combobox)
            for_combobox.sort()
        if flag == 'e':
            for_combobox = [i['name'] for i in links_skif['electro_links']] + [i['name'] for i in
                                                                                links_muztorg['electro_links']] + [
                               i['name'] for i in links_pop['electro_links']]
            for_combobox = set(for_combobox)
            for_combobox = list(for_combobox)
            for_combobox.sort()
        if flag == 'b':
            for_combobox = [i['name'] for i in links_skif['bass_links']] + [i['name'] for i in
                                                                               links_muztorg['bass_links']] + [
                               i['name'] for i in links_pop['bass_links']]
            for_combobox = set(for_combobox)
            for_combobox = list(for_combobox)
            for_combobox.sort()
            print(for_combobox)
        self.ui.comboBox_name.clear()
        global img_path
        self.ui.comboBox_name.addItems(for_combobox)
        img_path = ''
        self.ui.check_img.setEnabled(False)
        self.ui.Pages_Widget.setCurrentWidget(self.ui.page_add)
        self.ui.back_but_2.clicked.connect(self.back)
        self.ui.but_add_g.clicked.connect(self.add_guitar)
        self.ui.but_img.clicked.connect(self.choose_img)
        self.ui.but_find.clicked.connect(self.find)
        self.ui.muztorg_add.setEnabled(False)
        self.ui.skif_add.setEnabled(False)
        self.ui.pop_add.setEnabled(False)
        self.ui.frame_left_menu.hide()
        self.ui.frame_toggle.hide()
        self.ui.pop_add.setText('')
        self.ui.muztorg_add.setText('')
        self.ui.skif_add.setText('')
        self.ui.check_img.setChecked(False)


    def test(self,arg,flag):
        global for_parce,magazines,name_export
        global time_start
        time_start = time.time()
        for_table = []
        links = []
        name_export = arg
        QtWidgets.QMessageBox.information(self,'Информация',f'Процесс сбора данных запущен. Пожалуйста, подождите ~ {random.randint(7,9)} секунд.')
        # self.ui.Pages_Widget.setCurrentWidget(self.ui.page_loading)
        # movie = QtGui.QMovie('pictures/loading.gif')
        # self.ui.loading_bar.setMovie(movie)
        # self.ui.loading_bar.setScaledContents(True)
        # movie.start()
        print(arg)
        #Переход на ту или иную процедуру отбора в зависимости от флага
        if flag == 'a':
            #Отбор ссылок по выбранному имени(атрибуту)
            for_parce = [[i['link_muztorg'],i['link_skif'],i['link_popmusic']] for i in data['acoustic']['guitars'] if i['name'] == arg]
            img = [[i['image']] for i in data['acoustic']['guitars'] if i['name'] == arg]
            print(for_parce[0])
            if 'MuzTorg' in magazines:
                price_muz,rating_muz = self.parse_muztorg(for_parce[0][0])
                print(f"Музторг : Цена {price_muz}, Рейтинг {rating_muz}")
                for_table.extend((price_muz,rating_muz))
                links.append(for_parce[0][0])
            if 'SkifMusic' in magazines:
                price_skif, rating_skif = self.parce_skif(for_parce[0][1])
                print(f"Скиф: Цена {price_skif}, Рейтинг {rating_skif}")
                for_table.extend((price_skif, rating_skif))
                links.append(for_parce[0][1])
            if 'PopMusic' in magazines:
                price_pop, rating_pop = self.parce_pop(for_parce[0][2])
                print(f'Поп: Цена {price_pop}, Рейтинг {rating_pop} ')
                for_table.extend((price_pop,rating_pop))
                links.append(for_parce[0][2])
            self.table_parce(arg,for_table,flag,links,img[0][0])

        if flag == 'e':
            for_parce = [[i['link_muztorg'],i['link_skif'],i['link_popmusic']] for i in data['electric']['guitars'] if i['name'] == arg]
            img = [[i['image']] for i in data['electric']['guitars'] if i['name'] == arg]
            print(for_parce)
            if 'MuzTorg' in magazines:
                price_muz,rating_muz = self.parse_muztorg(for_parce[0][0])
                print(f"Музторг : Цена {price_muz}, Рейтинг {rating_muz}")
                for_table.extend((price_muz,rating_muz))
                links.append(for_parce[0][0])
            if 'SkifMusic' in magazines:
                price_skif, rating_skif = self.parce_skif(for_parce[0][1])
                print(f"Скиф: Цена {price_skif}, Рейтинг {rating_skif}")
                for_table.extend((price_skif, rating_skif))
                links.append(for_parce[0][1])
            if 'PopMusic' in magazines:
                price_pop, rating_pop = self.parce_pop(for_parce[0][2])
                print(f'Поп: Цена {price_pop}, Рейтинг {rating_pop} ')
                for_table.extend((price_pop,rating_pop))
                links.append(for_parce[0][2])
            self.table_parce(arg,for_table,flag,links,img[0][0])
        if flag == 'b':
            for_parce = [[i['link_muztorg'], i['link_skif'], i['link_popmusic']] for i in data['bass']['guitars'] if
                         i['name'] == arg]
            img = [[i['image']] for i in data['bass']['guitars'] if i['name'] == arg]
            print(for_parce)
            if 'MuzTorg' in magazines:
                price_muz, rating_muz = self.parse_muztorg(for_parce[0][0])
                print(f"Музторг : Цена {price_muz}, Рейтинг {rating_muz}")
                for_table.extend((price_muz, rating_muz))
                links.append(for_parce[0][0])
            if 'SkifMusic' in magazines:
                price_skif, rating_skif = self.parce_skif(for_parce[0][1])
                print(f"Скиф: Цена {price_skif}, Рейтинг {rating_skif}")
                for_table.extend((price_skif, rating_skif))
                links.append(for_parce[0][1])
            if 'PopMusic' in magazines:
                price_pop, rating_pop = self.parce_pop(for_parce[0][2])
                print(f'Поп: Цена {price_pop}, Рейтинг {rating_pop} ')
                for_table.extend((price_pop, rating_pop))
                links.append(for_parce[0][2])
            self.table_parce(arg, for_table, flag, links, img[0][0])

    #Функция, что парсит "Музторг"
    def parse_muztorg(self,link=None):
        if link == '' or link == 'empty':
            print('Ссылка отсутствует')
            return 'empty','empty'
        HEADERS = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
        }
        r = requests.get(link,headers=HEADERS)
        src = r.text
        soup = BeautifulSoup(src,'lxml')
        price_muz = soup.find('meta',{'itemprop':'price'})['content']
        try:
            nal = (soup.find('div',class_ = 'product-info__available _pre-order help').text.strip()).split(' ')
            nal = nal[0]+' '+nal[1]+' '+nal[2]
            if nal == 'Нет в наличии':
                return 'Нет в наличии','Нет в наличии'

        except:
            pass
        try:
            rating_muz= soup.find('svg',class_='rating__star')['data-rating']
        except:
            rating_muz = 'Empty'
        return price_muz, rating_muz

    #Парсим Скиф
    def parce_skif(self,link=None):
        if link == '' or link == 'empty':
            print('Ссылка отсутствует')
            return 'empty','empty'
        r = requests.get(link)
        source = r.text
        soup = BeautifulSoup(source,'lxml')
        try:
            check = soup.find('div',class_ = 'red').text.strip()
            if check == 'Товар закончился':
                return 'Нет в наличии','Нет в наличии'
        except:
            pass
        price_skif = (soup.find('span',class_ = 'bigger-170 text-bold').text).replace("\xa0",'')
        rating = soup.find_all('i',class_ = 'fas fa-star yellow')
        if len(rating) == 10:
            rating = len(rating)//2
        else:
            rating = len(rating)
        return price_skif, rating

    #Парсим PopMusic
    def parce_pop(self,link = None):
        if link == '' or link == 'empty':
            print('Ссылка отсутствует')
            return 'empty','empty'
        r = requests.get(link)
        src = r.text
        soup = BeautifulSoup(src,'lxml')
        price = ((soup.find('div',class_ = 'productfull__newprice').text).replace(' ','')).replace('₽','')
        rating = soup.find('div',class_ = 'rate _medium').findAll('i',class_ = 'rate__star is-full')
        return price, len(rating)

    def table_parce(self,name=None,spis=None,flag = None,links=None,img=None):
        global spis_export
        spis_export = spis
        print(f'Ссылки {links}')
        print(spis)
        oldsort = self.ui.tableWidget.horizontalHeader().sortIndicatorSection()
        oldorder = self.ui.tableWidget.horizontalHeader().sortIndicatorOrder()
        self.ui.tableWidget.setSortingEnabled(False)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(magazines))
        ch_row = 0
        for i in magazines:
            self.ui.tableWidget.setItem(ch_row,0,QtWidgets.QTableWidgetItem(str(i)))
            ch_row += 1
        ch_row=0
        ch_col=1
        for i in spis:
            if ch_col == 3:
                ch_col = 1
                ch_row +=1
            self.ui.tableWidget.setItem(ch_row,ch_col,QtWidgets.QTableWidgetItem(str(i)))
            ch_col +=1
        self.ui.Pages_Widget.setCurrentWidget(self.ui.page_table_parce)
        self.ui.label_guitar.setPixmap(img)
        #Выводим кпопки-ссылки
        ch_row = 0
        for i in links:
            but = QPushButton()
            but.setText('Перейти')
            but.clicked.connect(lambda checked=None , x = i: webbrowser.open(x,new=1))
            if i != '' and i !='empty':
                self.ui.tableWidget.setCellWidget(ch_row,3,but)
            ch_row +=1

        time_fin = time.time()

        print(f"Время,затраченное на выполнение программы {round(time_fin - time_start,2)} cек")
        self.ui.label_7.setText(f'Результаты парсинга товара {name}')
        self.ui.tableWidget.sortItems(oldsort,oldorder)
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.back_but.clicked.connect(self.back)
        self.ui.but_export.clicked.connect(self.export_JSON)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def back(self):
        try:
            self.ui.but_find.clicked.disconnect()
            self.ui.but_add_g.clicked.disconnect()
            self.ui.but_img.clicked.disconnect()
            self.ui.frame_toggle.show()
            self.ui.frame_left_menu.show()
        except:
            pass

        if flag == 'a':
            self.acoustic()
        if flag == 'e':
            self.electro()
        if flag == 'b':
            self.bass()

    #Функция выбора страницы с акустическими гитарами
    def acoustic(self):
        global flag
        check = self.check_internet()
        if check:
            flag = 'a'
            ch_str=0
            ch_col=0
            self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1)
            for i in data['acoustic']['guitars']:
                if ch_col == 3:
                    ch_col=0
                    ch_str+=1
                self.guitar_1 = QFrame(self.ui.gridLayoutWidget)
                self.guitar_1.setObjectName(u"guitar_1")
                self.guitar_1.setMinimumSize(QSize(200, 400))
                self.ui.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
                self.guitar_1.setMaximumSize(QSize(200, 400))
                self.guitar_1.setStyleSheet(u"background-color: rgb(35, 35, 35);")
                self.guitar_1.setFrameShape(QFrame.StyledPanel)
                self.guitar_1.setFrameShadow(QFrame.Raised)
                self.verticalLayout_14 = QVBoxLayout(self.guitar_1)
                self.verticalLayout_14.setSpacing(0)
                self.verticalLayout_14.setObjectName(u"verticalLayout_14")
                self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
                self.frame_img = QFrame(self.guitar_1)
                self.frame_img.setObjectName(u"frame_img")
                self.frame_img.setMinimumSize(QSize(0, 150))
                self.frame_img.setFrameShape(QFrame.StyledPanel)
                self.frame_img.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_5 = QHBoxLayout(self.frame_img)
                self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
                self.label_7 = QLabel(self.frame_img)
                self.label_7.setObjectName(u"label_7")
                self.label_7.setPixmap(QPixmap(f"{i['image']}"))
                self.label_7.setScaledContents(True)

                self.horizontalLayout_5.addWidget(self.label_7)

                self.verticalLayout_14.addWidget(self.frame_img)

                self.frame_ch = QFrame(self.guitar_1)
                self.frame_ch.setObjectName(u"frame_ch")
                self.frame_ch.setFrameShape(QFrame.StyledPanel)
                self.frame_ch.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_4 = QHBoxLayout(self.frame_ch)
                self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
                self.label_9 = QLabel(self.frame_ch)
                self.label_9.setObjectName(u"label_9")
                self.label_9.setStyleSheet(u"color:white")
                self.label_9.setText(f"{i['name']}")
                self.label_9.setWordWrap(True)

                self.horizontalLayout_4.addWidget(self.label_9)

                self.pushButton_2 = QPushButton(self.frame_ch)
                self.pushButton_2.setObjectName(u"pushButton_2")
                self.pushButton_2.setStyleSheet('background-color:#AFAFAF;')

                self.horizontalLayout_4.addWidget(self.pushButton_2)
                self.pushButton_d = QPushButton(self.frame_ch)
                self.pushButton_d.setObjectName(u"pushButton_d")
                self.pushButton_d.setStyleSheet('background-color:#AFAFAF;')
                self.pushButton_d.setIcon(QIcon('pictures/trash.png'))
                self.pushButton_d.clicked.connect(lambda checked=None, g = i['name']: self.remove_guitar(g))
                self.horizontalLayout_4.addWidget(self.pushButton_d)
                self.verticalLayout_14.addWidget(self.frame_ch)

                self.ui.gridLayout_2.addWidget(self.guitar_1, ch_str, ch_col, 1, 1)
                print('i',i)
                self.pushButton_2.clicked.connect(lambda checked=None, x=i['name']: self.test(x,flag))
                self.pushButton_2.setText('Выбор')
                ch_col+=1
            # Кнопка "Добавить"
            self.but_add = QPushButton(self.frame_ch)
            self.but_add.setObjectName(u"but_add")
            self.but_add.setStyleSheet(u"QPushButton {\n"
            "color:white;\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(61, 145, 255);\n"
            "}")
            if ch_col == 3:
                ch_col = 0
                ch_str += 1
            self.ui.gridLayout_2.addWidget(self.but_add,ch_str,ch_col,1,1)
            self.but_add.setText('Добавить')
            self.but_add.clicked.connect(self.add_guitar_page)
        else:
            QtWidgets.QMessageBox.information(self,"Внимание","Проверьте подключение к интернету")

    def electro(self):
        global flag
        check = self.check_internet()
        if check:
            flag = 'e'
            ch_str = 0
            ch_col = 0
            self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2)
            for i in data['electric']['guitars']:
                if ch_col == 3:
                    ch_col = 0
                    ch_str += 1
                self.guitar_1 = QFrame(self.ui.gridLayoutWidget)
                self.guitar_1.setObjectName(u"guitar_1")
                self.guitar_1.setMinimumSize(QSize(200, 400))
                self.ui.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
                self.guitar_1.setMaximumSize(QSize(200, 900000))
                self.guitar_1.setStyleSheet(u"background-color: rgb(35, 35, 35);")
                self.guitar_1.setFrameShape(QFrame.StyledPanel)
                self.guitar_1.setFrameShadow(QFrame.Raised)
                self.verticalLayout_14 = QVBoxLayout(self.guitar_1)
                self.verticalLayout_14.setSpacing(0)
                self.verticalLayout_14.setObjectName(u"verticalLayout_14")
                self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
                self.frame_img = QFrame(self.guitar_1)
                self.frame_img.setObjectName(u"frame_img")
                self.frame_img.setMinimumSize(QSize(0, 150))
                self.frame_img.setFrameShape(QFrame.StyledPanel)
                self.frame_img.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_5 = QHBoxLayout(self.frame_img)
                self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
                self.label_7 = QLabel(self.frame_img)
                self.label_7.setObjectName(u"label_7")
                self.label_7.setPixmap(QPixmap(f"{i['image']}"))
                self.label_7.setScaledContents(True)

                self.horizontalLayout_5.addWidget(self.label_7)

                self.verticalLayout_14.addWidget(self.frame_img)

                self.frame_ch = QFrame(self.guitar_1)
                self.frame_ch.setObjectName(u"frame_ch")
                self.frame_ch.setFrameShape(QFrame.StyledPanel)
                self.frame_ch.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_4 = QHBoxLayout(self.frame_ch)
                self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
                self.label_9 = QLabel(self.frame_ch)
                self.label_9.setObjectName(u"label_9")
                self.label_9.setStyleSheet(u"color:white")
                self.label_9.setText(f"{i['name']}")
                self.label_9.setWordWrap(True)

                self.horizontalLayout_4.addWidget(self.label_9)

                self.pushButton_2 = QPushButton(self.frame_ch)
                self.pushButton_2.setObjectName(u"pushButton_2")
                self.pushButton_2.setStyleSheet('background-color:#AFAFAF;')

                self.horizontalLayout_4.addWidget(self.pushButton_2)
                self.pushButton_d = QPushButton(self.frame_ch)
                self.pushButton_d.setObjectName(u"pushButton_d")
                self.pushButton_d.setStyleSheet('background-color:#AFAFAF;')
                self.pushButton_d.setIcon(QIcon('pictures/trash.png'))
                self.pushButton_d.clicked.connect(lambda checked=None, g=i['name']: self.remove_guitar(g))
                self.horizontalLayout_4.addWidget(self.pushButton_d)
                self.verticalLayout_14.addWidget(self.frame_ch)

                self.ui.gridLayout_3.addWidget(self.guitar_1, ch_str, ch_col, 1, 1)
                print('i', i)
                self.pushButton_2.clicked.connect(lambda checked=None, x=i['name']: self.test(x,flag))
                self.pushButton_2.setText('Выбор')
                ch_col += 1
                # Кнопка "Добавить"
                self.but_add = QPushButton(self.frame_ch)
                self.but_add.setObjectName(u"but_add")
                self.but_add.setStyleSheet(u"QPushButton {\n"
                                           "color:white;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "	background-color: rgb(61, 145, 255);\n"
                                           "}")
                if ch_col == 3:
                    ch_col = 0
                    ch_str += 1
                self.ui.gridLayout_3.addWidget(self.but_add, ch_str, ch_col, 1, 1)
                self.but_add.setText('Добавить')
                self.but_add.clicked.connect(self.add_guitar_page)
        else:
            QtWidgets.QMessageBox.information(self, "Внимание", "Проверьте подключение к интернету")

    def bass(self):
        global flag
        check = self.check_internet()
        if check:
            flag = 'b'
            ch_str = 0
            ch_col = 0
            self.ui.Pages_Widget.setCurrentWidget(self.ui.page_bass)
            for i in data['bass']['guitars']:
                if ch_col == 3:
                    ch_col = 0
                    ch_str += 1
                self.guitar_1 = QFrame(self.ui.gridLayoutWidget)
                self.guitar_1.setObjectName(u"guitar_1")
                self.guitar_1.setMinimumSize(QSize(200, 400))
                self.ui.gridLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
                self.guitar_1.setMaximumSize(QSize(200, 900000))
                self.guitar_1.setStyleSheet(u"background-color: rgb(35, 35, 35);")
                self.guitar_1.setFrameShape(QFrame.StyledPanel)
                self.guitar_1.setFrameShadow(QFrame.Raised)
                self.verticalLayout_14 = QVBoxLayout(self.guitar_1)
                self.verticalLayout_14.setSpacing(0)
                self.verticalLayout_14.setObjectName(u"verticalLayout_14")
                self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
                self.frame_img = QFrame(self.guitar_1)
                self.frame_img.setObjectName(u"frame_img")
                self.frame_img.setMinimumSize(QSize(0, 150))
                self.frame_img.setFrameShape(QFrame.StyledPanel)
                self.frame_img.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_5 = QHBoxLayout(self.frame_img)
                self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
                self.label_7 = QLabel(self.frame_img)
                self.label_7.setObjectName(u"label_7")
                self.label_7.setPixmap(QPixmap(f"{i['image']}"))
                self.label_7.setScaledContents(True)

                self.horizontalLayout_5.addWidget(self.label_7)

                self.verticalLayout_14.addWidget(self.frame_img)

                self.frame_ch = QFrame(self.guitar_1)
                self.frame_ch.setObjectName(u"frame_ch")
                self.frame_ch.setFrameShape(QFrame.StyledPanel)
                self.frame_ch.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_4 = QHBoxLayout(self.frame_ch)
                self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
                self.label_9 = QLabel(self.frame_ch)
                self.label_9.setObjectName(u"label_9")
                self.label_9.setStyleSheet(u"color:white")
                self.label_9.setText(f"{i['name']}")
                self.label_9.setWordWrap(True)

                self.horizontalLayout_4.addWidget(self.label_9)

                self.pushButton_2 = QPushButton(self.frame_ch)
                self.pushButton_2.setObjectName(u"pushButton_2")
                self.pushButton_2.setStyleSheet('background-color:#AFAFAF;')

                self.horizontalLayout_4.addWidget(self.pushButton_2)
                self.verticalLayout_14.addWidget(self.frame_ch)
                self.pushButton_d = QPushButton(self.frame_ch)
                self.pushButton_d.setObjectName(u"pushButton_d")
                self.pushButton_d.setStyleSheet('background-color:#AFAFAF;')
                self.pushButton_d.setIcon(QIcon('pictures/trash.png'))
                self.pushButton_d.clicked.connect(lambda checked=None, g=i['name']: self.remove_guitar(g))
                self.horizontalLayout_4.addWidget(self.pushButton_d)
                self.ui.gridLayout_4.addWidget(self.guitar_1, ch_str, ch_col, 1, 1)
                print('i', i)
                self.pushButton_2.clicked.connect(lambda checked=None, x=i['name']: self.test(x, flag))
                self.pushButton_2.setText('Выбор')
                ch_col += 1
                # Кнопка "Добавить"
                self.but_add = QPushButton(self.frame_ch)
                self.but_add.setObjectName(u"but_add")
                self.but_add.setStyleSheet(u"QPushButton {\n"
                                           "color:white;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "	background-color: rgb(61, 145, 255);\n"
                                           "}")
                if ch_col == 3:
                    ch_col = 0
                    ch_str += 1
                self.ui.gridLayout_4.addWidget(self.but_add, ch_str, ch_col, 1, 1)
                self.but_add.setText('Добавить')
                self.but_add.clicked.connect(self.add_guitar_page)
                # Кнопка "Добавить"
                self.but_add = QPushButton(self.frame_ch)
                self.but_add.setObjectName(u"but_add")
                self.but_add.setStyleSheet(u"QPushButton {\n"
                                           "color:white;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "	background-color: rgb(61, 145, 255);\n"
                                           "}")
                if ch_col == 3:
                    ch_col = 0
                    ch_str += 1
                self.ui.gridLayout_4.addWidget(self.but_add, ch_str, ch_col, 1, 1)
                self.but_add.setText('Добавить')
                self.but_add.clicked.connect(self.add_guitar_page)
        else:
            QtWidgets.QMessageBox.information(self, "Внимание", "Проверьте подключение к интернету")

    def mail(self):
        pyperclip.copy(self.ui.but_mail.text())
        QtWidgets.QMessageBox.information(self,"Почта",'Адрес электронной почты успешно скопирован в буфер обмена')

    def export_JSON(self):
        dict_export = {}
        dict_export['name'] = name_export
        ind_1 = 0
        ind_2 = 1
        for i in magazines:
            if i in magazines:
                dict_export[f'{i} price'] = spis_export [ind_1]
                dict_export[f'{i} rating'] = spis_export[ind_2]
                ind_1 += 2
                ind_2 +=2
        now = datetime.datetime.now()
        dict_export['date'] = now.strftime('%d.%m.%y')
        if not os.path.isdir('export'): os.mkdir('export')
        with open (f'export/JSON_export_{name_export} {now.strftime("%d.%m.%y")}.json','w') as f:
            json.dump(dict_export,f,indent=4)
        QtWidgets.QMessageBox.information(self,'Экспорт','Экспорт в JSON-файл произведён успешно')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.open_json()
    sys.exit(app.exec_())