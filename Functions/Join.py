'''
Условие
Требуется реализовать на языке Python функцию Join(array, separator), которая принимает два параметра — список строк и разделитель — и возвращает строку, полученную соединением элементов переданного списка, при этом между элементами списка вставляется разделитель (separator). Если не передать функции разделитель, то она должна использовать в качестве разделителя пробел. Пример использования функции в примерах тестов.

В решении запрещено использовать стандартную функцию join.

При решении задачи запрещено использовать библиотеку numpy.

Формат выходных данных
Код решения должен содержать только определение и реализацию функции. Он не должен ничего выводить.
'''
def Join(a, b=" "):
    c =  str(a.pop(0))
    while a:
        c += b + str(a.pop(0))
    return c