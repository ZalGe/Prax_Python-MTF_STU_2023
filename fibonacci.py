"""
Uloha:  Vytvorte funkciu, ktora vypise fibonacciho postupnost, dlzka postupnosti je zadavana pouzivatelom
        z klavesnice.
"""


def print_fibonacci(leng):
    """
    Funkcia na vypis fibonacciho postupnosti

    :param leng: dlzka postupnosti
    """

    # zaciatocne hodnoty fibonacciho postupnosti a ich ulozenie do pola
    a = 0
    b = 1
    arr = [a, b]

    # cyklus, pomocou ktoreho pocitame dalsi prvok postupnosti a jeho nasledne ulozenie do pola
    for i in range(leng - 2):
        tmp = a + b
        a = b
        b = tmp
        arr.append(b)

    print(arr)      # vypis pola


length = int(input("Enter number of elements to print: "))      # dlzka postupnosti zadavana z klavesnice
print_fibonacci(length)     # volanie funkcie
