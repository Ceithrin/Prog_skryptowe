import sys
import warnings


def list(dict):
    for arg in dict:
        print(arg, dict[arg])
    

def Zwrot(data, users, books):
    if data[1] in users[data[0]]:
        books[data[1]] = books[data[1]] + 1
        users[data[0]].remove(data[1])
    else:
        warnings.warn("Uzytkownik nie moze zwrocic ksiazki ktorej nie posiada")
        return None


def Wypozyczenie(data, users, books):
    if data[1] not in books:
        print("Dana ksiazka nie istnieje")
        return False
    elif int(books[data[1]]) > 0:
        users[data[0]].append(data[1])
        books[data[1]] -= 1
    else:
        print("Ksiazka niedostepna")
        return None


def dictionary(args):
    a = dict([arg.split(':') for arg in args])
    for arg in a:
        a[arg] = int(a[arg])
    return a


books = dictionary(sys.argv[1:])


users = {}

if __name__ == "__main__":
    while True:
        try:
            usr_inp = input()
            if chr(4) in usr_inp:
                break
            if usr_inp:
                data = usr_inp.split(' ')
            if data[0] not in users:
                users[data[0]] = []
            if data[2] == "Z":  #obsluga zwrotow
                Zwrot(data, users, books)
            elif data[2] == "W":   #obsluga wypozyczenia
                Wypozyczenie(data, users, books)
        except EOFError:
            break


list(books)
for arg in users:
    print(f"{arg} posiada:")
    for book in users[arg]:
        print(book, end = ' ')