'''
Условие
Запуск космического корабля это очень торжественное событие, требующее обратного отсчета.

Формат входных данных
На вход программа получает одно число N — количество секунд до запуска.

Формат выходных данных
Программа должна вывести обратный отсчет от N до 1, завершающийся командой "Start".
Каждый шаг отсчета сопровождается восклицательными знаками. С каждой секундой их количество увеличивается на единицу,
так что команда "Start" сопровождается N восклицательными знаками.

Ограничения
1<N<100
'''
N = int(input())
z = "!"
for i in range(N):
    Z = z * i
    Q = N - i
    print(str(Q) +  str (Z))
z = z * N
print("Start" + z)