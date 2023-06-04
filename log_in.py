"""
Uloha:  Vytvorte jednoduche prihlasovacie menu v konzole. Menu by malo obsahovat vyber zo 4 moznosti: prihlasenie
        ulozeneho pouzivatela, registracia noveho pouzivatela, zmazanie existujuceho pouzivatela a ukoncenie aplikacie.
        Na ulozenie prihlasovacich mien a hesiel pouzite pole.
"""


def print_menu():
    """
    Vypis menu
    """
    print("What would you like to do?")
    print("1. -> Log in")
    print("2. -> Register new user")
    print("3. -> Delete existing user")
    print()
    print()
    print("Q -> Quit")


def execute_choice(choice, names, passwords):
    """
    Zavolanie prislusnej funkcie, na zaklade vyberu pouzivatela

    :param choice: zvolena akcia
    :param names: pole, v ktorom su ulozene prihlasovacie mena
    :param passwords: pole, v ktorom su ulozene prihlasovacie hesla
    """

    if choice == "1":
        log_in(names, passwords)
    elif choice == "2":
        register(names, passwords)
        print()
        print()
    elif choice == "3":
        delete(names, passwords)
        print()
        print()
    elif choice == "Q" or choice == "q":
        raise SystemExit
    else:
        print("Entered unknown symbol, please enter valid choice!")
        print()
        print()


def log_in(names, passwords):
    """
    Funkcia sluziacia na prihlasenie do systemu

    :param names: pole, v ktorom su ulozene prihlasovacie mena
    :param passwords: pole, v ktorom su ulozene prihlasovacie hesla
    """

    while True:
        name = input("Username: ")
        passwd = input("Password: ")

        # zistovanie, ci sa zadane meno a heslo zhoduje s ulozenymi zaznami
        if name not in names or passwd not in passwords:
            print("Entered username or password is not registered, please try again!")
            continue

        # zistenie pozicie zadaneho mena a hesla v prislusnych poliach
        index_name = names.index(name)
        index_passwd = passwords.index(passwd)

        # porovnanie ziskanych indexov, ak sa zhoduju, prihlasenie prebehlo uspene a ukonci program
        if index_name == index_passwd:
            print("Log in successful!")
            raise SystemExit
        else:
            print("Registered username is not corresponding with registered password, please try again!")


def register(names, passwords):
    """
    Registracia noveho pouzivatela

    :param names: pole, v ktorom su ulozene prihlasovacie mena
    :param passwords: pole, v ktorom su ulozene prihlasovacie hesla
    """

    names.append(input("Enter new username: "))
    passwords.append(input("Enter new password: "))
    print("New user registered successful!")


def delete(names, passwords):
    """
    Odstranenie existujuceho pouzivatela

    :param names: pole, v ktorom su ulozene prihlasovacie mena
    :param passwords: pole, v ktorom su ulozene prihlasovacie hesla
    """

    print("Which user would you like to delete?")
    name = input("Username: ")

    # zistovanie, ci sa zadane meno nachadza v prislusnom poli
    if name in names:
        position = names.index(name)
        names.pop(position)
        passwords.pop(position)
    else:
        print(name, "not found in registered users!")


# inicializacia poli
list_of_names = ["admin", "student"]
list_of_passwords = ["admin", "123"]

while True:
    print_menu()
    execute_choice(input("Enter number of desired action: "), list_of_names, list_of_passwords)
