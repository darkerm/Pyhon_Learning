'''
Условие
Условный оператор — это просто! Верно?
Напишите программу, которая принимает на вход от пользователя одну строку. Если пользователь ответил "Просто!", "Easy!" или "Einfach!", напечатайте в ответ улыбающийся смайл ":)". В ином случае — грустный смайл ":(".
'''
sentence = input()
if sentence == "Просто!" or sentence == "Easy!" or sentence == "Einfach!":
    print(":)")
else:
    print(":(")