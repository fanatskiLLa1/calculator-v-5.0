import sys
from math import factorial

print("Автор - fanat skiLLa1")
print()
print("Здравствуйте, вас приветствует \"умный калькулятор!\" (v 2.0)\n")
print("|======================================================|")
print("|P.s: весь текст нужно писать с маленькой буквы!       |")
print("|======================================================|\n")

print("Вы хотите воспользоваться программой? (да\нет):", end=" ")

ans1 = input()

if ans1 == "нет":
    sys.exit()

elif ans1 == "да":
    print()

else:
    sys.exit()

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
print("|----------------------------------|\n")

print("Выберите пункт (только цифра):", end=" ")

ans2 = int(input())

if ans2 == 1:
    print()
    print("Вы выбрали пункт --> \"сумма чисел\"!\n")
    print("Введите первое число:", end=" ")
    n1 = float(input())
    print("Введите второе число:", end=" ")
    n2 = float(input())
    summa = n1 + n2
    print()
    print(f"{n1} + {n2} = {summa}")

elif ans2 == 2:
    print()
    print("Вы выбрали пункт --> \"вычитание чисел\"!\n")
    print("Введите первое число:", end=" ")
    n1 = float(input())
    print("Введите второе число:", end=" ")
    n2 = float(input())
    unsumma = n1 - n2
    print()
    print(f"{n1} - {n2} = {unsumma}")

elif ans2 == 3:
    print()
    print("Вы выбрали пункт --> \"умножение чисел\"!\n")
    print("Введите первое число:", end=" ")
    n1 = float(input())
    print("Введите второе число:", end=" ")
    n2 = float(input())
    mult = n1 * n2
    print()
    print(f"{n1} * {n2} = {mult}")

elif ans2 == 4:
    print()
    print("Вы выбрали пункт --> \"деление чисел\"!\n")
    print("Введите первое число:", end=" ")
    n1 = float(input())
    print("Введите второе число:", end=" ")
    n2 = float(input())
    unmult = n1 / n2
    print()
    print(f"{n1} : {n2} = {unmult}")

elif ans2 == 5:
    print()
    print("Вы выбрали пункт --> \"возведение числа в степень\"!\n")
    print("Введите число:", end=" ")
    n1 = float(input())
    print("Введите степень:", end=" ")
    n2 = int(input())
    stepi = n1 ** n2
    print()
    print(f"{n1} ** {n2} = {stepi}")

elif ans2 == 6:
    print()
    print("Вы выбрали пункт --> \"факториал числа\"!\n")
    print("Введите число:", end=" ")
    n1 = int(input())
    fact = factorial(n1)
    print()
    print(f"{n1}! = {fact}")

elif ans2 == 7:
    print()
    print("Вы выбрали пункт --> \"сумма цифр числа\"!\n")
    print("Введите число:", end=" ")
    n1 = int(input())
    summa = 0
    while n1 != 0:
        digit = n1 % 10
        summa = summa + digit
        n1 = n1 // 10
    print()
    print(f"Сумма цифр числа = {summa}")

elif ans2 == 8:
    print()
    print("Вы выбрали пункт --> \"перевод из дес. СС в двоич. СС\"!\n")
    print("Хорошо. Введите число:", end=" ")
    n = int(input())
    bini = bin(n)[2:]
    print()
    print(f"{n}\u2081\u2080 = {bini}\u2082")

elif ans2 == 9:
    print()
    print("Вы выбрали пункт --> \"перевод из дес. СС в восьм. СС\"!\n")
    print("Вау!. Хороший выбор. Вводите число:", end=" ")
    n = int(input())
    octi = oct(n)[2:]
    print()
    print(f"{n}\u2081\u2080 = {octi}\u2088")

elif ans2 == 10:
    print()
    print("Вы выбрали пункт --> \"перевод из дес. СС в шестн. СС\"!\n")
    print("Ничего себе!. Отличный выбор. Пишите число:", end=" ")
    n = int(input())
    hexi = hex(n)[2:]
    print()
    print(f"{n}\u2081\u2080 = {hexi}\u2081\u2086")

else:
    print()
    print("Нет такого пункта (┬┬﹏┬┬)")

print()
print("Спасибо за использование данного конвертера (●'◡'●)")
print("Нажмите клавишу --> \"enter\" для завершения программы!")

input()