import os


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


def remove_mutlispaceses(old_list):
    new_list = []
    for old_name in old_list:
        new_name = ' '.join(old_name.split())
        new_list.append(new_name)
    return new_list


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


def remove_word(target_word_one):
    filenames_list = os.listdir()
    trash_list = create_trash_list(filenames_list, target_word_one)
    wext_name = get_name_without_ext(trash_list)
    cleared_names = get_cleared_name(target_word_one, wext_name)
    cleared_names = remove_mutlispaceses(cleared_names)
    set_new_names(trash_list, cleared_names)

if __name__ == "__main__":
    while True:
        choise = input()
        if choise != "exit":
            remove_word(choise)
        else:
            break
