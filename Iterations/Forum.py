'''
Условие
Гости Всемирного Форума собрались по домам. Мы не знаем, представители каких делегаций были на форуме, но знаем, что делегаций не больше 197 (по количеству стран в мире). Всё, что может сказать каждый отдельный гость о себе, — номер делегации, которой он принадлежит. Необходимо рассадить гостей по автобусам так, чтобы каждой присутствующей делегации достался ровно один автобус. Какое минимальное количество автобусов нужно, чтобы рассадить гостей?

Формат входных данных
Входные данные содержат список чисел через пробел — номер делегации каждого отдельного гостя.

Формат выходных данных
Выходные данные должны содержать одно число — минимальное количество автобусов.
'''
A = input()
A = A.split(sep=" ")
A = list(set(A))
print(len(A))