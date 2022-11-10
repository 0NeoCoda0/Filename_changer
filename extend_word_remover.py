import os

# Удаляет подстроку в слове, которое находится в указанной папке

def is_wav(name):
   b = os.path.splitext(name)[1] == '.wav'
   return b

def get_dir_path(dir_name):
    path = os.path.abspath(dir_name)
    return path

def is_dir(name):
    b = os.path.isdir(name)
    return b

def get_filelist(path):
    list = os.listdir(path)
    return list


def remove_space(word):
    words = word.split()
    words[0] = words[0].capitalize()
    new_word = ' '.join(words)
    return new_word

def main():
    choosen_dir_name = input("Введите имя папки: ")
    if is_dir(choosen_dir_name):
        dir_path = get_dir_path(choosen_dir_name)
        filename_list = get_filelist(dir_path)
        target_word = input("Введите целевое слово для удаления: ")
        for old_name in filename_list:
            if is_wav(old_name):
                new_name = old_name.replace(target_word, '')
                new_name = remove_space(new_name)
                old_name_path = f"{dir_path}\{old_name}"
                new_name_path = f"{dir_path}\{new_name}"
                os.rename(old_name_path, new_name_path)

while True:
    main()
            