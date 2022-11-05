import taglib
import os


def get_title(filepath):
    wavfile = taglib.File(filepath)
    try:
        title = wavfile.tags["TITLE"][0]
        wavfile.close()
        return title
    except KeyError:
        wavfile.close()
        return filepath


def get_ext(path):
    ext = os.path.splitext(path)[1]
    return ext


def check_only_wav_ext(list):
    new_list = []
    for item in list:
        ext = get_ext(item)
        if ext == '.wav':
            new_list.append(item)
    return new_list


def recover_title():
    filenames = os.listdir()
    filenames = check_only_wav_ext(filenames)
    for name in filenames:
        oldname = name
        newname = get_title(name)
        os.rename(oldname, newname)
