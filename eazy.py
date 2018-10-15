import os
import shutil

#eazy_1

def create():
    a = 1
    while a < 10:
        try:
            dir_path = os.path.join(os.getcwd(), 'dir_' + str(a))
            os.mkdir(dir_path)
            print('Директория создана')
        except FileExistsError:
            print('Директория существует')
        a += 1


def delete():
    a = 1
    while a < 10:
        try:
            dir_path = os.path.join(os.getcwd(), 'dir_' + str(a))
            os.rmdir(dir_path)
            print('Директория удалена')
        except Exception:
            print('Уже удалёна')
        a += 1

print(create())

#eazy_2
def pap():
    try:
        list = os.listdir(path=os.getcwd())
        print('Папки:', list)
    except Exception:
        print('Такой папки нет')

#eazy_3
def copy():
    copy_file = __file__ + ".copy"
    shutil.copyfile(__file__, copy_file)
    return('Скопировано')
