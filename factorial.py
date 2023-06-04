"""
Uloha:  Napiste program, ktory vypocita faktorial zadaneho cisla pomocou cyklov for a while.
"""


def for_factorial(num):
    """
    Vypocet faktorialu pomocou for cyklu

    :param num: cislo, ktoreho faktorial pocitame
    :return: vypocitany faktorial
    """

    for_fact = 1

    for i in range(num, 0, -1):
        for_fact *= i

    return for_fact


def while_factorial(num):
    """
    Vypocet faktorialu pomocou while cyklu

    :param num: cislo, ktoreho faktorial pocitame
    :return: vypocitany faktorial
    """

    while_fact = 1

    while num > 0:
        while_fact *= num
        num -= 1

    return while_fact


# nacitanie cisla a nasledny vypis jeho faktorialu
number = int(input("Enter number: "))
print("Vypocitany faktorial pomocou for cyklu: ", for_factorial(number))
print("Vypocitany faktorial pomocou while cyklu: ", while_factorial(number))