'''
Условие
Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево (без учета пробелов и регистра символов).

При решении задачи запрещено использовать библиотеку numpy.

Формат входных данных
Входные данные содержат фразу, не содержащую знаков препинания, в которой слова разделены пробелами.

Формат выходных данных
Выходные данные должны содержать True, если фраза — палиндром, и False в противном случае.
'''
a = list(input().lower())
b = []
for i in range(len(a)):
    if str(a[i]).isalpha():
        b.append(a[i])
c = b.copy()
c.reverse()
if c == b:
    print("True")
else:
    print("False")