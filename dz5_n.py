import eazy
while True:
    ans = ''
    print(
    '1. Перейти в папку\n\
    2. Посмотреть содержимое текущей папки\n\
    3. Удалить папку\n\
    4. Создать папку\n\
    5. Выйти')
    ans = input('Что сделать?')
    if ans == '1':
        name = input('Введите название папки:')
        eazy.change(name)
    elif ans == '2':

        eazy.pap(name)
    elif ans == '3':
        name = input('Введите название папки:')
        eazy.delete(name)
    elif ans == '4':
        name = input('Введите название папки:')
        eazy.create(name)
    elif ans == '5':
        print('Не очень-то и хотелось тебе помогать')
        break
