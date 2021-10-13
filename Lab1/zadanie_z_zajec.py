import sys

def list(dict):
    for arg in dict:
        print(arg, dict[arg])



books = dict([arg.split(':', maxsplit=1) for arg in sys.argv[1:]])

for arg in books:
    books[arg] = int(books[arg])

users = {}

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
            if data[1] in users[data[0]]:
                books[data[1]] = books[data[1]] + 1
                users[data[0]].remove(data[1])
            else:
                print("Uzytkownik nie moze zwrocic ksiazki ktorej nie posiada")
        elif data[2] == "W":   #obsluga wypozyczenia
            if int(books[data[1]]) > 0:
                users[data[0]].append(data[1])
                books[data[1]] -= 1
            else:
                print("Ksiazka niedostepna")
    except EOFError:
        break
list(users)
list(books)
