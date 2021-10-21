# print('Ładowanie modułu "{0}"'.format(__name__))
# ############################################
# def wypisz():
#     print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
# ############################################
# print('Załadowano moduł "{0}"'.format(__name__))

slownik = {}

def zapisz(user_input):
    for inp in user_input:
        if inp in slownik.keys():
            slownik[inp] += 1
        else:
            slownik[inp] = 1


def wypisz():
    for element in slownik:
        print(f"{element}:{slownik[element]}", end = ',')
