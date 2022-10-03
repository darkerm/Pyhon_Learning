'''
Условие
Пусть задана некоторая матрица A
Требуется написать программу, выполняющую поворот этой матрицы по часовой стрелке k∈Z раз. При k<0 такой поворот эквивалентен повороту против часовой стрелки |k| раз.

В задаче запрещено пользоваться какими-либо пакетами.

Формат входных данных
Первая строка входного файла содержит натуральные числа n,m,k — количество строк, столбцов и поворотов. В каждой их следующих n строк содержится по m натуральных чисел — значения элементов матрицы.

Формат выходных данных
Выходной файл должен содержать повернутую матрицу. Каждая строка матрицы записывается в отдельной строке, при этом элементы разделены символом "пробел", аналогично входным данным.

Ограничения
2⩽n,m⩽2000
−100⩽k⩽100
'''
def rotate90(a):
    for i in zip(*a):
        A = list(reversed(i))
        print(" ".join(A))

def rotate180(a):
    while len(a) != 0:
        A = list(reversed(a.pop()))
        print(" ".join(A))

def rotate270(a):
    for i in zip(*a):
        A = list(i)
        AA.append(A)
    A = list(reversed(AA))
    for i in A:
        print(" ".join(i))

def rotate360(a):
    for i in a:
        print(" ".join(i))


n = input().split(sep=" ")
a = []
AA= []
for i in range(int(n[0])):
   a.append(input().split(sep=" "))
s = int(n[2]) % 4
if int(n[2]) > 0:
    if s == 0:
        rotate360(a)
    elif s == 1:
        rotate90(a)
    elif s == 2:
        rotate180(a)
    elif s == 3:
        rotate270(a)
else:
    if s == 0:
        rotate360(a)
    elif s == 1:
        rotate90(a)
    elif s == 2:
        rotate180(a)
    elif s == 3:
        rotate270(a)