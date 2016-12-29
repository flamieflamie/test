def is_year_leap (y):
    if (y%4 != 0):
        return "Год не является високосным"
    else:
        return "Год является високосным"

ex="Y"
while (ex=="Y") or (ex=="y"):
    z=True
    while z:
        z=False
        try:
            year=int(input("Введите год: \n"))
        except ValueError:
            print("Необходимо вводить целое число.")
            z=True
 
    print(is_year_leap(year))
    ex=input("Продолжить? (Y/N)\n ")

