'''
Условие
Требуется реализовать на языке Python функцию PrintMatrix(mat), которая принимает двумерный массив и печатает его. Пример использования функции в примерах тестов.

При решении задачи запрещено использовать библиотеку numpy.

Формат выходных данных
Код решения должен содержать только определение и реализацию функции.
'''
def PrintMatrix(a):
    [print(*i) for i in a]