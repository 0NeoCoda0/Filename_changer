import os
import taglib
import shutil

"""
Выявить все существующие жанры у файлов и вернуть их список
Создать папки на основании списка жанров
Переместить файлы с одноименным жанром в соответствующую папки
"""

""" get genre list
Собрать список всех файлов
Выявить тег жанра у файла
Сохранить тег в список, если такого еще нет
"""

""" переместить файлы по папкам
Выявить тег жанра у файла
Найти соотвествие имени тега и имени папки
Переместить файл в папку
"""

def collect_filenames():
    filenames = os.listdir()
    return filenames


def tag_is_new(incoming_tag, tag_list):
    for exist_tag in tag_list:
        if exist_tag == incoming_tag:
            return False
        else:
            pass
    return True


def file_is_wav(file):
    extention = os.path.splitext(file)[1]
    if extention == '.wav':
        return True
    else:
        return False


def create_genre_folder(genre_list):
    for genre in genre_list:
        try:
            os.mkdir(genre)
        except FileExistsError:
            None


def format_taglist(tag_list):
    tag_list.sort()
    tag_list.pop(0)


def get_genre_tag(file):
    if file_is_wav(file):
        song = taglib.File(file)
        genre_tag = song.tags["GENRE"][0]
        song.close()
        return genre_tag
    return ''


def get_genre_list(namelist):
    genre_list = []
    for name in namelist:
        genre_tag = get_genre_tag(name)
        if genre_list == []:
            genre_list.append(genre_tag)
        if tag_is_new(genre_tag, genre_list):
            genre_list.append(genre_tag)
    format_taglist(genre_list)
    return genre_list


def move_files_to_genre_folders(namelist):
    for filename in namelist:
        destination_folder = get_genre_tag(filename)
        if destination_folder != '':
            shutil.move(filename, destination_folder)

def genre_sort():
    namelist = collect_filenames()
    genre_list = get_genre_list(namelist)
    create_genre_folder(genre_list)
    move_files_to_genre_folders(namelist)