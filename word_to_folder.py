# найти все файлы с целевым словом и отправить их в одноименную папку

import os
import shutil



while True:
    all_files_in_dir = os.listdir()
    target_word = input("Введите целевое слово для сортировки: ")
    target_word = target_word.lower()
    target_list = []
    for filename in all_files_in_dir:
        if filename.lower().find(target_word) != -1:
            target_list.append(filename)

    if target_list != []:
        destination = target_word.lower().capitalize()
        try:
            os.mkdir(destination)
        except FileExistsError:
            None
        for name in target_list:
            shutil.move(name, destination)
