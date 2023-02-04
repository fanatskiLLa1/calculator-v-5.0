import sys
from math import factorial, sqrt, cos, sin, tan

print("Автор - fanat skiLLa1")
print()
print("Здравствуйте, вас приветствует \"умный калькулятор!\" (v 3.0)\n")
print("|======================================================|")
print("|P.s: весь текст нужно писать с маленькой буквы!       |")
print("|======================================================|\n")

print("Вы хотите воспользоваться программой? (да\нет):", end=" ")

ans1 = input()

if ans1 == "да":
    print()
    print("Список команд \"умного калькулятора\":")
    print()
    print("|----------------------------------|")
    print("|1) Сумма чисел                    |")
    print("|2) Вычитание чисел                |")
    print("|3) Умножение чисел                |")
    print("|4) Деление чисел                  |")
    print("|5) Возведение числа в степень     |")
    print("|6) Факториал числа                |")
    print("|7) Сумма цифр числа               |")
    print("|8) Перевод из дес. СС в двоич. СС |")
    print("|9) Перевод из дес. СС в восьм. СС |")
    print("|10) Перевод из дес. СС в шестн. СС|")
    print("|11) Корень числа                  |")
    print("|12) Решение квадр. уравнений      |")
    print("|13) Тригонометрия                 |")
    print("|14) Выход                         |")
    print("|----------------------------------|\n")

    print("Выберите пункт (только цифра):", end=" ")
    ans2 = int(input())

else:
    sys.exit()

