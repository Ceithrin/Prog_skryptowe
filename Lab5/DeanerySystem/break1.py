from basicterm import BasicTerm

class Break:
    def __init__(self, term):
        self.__term = term

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        if type(value) is not BasicTerm:
            raise TypeError('termin musi być obiektem klasy \"BasicTerm\"')
        else:
            self.__term = value

    def __str__(self):
        return "Przerwa"

    def getTerm(self):
        return self.__term