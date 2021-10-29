from day import Day
import regex

class Term():
    def __init__(self, day, hour, minute):
        self.__day = day
        self.hour = hour
        self.minute = minute
        self.duration = 90
    
    def __str__(self):
        return f'{self.__day} {self.hour}:{self.minute} [{self.duration}]'

    def earlierThan(self, termin):
        if self.__day.difference(termin._Term__day) < 0:
            return False
        if self.__day.difference(termin._Term__day) == 0:
            if termin.hour < self.hour:
                return False
            if termin.hour == self.hour and termin.minute <= self.minute:
                return False
            else:
                return True
        return True

    def laterThan(self, termin):
        if self.__day.difference(termin._Term__day) > 0:
            return False
        if termin.hour > self.hour:
            return False
        if termin.hour == self.hour and termin.minute >= self.minute:
            return False
        else:
            return True

    def equals(self, termin):
        if termin.hour == self.hour and termin.minute == self.minute and termin.duration == self.duration and self.__day.difference(termin._Term__day) == 0:
            return True
        else:
            return False

    def setTerm(self, string):
        datetab = regex.dateMatch(string)
        self.hour = datetab[3]
        self.minute = datetab[4]
        yeardiff = datetab[7] - datetab[2]
        monthdiff = datetab[6] - datetab[1]
        if yeardiff > 0:
            monthdiff += 12*yeardiff
        daydiff = datetab[5] - datetab[0]
        if monthdiff >0:
            daydiff += 30*monthdiff
        hourdiff = datetab[8] - datetab[3]
        minutediff = datetab[9] - datetab[4]
        if daydiff > 0:
            hourdiff += 24*daydiff
        if hourdiff > 0:
            minutediff += 60*hourdiff
        self.duration = minutediff
        day, name_of_day = regex.weekDay(datetab)
        self.__day = name_of_day



        

        
