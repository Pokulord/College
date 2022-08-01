#! Конвертер из DOCX в PDF

import os
import time

from docx2pdf import convert


class Convert:
    def __init__(self):
        self.dir_list()

    def dir_list(self):
        if not os.path.isdir('results'):
            os.mkdir('results')
        files_in_dir = os.listdir()
        print(files_in_dir)
        files_to_conv = [i for i in files_in_dir if i.endswith('.docx')]
        if len(files_to_conv) == 0:
            print('Не обнаружено файлов с расширением DOCX')
            return 
        for i in files_to_conv:
            new_name = i.split('.docx')[0] + '.pdf'
            convert(i,f'results\\{new_name}')
            print(f'Файл {new_name} сконвертирован')
        print('-'*40)
        print('Работа программы завершена')
        time.sleep(4)


if __name__ == '__main__':
    Convert()
