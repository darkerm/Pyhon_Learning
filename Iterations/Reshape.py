'''
Условие
Дан вектор, состоящий из p чисел.
Необходимо преобразовать вектор в матрицу размера n × m = p, состоящую из n строк и m столбцов. Матрица заполняется последовательно, то есть элементы вектора с 1 по m попадут в первую строку матрицы, с m + 1 по 2 m — во вторую строку и так далее.

При решении задачи запрещено использовать библиотеку numpy.

Формат входных данных
Первая строка входных данных содержат целое число p — количество элементов в входном векторе. Вторая строка содержит p целых чисел — элементы вектора. Третья строка содержит два целых числа n и m — размеры итоговой матрицы.

Формат выходных данных
Выходные данные должны содержать итоговую матрицу. Строки матрицы разделяются переводами строки, числа в каждой строке — пробелами.
'''
p = int(input())
v = input().split()
n, m = map(int, input().split())
[print(" ".join(v[i:i + m])) for i in range(0, len(v), m)]