while ans2 != 14:
    if ans2 == 1:
        print()
        print("Вы выбрали пункт --> \"Сумма чисел\"!\n")
        print("Введите первое число:", end=" ")
        n1 = float(input())
        print("Введите второе число:", end=" ")
        n2 = float(input())
        summa = n1 + n2
        summa1 = round(summa, 5)
        print()
        print(f"{n1} + {n2} = {summa1}")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 2:
        print()
        print("Вы выбрали пункт --> \"Вычитание чисел\"!\n")
        print("Введите первое число:", end=" ")
        n1 = float(input())
        print("Введите второе число:", end=" ")
        n2 = float(input())
        unsumma = n1 - n2
        unsumma1 = round(unsumma, 5)
        print()
        print(f"{n1} - {n2} = {unsumma1}")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 3:
        print()
        print("Вы выбрали пункт --> \"Умножение чисел\"!\n")
        print("Введите первое число:", end=" ")
        n1 = float(input())
        print("Введите второе число:", end=" ")
        n2 = float(input())
        mult = n1 * n2
        mult1 = round(mult, 5)
        print()
        print(f"{n1} * {n2} = {mult1}")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 4:
        print()
        print("Вы выбрали пункт --> \"Деление чисел\"!\n")
        print("Введите первое число:", end=" ")
        n1 = float(input())
        print("Введите второе число:", end=" ")
        n2 = float(input())
        unmult = n1 / n2
        unmult1 = round(unmult, 5)
        print()
        print(f"{n1} : {n2} = {unmult1}")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 5:
        print()
        print("Вы выбрали пункт --> \"Возведение числа в степень\"!\n")
        print("Введите число:", end=" ")
        n1 = float(input())
        print("Введите степень:", end=" ")
        n2 = int(input())
        stepi = n1 ** n2
        stepi1 = round(stepi, 5)
        print()
        print(f"{n1} ** {n2} = {stepi1}")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 6:
        print()
        print("Вы выбрали пункт --> \"Факториал числа\"!\n")
        print("Введите число:", end=" ")
        n1 = int(input())
        fact = factorial(n1)
        print()
        print(f"{n1}! = {fact}")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 7:
        print()
        print("Вы выбрали пункт --> \"Сумма цифр числа\"!\n")
        print("Введите число:", end=" ")
        n1 = int(input())
        summa = 0
        while n1 != 0:
            digit = n1 % 10
            summa = summa + digit
            n1 = n1 // 10
        print()
        print(f"Сумма цифр числа = {summa}")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 8:
        print()
        print("Вы выбрали пункт --> \"Перевод из дес. СС в двоич. СС\"!\n")
        print("Хорошо. Введите число:", end=" ")
        n = int(input())
        bini = bin(n)[2:]
        print()
        print(f"{n}\u2081\u2080 = {bini}\u2082")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 9:
        print()
        print("Вы выбрали пункт --> \"Перевод из дес. СС в восьм. СС\"!\n")
        print("Вау!. Хороший выбор. Вводите число:", end=" ")
        n = int(input())
        octi = oct(n)[2:]
        print()
        print(f"{n}\u2081\u2080 = {octi}\u2088")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 10:
        print()
        print("Вы выбрали пункт --> \"Перевод из дес. СС в шестн. СС\"!\n")
        print("Ничего себе!. Отличный выбор. Пишите число:", end=" ")
        n = int(input())
        hexi = hex(n)[2:]
        print()
        print(f"{n}\u2081\u2080 = {hexi}\u2081\u2086")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 11:
        print()
        print("Вы выбрали пункт --> \"Корень числа\"!\n")
        print("Введите число:", end=" ")
        n = float(input())
        sqrti = sqrt(n)
        sqrti1 = round(sqrti, 5)
        print()
        print(f"√{n} = {sqrti1}")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    elif ans2 == 12:
        print()
        print("Вы выбрали пункт --> \"Решение квадр. уравнений\"!\n")
        print("Введите коэффициенты квадр. уравнения (через пробел):", end=" ")
        a, b, c = map(int, input().split())
        print()
        print(f"({a})x\u00b2 + ({b})x + ({c}) = 0")

        form = (b ** 2) - 4 * a * c

        if form < 0:
            print()
            print("Корней нет!")
            print()
            print("Нажмите клавишу --> \"enter\", что бы продолжить!")
            input()

        elif form == 0:
            print()
            x1 = (-b - sqrt(form)) / 2 * a
            xi1 = round(x1, 5)
            print(f"x = {xi1}")
            print()
            print("Нажмите клавишу --> \"enter\", что бы продолжить!")
            input()

        else:
            print()
            x1 = (-b - sqrt(form)) / 2 * a
            x2 = (-b + sqrt(form)) / 2 * a
            xi1 = round(x1, 5)
            xi2 = round(x2, 5)
            print(f"x1 = {xi1}")
            print(f"x2 = {xi2}")
            print()
            print("Нажмите клавишу --> \"enter\", что бы продолжить!")
            input()

    elif ans2 == 13:
        print()
        print("Вы выбрали пункт --> \"Тригонометрия\"!\n")
        print("Список моих функций:")
        print()
        print("|----------------------------------|")
        print("|1) Синус числа                    |")
        print("|2) Косинус числа                  |")
        print("|3) Тангенс числа                  |")
        print("|----------------------------------|")
        print()
        print("Выберите функцию (только цифра):", end=" ")
        ans3 = int(input())
        if ans3 == 1:
            print()
            print("Введите число:", end=" ")
            n3 = int(input())
            sini = sin(n3)
            sini1 = round(sini, 5)
            print()
            print(f"sin({n3}) = {sini1}")
            print()
            print("Нажмите клавишу --> \"enter\", что бы продолжить!")
            input()
        elif ans3 == 2:
            print()
            print("Введите число:", end=" ")
            n3 = int(input())
            cosi = cos(n3)
            cosi1 = round(cosi, 5)
            print()
            print(f"cos({n3}) = {cosi1}")
            print()
            print("Нажмите клавишу --> \"enter\", что бы продолжить!")
            input()
        elif ans3 == 3:
            print()
            print("Введите число:", end=" ")
            n3 = int(input())
            tani = tan(n3)
            tani1 = round(tani, 5)
            print()
            print(f"tg({n3}) = {tani1}")
            print()
            print("Нажмите клавишу --> \"enter\", что бы продолжить!")
            input()
        else:
            print()
            print("Нет такой функции ¯\_(ツ)_/¯")
            print()
            print("Нажмите клавишу --> \"enter\", что бы продолжить!")
            input()
    else:
        print()
        print("Нет такого пункта (┬┬﹏┬┬)")
        print()
        print("Нажмите клавишу --> \"enter\", что бы продолжить!")
        input()

    print()
    print("Список команд \"умного калькулятора\":")
    print()
    print("|----------------------------------|")
    print("|1) Сумма чисел                    |")
    print("|2) Вычитание чисел                |")
    print("|3) Умножение чисел                |")
    print("|4) Деление чисел                  |")
    print("|5) Возведение числа в степень     |")
    print("|6) Факториал числа                |")
    print("|7) Сумма цифр числа               |")
    print("|8) Перевод из дес. СС в двоич. СС |")
    print("|9) Перевод из дес. СС в восьм. СС |")
    print("|10) Перевод из дес. СС в шестн. СС|")
    print("|11) Корень числа                  |")
    print("|12) Решение квадр. уравнений      |")
    print("|13) Тригонометрия                 |")
    print("|14) Выход                         |")
    print("|----------------------------------|\n")
    print("Выберите пункт (только цифра):", end=" ")
    ans2 = int(input())

print()
print("Спасибо за использование данного калькулятора (●'◡'●)")
print("Нажмите клавишу --> \"enter\" для завершения программы!")

input()