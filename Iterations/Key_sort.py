'''
Условие
Дан массив слов, нужно отсортировать его по второй букве. Гарантируется, что в каждом слове не меньше двух букв, а все вторые буквы слов различны.

При решении задачи запрещено использовать библиотеку numpy.

Формат входных данных
Входные данные содержат слова, разделённые пробелами.

Формат выходных данных
Выходные данные должны содержать строку слов, разделённых пробелом, отсортированных по второй букве.
'''
a = input().split()
a.sort(key=lambda i: i[1])
print(" ".join(a))