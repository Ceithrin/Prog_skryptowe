from day import Day

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
        if termin.hour < self.hour:
            return False
        if termin.hour == self.hour and termin.minute <= self.minute:
            return False
        else:
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