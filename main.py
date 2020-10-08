'''

# Условные операторы

name1 = 10
name2 = 20

if name1 == name2:
    print('name1 > name2')
    if name2 is True:
        print('True')
if name1 >= name2:
    pass
elif name1 < name2:
    print('name1 < name2')  
elif name1 != name2:
    pass
else:
    print('name1 = name2')
'''

# циклы

# Список [], Кортедж ()  в списске можно менять эллементы, а в кортедже нет.
n = [1, 2, 3, 'sasory']  # Список
print(n[3])              # печатает элемент из списка под указанным номером от (0;+n) или от (-1;-n)
print(len(n))            # подсчитывает колличество эллементов в списке
n.append(7)
print(n)
'''
for i in n:
    print(i)
for j in 'sasory':
    print(j)
'''

m=0
while m < 10:
    print(m)
    m += 1
while True:              #бесконечный цикл
    print(m)
    m += 1