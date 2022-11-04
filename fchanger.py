import os
import taglib
import time

# сделать ввод нечувствительным к регистру

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
            os.rename(old_names[a], new_names[a] + ' ' +str(a) + ' ' + wav_ext)
        except IndexError:
            None
        a += 1


def clear_screen():
    os.system("cls")


def remove_mutlispaceses(old_list):
    new_list = []
    for old_name in old_list:
        new_name = ' '.join(old_name.split())
        new_list.append(new_name)
    return new_list


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
    wext_non_mod_name = remove_mutlispaceses(wext_non_mod_name)
    set_new_names(filenames, wext_non_mod_name)


def remove_word(target_word_one):
    filenames_list = os.listdir()
    trash_list = create_trash_list(filenames_list, target_word_one)
    wext_name = get_name_without_ext(trash_list)
    cleared_names = get_cleared_name(target_word_one, wext_name)
    cleared_names = remove_mutlispaceses(cleared_names)
    set_new_names(trash_list, cleared_names)


def add_space_after_subline(target_subline):
    filenames = os.listdir()
    new_namelist = []
    result_subline = target_subline + ' '
    for name in filenames:
        file_ext = os.path.splitext(name)[1]
        if file_ext == '.wav':
            new_name = name.replace(target_subline, result_subline)
            new_namelist.append(new_name)
    new_namelist = get_name_without_ext(new_namelist)
    new_namelist = remove_mutlispaceses(new_namelist)
    set_new_names(filenames, new_namelist)

def add_space_before_subline(target_subline):
    filenames = os.listdir()
    new_namelist = []
    result_subline = ' ' + target_subline
    for name in filenames:
        file_ext = os.path.splitext(name)[1]
        if file_ext == '.wav':
            new_name = name.replace(target_subline, result_subline)
            new_namelist.append(new_name)
    new_namelist = get_name_without_ext(new_namelist)
    new_namelist = remove_mutlispaceses(new_namelist)
    set_new_names(filenames, new_namelist)    

while True:
    clear_screen()
    print("File changer редактирует имена файлов, помогая навести порядок в библиотеке звуков.\n")
    print(''''remove' - удалить нужную подстроку из имени
'restore' - восстановить все из тегов
'bspace' - добавить пробел перед подстрокой
'afspace' - добавить пробел после подстроки
'exit' - выход из программы
>>>''')
    choise = input()
    if choise == 'remove':
        print("Введите слово, которое надо удалить: ")
        target = input()
        remove_word(target)

    if choise == 'restore':
        restore_all_names_from_tag()

    if choise == 'bspace':
        print('Введите слово: ')
        target = input()
        add_space_before_subline(target)

    if choise == 'afspace':
        print('Введите слово: ')
        target = input()
        add_space_after_subline(target)

    if choise == 'exit':
        break
