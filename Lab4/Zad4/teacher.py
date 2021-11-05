from day import Day
from term import Term
from action import Action


class Teacher():
    
    def __init__(self, name, surname, hours=0):
        self.name = name
        self.surname = surname
        self.hours = hours

    def __str__(self):
        return f'{self.name} {self.surname}'