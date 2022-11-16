import os

filenames = os.listdir()
numbers = "1234567890"
for name in filenames:
    new_name = name
    for n in numbers:
        new_name = new_name.replace(n, '')
    name_list = new_name.split()
    new_name = ' '.join(name_list)
    try:
        os.rename(name, new_name)
    except FileExistsError:
        None
    filenames = os.listdir()