import sys
import getopt
import lista, slownik

opt, numbers = getopt.getopt(sys.argv[1:], '', ['modul='])
numbers = ''.join(numbers)
if opt[0][1] == 'lista':
    lista.zapisz(numbers)
    lista.wypisz()
elif opt[0][1] == 'slownik':
    slownik.zapisz(numbers)
    slownik.wypisz()
