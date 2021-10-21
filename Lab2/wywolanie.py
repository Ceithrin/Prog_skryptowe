import sys
import lista, slownik

user_input = ''.join(sys.argv[2:])
print(user_input)
if sys.argv[1] == '--lista':
    lista.zapisz(user_input)
    lista.wypisz()
elif sys.argv[1] == '--slownik':
    slownik.zapisz(user_input)
    slownik.wypisz()
