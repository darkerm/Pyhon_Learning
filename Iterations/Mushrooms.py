'''
Условие
Аня очень хорошо разбирается в грибах. Грибы бывают разные. Опята, лисички. сыроежки, подосиновики, подберезовики, обабки, маслята, оленьи рожки, поганки (ядовитые).
 Boletus edulis (белые грибы) — самые хорошие. Нужно посчитать, сколько Boletus edulis собрала Аня.

Формат входных данных
В первой строке содержится число N — количество грибов. В следующих N строках — названия грибов.

Формат выходных данных
Выходные данные должны содержать одно число — количество Boletus edulis. Регистр не имеет значения, т.е. к примеру BoLeTuS eDuLiS и bolETUS edulIS — один и тот же гриб.

Ограничения
1≤N≤100
'''
I = int(input())
mushroom = []
SM = 0
for i in range(I):
    M = input()
    M = M.lower()
    mushroom.append(M)
for i in mushroom:
    if i == "boletus edulis":
        SM = SM + 1
print(SM)