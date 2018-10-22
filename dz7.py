import  random

def cards():
    a = []
    b = []
    c = []
    seq = random.sample(range(1, 91), 15)
    a = (seq[0:5])
    b = (seq[5:10])
    c = (seq[10:15])

    a.sort()
    b.sort()
    c.sort()

    card = (a, b, c)
    return card

player_card = cards()
comp_card = cards()

def show_card(card):
    for line in card:
        for el in line:
            print('{}'.format(el), end = ' ')
        print('\n')
'''
def create_boch():
    sp = []
    boch = 0
    if boch not in sp:
        boch = random.randint(1, 91)
        sp.append(boch)
    print('Новый бочонок:', boch)
'''

def check(card, boch):
    for line in card:
        for i, el in enumerate(line):
            if el == boch:
                line[i] = '-'
                return True
    return False

def compare(card):
    for line in card:
        for i, el in enumerate(line):
            if not type(el) == int:
                return True
    return False



bochs = random.sample(range(1, 91), 90)
print('Давай поиграем!\n')
for n, boch in enumerate(bochs):

    print('--Карточка игрока--\n')
    show_card(player_card)
    print('-------------------\n')
    print('--Карточка компьютера--\n')
    show_card(comp_card)
    print('-----------------------')
    print('Новый бочонок: {}. Осталось бочонков: {}.'.format(boch, len(bochs) - n -1 ))

    while True:
        ans = input('Зачеркнуть цифру? Выйти? y/n/q:')
        if ans == 'q':
            print('Слабак')
            exit()
        elif ans == 'y':
            if not check(player_card, boch):
                print('Вы проиграли')
                exit()
            break

        elif ans == 'n':
            if check(player_card, boch):
                print('Вы проиграли')
                exit()

            break

    check(comp_card, boch)

    if compare(comp_card) == compare(player_card):
        print('Ничья')
    elif compare(comp_card):
        print('Вы проиграли')
    else:
        print('Вы выйграли!')


