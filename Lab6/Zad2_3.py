import sys,re
from functools import reduce

'''
sys.argv[1:]  # nazwy plików
lambda y : open(y, 'r').read  #otwieram plik i go czytam

b = sys.argv[1:]
print(b)
c = list(map(lambda y : open(y, 'r').read(), sys.argv[1:]))
print(c)
a = reduce(lambda a, b: a + b, list(map(lambda y : open(y, 'r').read(), sys.argv[1:]))) # wykonuję tę funkcję dla każdego pliku i mam listę?
print(a) # ?????????????????????
d = re.findall(r'[0-9]+', reduce(lambda a, b: a + b, list(map(lambda y : open(y, 'r').read(), sys.argv[1:]))))
print(d)
e = list(map(int, re.findall(r'[0-9]+', reduce(lambda a, b: a + b, list(map(lambda y : open(y, 'r').read(), sys.argv[1:]))))))
print(e)
'''
print(len(list(filter(lambda x: x % 2 == 0, iter(map(int, re.findall(r'[0-9]+', reduce(lambda a, b: a + b, list(map(lambda y : open(y, 'r').read(), sys.argv[1:]))))))))))



