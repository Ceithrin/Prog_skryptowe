import sys;
from collections import Counter;


a = ["abc", "hscidsv", "1", "1"]
'''
sys.stdin.read().split() 
#wczytuje dane z klawiatury i dzielę po białych znakach, robię z tego listę słów

lambda t: len(t) 
#funkcja anonimowa, tak jakbym zrobiła def(x): return len(x)

map(lambda t: len(t), sys.stdin.read().split())
#teraz biorę dla każdego słowa tę lambdę, czyli mam nową tablicę, z długościami słów?

# teraz testy
c = dict(Counter(map(lambda t: len(t), a)))  
print(c)

Counter - zlicza mi wystąpienia i robi słownik, a dict Usunie z outputu wyraz Counter(<słownik>) i da sam słownik
'''

import sys;from collections import Counter;print(dict(Counter(map(lambda t: len(t), sys.stdin.read().split()))))