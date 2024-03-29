'''
Условие
Дан массив чисел. Нужно заменить в нем максимальный элемент на минимальный из этого же массива. Если максимальных несколько — заменить каждый из них.

При решении задачи запрещено использовать библиотеку numpy.

Формат входных данных
Входные данные содержат несколько чисел, разделенных пробелами.

Формат выходных данных
Выходные данные должны содержать массив, в котором максимальные элементы заменены на минимальный. Элементы массива должны быть разделены пробелами.
'''
a = input().split(sep=" ")
b = str(max(int(i) for i in a))
c = str(min(int(i) for i in a))
for i in range(len(a)):
    if a[i] == b:
        a[i] = c
print(" ".join(a))