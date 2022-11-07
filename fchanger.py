import os
import taglib
import time
import recover_title
import genre_sort

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
            os.rename(old_names[a], new_names[a] +
                      ' ' + str(a) + ' ' + wav_ext)
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
'recover' - восстановить все из тегов
'bspace' - добавить пробел перед подстрокой - баги
'afspace' - добавить пробел после подстроки - баги
'gsort' - сортировка файлов по папкам в соответствии с тегом "ЖАНР"
'exit' - выход из программы
>>>''')
    choise = input()
    if choise == 'remove':
        target = ''
        while target != "*":
            target = input("Введите слово, которое надо удалить: ")
            remove_word(target)

    if choise == 'recover':
        print('Идет чтение тегов и восстановление заголовков.')
        recover_title.recover_title()

    if choise == 'bspace':
        target = input('Введите слово: ')
        add_space_before_subline(target)

    if choise == 'afspace':
        target = input('Введите слово: ')
        add_space_after_subline(target)

    if choise == 'gsort':
        genre_sort.genre_sort()

    if choise == 'exit':
        break

# v0.5
# afspace и bspace - работают не корректно, удаляют exe файл, вносят путаницу в имена файлов
# добавить возможность перевести теги на русский с английского через гугл
# добавить возможность сохранить теги в json файл и при необходимости их восстановить
# добавить сортировку по папкам на основании введенного слова. Слово из перемещенных файлов удалить.
# добавить поиск файла по тегам
