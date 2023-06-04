"""
Uloha:  Vygenerujte pole nahodnych celych cisiel, vyhladajte v nom prvocisla a zistite pocet ich opakovani
"""


import random   # modul, pomocou ktoreho generujeme nahodne cisla


def generate_array_of_integers(arr, length, max_range):
    """
    Funkcia generuje nahodne cisla a uklada ich do pola

    :param arr: pole, do ktoreho ukladame vygenerovane cisla
    :param length: dlzka pola
    :param max_range: maximalna hodota vygenerovanych cisiel
    """

    for i in range(length):
        arr.append(random.randint(0, max_range))


def prime_number_selector(arr_generated, arr_prime):
    """
    Funkcia, ktora vyhladava prvocisla v danom poli

    :param arr_generated: pole, z ktoreho cita dane cisla
    :param arr_prime: pole, do ktoreho uklada prvocisla
    """

    for number in arr_generated:
        is_prime = True     # premenna, pomocou ktorej vieme identifikovat, ci cislo je prvocislo
        if number < 2:      # cisla 0 a 1 vylucime z vyhladavania, kedze sa nejedna o prvocisla
            is_prime = False
        else:
            for i in range(2, int(number ** 0.5) + 1):      # Zistujeme, ci je cislo delitelne cislami v intervale <2 ; odmocnina z daneho cisla>
                if number % i == 0:     # pokial je cislo delitelne cislom z daneho intervalu, nejedna sa o prvocislo
                    is_prime = False
                    break

        if is_prime:    # ak sa nezmenila hodnota premennej 'is_prime', tak sa jedna o prvocislo a je ulozene do pola
            arr_prime.append(number)


def number_histogram(arr_prime, arr_hist):
    """
    Funkcia, na zistenie pocetnosti jednotlivych prvocisel

    :param arr_prime: pole, v ktorom su ulozene prvocisla
    :param arr_hist: pole, do ktoreho uklada pocetnost prvocisel
    """

    arr_prime.sort()        # zoradenie pola od najmensieho po najvacsie

    for i in range(len(arr_prime)):     # vyber prvku z pola
        count = 1

        for j in range(i + 1, len(arr_prime) - 1):      # prechadzanie pola
            if arr_prime[i] == arr_prime[j] and arr_prime[i] != '\0':       # zistovanie duplicit vybraneho prvku pri prechadzani pola
                count += 1
                arr_prime[j] = '\0'     # vymazanie duplicit z pola

        if arr_prime[i] != '\0':        # zistovanie, ci vybrany prvok neznaci koniec pola
            arr_hist.append(str(arr_prime[i]) + " -> " + str(count))        # ulozenie zaznamu do pola vo forme 'prvocislo -> jeho pocet'


# inicializacia poli
array_of_numbers = []
array_of_prime_numbers = []
histogram_of_prime_numbers = []

# volanie jednotlivych funkcii a nasledny vypis obsahu poli do konzoly
generate_array_of_integers(array_of_numbers, 5000, 1000)
print(array_of_numbers)
prime_number_selector(array_of_numbers, array_of_prime_numbers)
print(array_of_prime_numbers)
number_histogram(array_of_prime_numbers, histogram_of_prime_numbers)
print(histogram_of_prime_numbers)
