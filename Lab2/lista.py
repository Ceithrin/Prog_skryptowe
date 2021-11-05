

lista = []

def zapisz(user_input):
    for inp in user_input:
        flag = True
        for element in lista:
            if element[0] == inp:
                element[1] += 1
                found = False
        if flag:
            lista.append([inp, 1])


def wypisz():
    for element in lista:
        print(f"{element[0]}:{element[1]}", end = ',')