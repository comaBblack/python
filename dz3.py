#eazy_1

def krug(number, ndigits):
    a = int(number * 10 ** ndigits) / (10 ** ndigits)
    return a

print(krug(2.1234567, 5))
print(krug(2.1999967, 5))
print(krug(2.9999967, 5))

#eazy_2

def ticket(number):
    number = str(number)
    if len(number) != 6:
        return 'Неправильный номер'
    elif int(number[0]) + int(number[1]) + int(number[2]) - int(number[3]) -int(number[4]) -int(number[5]) == 0:
        return 'У Вас счастливый билет!'
    else:
        return 'Ваш билет не счастливый'
print(ticket(123006))
print(ticket(12321))
print(ticket(436751))


#normal_1
def fib (n,m):
    fib = [1, 1]
    a = 0
    b = 0
    c = 1
    while a <= m:
        fib.append(fib[b]+fib[c])
        a += 1
        b += 1
        c += 1
    m = fib[n-1:m]
    return m
print(fib(1,6))
print(fib(5,10))
print(fib(3,15))

#normal_2
def sort(list):
    list2 = []
    while len(list) > 0:
        max = 2147483647 ** 20000
        for i in list:
            if i < max:
             max = i
        list2.append(max)
        list.remove(max)

    return list2
print (sort([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

#normal_3
def filter(cond,list):
    for a in list:
        if not cond(a):
            list.remove(a)
    return list

list1 = [ '','2', '10', '-106', '8', '', '24y4', '0', '14']
filter(len, list1)
print(list1)

#normal_4
#работает только если за (x1,y1) принимать верхнюю левую вершину
def par(x1,x2,x3,x4,y1,y2,y3,y4):
    if x1 - x3 == x2 - x4 and y1 == y2 and y3 == y4:
        return 'Точки являются вершинами параллелограмма'
    else:
        return 'Точки не являются вершинами параллелограмма'
print(par(3,5,6,8,4,4,7,7,))
print(par(3,3,6,8,4,4,9,7,))



