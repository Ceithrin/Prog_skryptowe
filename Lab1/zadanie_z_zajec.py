import sys


books = dict([arg.split(':', maxsplit=1) for arg in sys.argv[1:]])

users = {}

while True:
    try:
        usr_inp = input()
        if chr(4) in usr_inp:
            break
        if usr_inp:
            inp = usr_inp.split(' ')
        if inp[0] not in users:
            users[inp[0]] = []
        print(inp)

        if inp[2] == "Zwrot":  #obsluga zwrotow
            if inp[1] in users[inp[0]]:
                books[inp[1]] = books[inp[1]] + 1
                users[inp[0]].remove(inp[1])
        elif inp[2] == "Wypozyczenie":   #obsluga wypozyczenia
            if int(books[inp[1]]) > 0:
                users[inp[0]] = users[inp[0]] + users[inp[1]]
                books[inp[1]] -= 1
            else:
                print("Ksiazka niedostepna")
    except EOFError:
        break
