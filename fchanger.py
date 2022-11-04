import os
import taglib

# сделать ввод нечувствительным к регистру
# получить список имен всех файлов в папке
# получить имя файла без расширения
# вырезать требуемое слово
# перезаписать новое имя поверх старого

# заменить все символы разделения в имени файла на пробел


# Прежде чем экспериментировать с файлами и их именами, мне определенно необходимо сделать резервную базу данных, чтобы восстановить все в случае багов.


def get_name_without_ext(name_ext):
    names_without_ext = []
    for name in name_ext:
        names_without_ext.append(os.path.splitext(name)[0])
    return names_without_ext


def get_cleared_name(trash_word, dirty_names):
    cleared_names = []
    for name in dirty_names:
        name = (
            name.replace(trash_word, "")
            .replace("-", " ")
            .replace("_", " ")
            .replace(",", " ")
        )
        cleared_names.append(name)
    return cleared_names


def create_trash_list(whole_list, target):
    trash_list = []
    for word in whole_list:
        if target in word:
            trash_list.append(word)
    return trash_list


def set_new_names(old_names, new_names):
    a = 0
    wav_ext = ".wav"
    while a < len(old_names):
        try:
            os.rename(old_names[a], new_names[a] + wav_ext)
        except FileExistsError:
            None
        except IndexError:
            None
        a += 1


def clear_screen():
    os.system("cls")


def restore_all_names_from_tag():
    filenames = os.listdir()
    non_modifyed_names_ext = []
    for pathname in filenames:
        file_ext = os.path.splitext(pathname)[1]
        if file_ext == '.wav':
            song = taglib.File(pathname)
            try:
                non_modifyed_names_ext.append(song.tags['TITLE'][0])
            except KeyError:
                None
    wext_non_mod_name = get_name_without_ext(non_modifyed_names_ext)
    set_new_names(filenames, wext_non_mod_name)


def remove_word():
    filenames_list = os.listdir()
    target_word_one = input("Введите слово, которое надо удалить: ")
    trash_list = create_trash_list(filenames_list, target_word_one)
    wext_name = get_name_without_ext(trash_list)
    cleared_names = get_cleared_name(target_word_one, wext_name)
    set_new_names(trash_list, cleared_names)


def add_space_before_subline(target_subline):
    filenames = os.listdir()
    new_namelist = []
    result_subline = ' ' + target_subline
    for name in filenames:
        new_name = name.replace(target_subline, result_subline)
        new_namelist.append(new_name)
    new_namelist = get_name_without_ext(new_namelist)
    set_new_names(filenames, new_namelist)
        

while True:
    clear_screen()
    choise = input(''''remove' - удалить нужную подстроку из имени
'restore' - восстановить все из тегов
'bspace' - добавить пробел перед подстрокойханьчд
>>>''')
    if choise == 'remove':
        remove_word()
    if choise == 'restore':
        restore_all_names_from_tag()
    if choise == 'bspace':
        target = input('Введите слово: ')
        add_space_before_subline(target)
