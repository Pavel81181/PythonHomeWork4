n = int(input('Введите количество элементов в первом наборе чисел: '))
a = list()
for i in range(n):
    a.append(int(input(f'Введите {i+1} элемент: ')))
print (f'Первый набор: {a}')
a1 = set(a)
m = int(input('Введите количество элементов во втором наборе чисел: '))
b = list()
for i in range(m):
    b.append(int(input(f'Введите {i+1} элемент:')))
print (f'Второй набор: {b}')
b1 = set(b)
c = sorted(a1.intersection(b1))
print(f'Повторяющиеся элементы: {c}')