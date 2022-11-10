import os
import recover_title
import genre_sort
import remove_word

# сделать ввод нечувствительным к регистру

# Прежде чем экспериментировать с файлами и их именами, мне определенно необходимо сделать резервную базу данных, чтобы восстановить все в случае багов.


def clear_screen():
    os.system("cls")


def choose_filename_action():
    print(''''remove' - удалить нужную подстроку из имени
'recover' - восстановить все из тегов
'gsort' - сортировка файлов по папкам в соответствии с тегом "ЖАНР"
'exit' - выход из программы
>>>''')

    if choise == 'remove':
        target = ''
        while target != "*":
            target = input("Введите слово, которое надо удалить: ")
            remove_word.remove_word(target)

    if choise == 'recover':
        print('Идет чтение тегов и восстановление заголовков.')
        recover_title.recover_title()

    if choise == 'gsort':
        genre_sort.genre_sort()

    if choise == 'exit':
        return 1


while code != 1:
    clear_screen()
    print("File changer редактирует имена файлов, помогая навести порядок в библиотеке звуков.\n")
    choise = input()
    code = choose_filename_action(choise)


# v0.3
# afspace и bspace - работают не корректно, удаляют exe файл, вносят путаницу в имена файлов
# добавить возможность перевести теги на русский с английского через гугл
# добавить возможность сохранить теги в json файл и при необходимости их восстановить
# добавить сортировку по папкам на основании введенного слова. Слово из перемещенных файлов удалить.
# добавить поиск файла по тегам
