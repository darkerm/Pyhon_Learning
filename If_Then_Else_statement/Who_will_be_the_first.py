'''
Условие
Помогите трем студентам понять, кто из них первый пойдет решать диффуры, если преподаватель вызывает к доске в алфавитном порядке.

Формат входных данных
Входные данные содержат три фамилии студентов, разделенные переносом строки. Используется кодировка UTF8.

Формат выходных данных
Программа должна напечатать фамилию студента, который пойдет к доске первым.
'''
import sys
sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

Input1 = input()
Input2 = input()
Input3 = input()
Input = []
Input.append(Input1)
Input.append(Input2)
Input.append(Input3)
Input.sort()
print(Input[0])