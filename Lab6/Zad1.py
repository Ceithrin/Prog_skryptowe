from inspect import signature

def argumenty(dargs): #pobiera argumenty funkcji dekorującej podane w dekoratorze
        def wynik(funkcja): #pobiera funkcję dekorowaną
            def wrapper(*args):
                par_number = len(list(signature(funkcja).parameters)) #[pobieram liczbę argumentow konieczną dla oryginalnej funkcji]
                # print(par_number)
                # print(args)
                final_args = list(args) #zmienna będzie przechowywać finalną liczbę argumentow, na razie są tam tylko argumenty funkcji oryginalnej
                max_num = len(final_args) + len(dargs) #dargs = 2

                # wymagany w zadaniu TypeError jak za mało podanych arg i w funkcji i w dekoratorze
                if max_num < par_number:
                    raise TypeError(f'{funkcja.__name__} takes exactly {par_number - 1} arguments ({max_num - 1} given)')

                ctr = 0
                while len(final_args) < par_number:
                    final_args.append(dargs[ctr])
                    ctr += 1

                funkcja(*final_args)

                try:
                    return dargs[ctr]
                except:
                    return None
            return wrapper
        return wynik 






class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    def __setitem__(self, key, value):
        if(key == "suma"):
            self.argumentySuma = value
        elif(key == "roznica"):
            self.argumentyRoznica = value

    @argumenty(argumentySuma)
    def suma(self, a,b,c):
        print(f'{a} + {b} + {c} = {a + b + c}')

    @argumenty(argumentyRoznica)
    def roznica(self, x,y):
        print(f'{x} - {y} = {x - y}')


if __name__ == '__main__':
    op=Operacje()
    op.suma(1,2,3) #Wypisze: 1+2+3=6
    op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
    try:
        op.suma()  # TypeError: suma() takes exactly 3 arguments (2 given)
    except Exception as exc:
        print(exc) 
    op.roznica(2,1) #Wypisze: 2-1=1
    op.roznica(2) #Wypisze: 2-4=-2
    wynik = op.roznica() #Wypisze: 4-5=-1
    print(wynik) #Wypisze: 6

    #Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma']=[1,2]
    #oznacza, że   argumentySuma=[1,2]
    print(op.argumentySuma)

    #Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica']=[1,2,3]
    #oznacza, że   argumentyRoznica=[1,2,3]
    print(op.argumentyRoznica)