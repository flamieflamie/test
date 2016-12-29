def arithmetic ():
    x=True;
    
    while x==True:
        try:
            a = int(input ("Введите первое число\n"))
        except ValueError:
            print("Необходимо ввести число\n")
        else:
            x=False

    y=True;        
    while y==True:
        try:
            b = int(input ("Введите второе число\n"))
        except ValueError:
            print("Необходимо ввести число\n")
        else:
            y=False

            z=True
            
    while z==True:
        z=False;
        operation = input("Выберите одну из арифметических операций (+, -, *, /)\n")
        if (operation == '+'):
            result = a+b
        elif (operation == '-'):
            result = a-b
        elif (operation == '*'):
            result = a*b
        elif (operation == '/'):
            if b == 0:
                result = "Делить на ноль нельзя"
            else:
                result = a/b
        else:
           print("Необходимо выбрать одну из следующих операций: +, -, *, / \n")
           z=True
    return result

i = True

while (i):
    result=arithmetic()
    print (result)
    ex = input("Продолжить(Y/N)?\n")
    if (ex == "Y") or (ex == "y"):
        i = True
    else:
        i = False
