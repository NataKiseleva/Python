k = 2
while (k != 1):
    print("Введите три числа")
    a = input()
    b = input()
    c = input()
    a = float(a)
    b = float(b)
    c = float(c)

    if ((a + b) == c):
        print("ok")
    else:
        print("no")
    if ((a * b) == c):
        print("ok")
    else:
        print("no")
    if ((a % c) == b):
        print("ok")
    else:
        print("no")
    if b != 0:
        if ((a / b) == c):
            print("ok")
        else:
            print("no")
    else:
        print("no")
    print("Для завершения работы, нажмите 1. Для продолжения любую цифру")
    k = input()
    k = int(k)