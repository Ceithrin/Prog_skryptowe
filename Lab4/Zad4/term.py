from day import Day
# import regex

class Term():
    def __init__(self, hour, minute, day, duration=90):
        self.__hour = hour
        self.__minute = minute
        self.__day = day
        self.__duration = duration

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        if type(value) is not int:
            raise TypeError('Godzina musi być typu int')
        elif value < 0 or value > 23:
            raise ValueError('Godzina musi być w przedziale od 0 do 23')
        else:
            self.__hour = value

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if type(value) is not int:
            raise TypeError('Minuty muszą być typu int')
        elif value < 0 or value > 59:
            raise ValueError('Minuty muszą być w przediale 0 - 59')
        else:
            self.__minute = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if type(value) is not Day:
            raise TypeError('Dzień musi być typu \'Day\'')
        else:
            self.__day = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if type(value) is not int:
            raise TypeError('Czas trwania musi być typu int')
        elif value <=0:
            raise ValueError('Czas trwania musi być dodatni')
        else:
            self.__duration = value
    
    def __str__(self):
        return f'{self.day}  {self.hour}:{self.minute} [{self.duration}]'

    def earlierThan(self, termin):
        if self.__day.difference(termin.day) < 0:
            return False
        if self.__day.difference(termin.day) == 0:
            if termin.hour < self.__hour:
                return False
            if termin.hour == self.__hour and termin.minute <= self.__minute:
                return False
            else:
                return True
        return True

    def laterThan(self, termin):
        if self.__day.difference(termin.day) > 0:
            return False
        if termin.hour > self.__hour:
            return False
        if termin.hour == self.__hour and termin.minute >= self.__minute:
            return False
        else:
            return True

    def equals(self, termin):
        if termin.hour == self.__hour and termin.minute == self.__minute and termin.duration == self.__duration and self.__day.difference(termin.day) == 0:
            return True
        else:
            return False

    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __gt__(self, termin):
        return self.laterThan(termin)

    def __eq__(self, termin):
        return self.equals(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)

    def __sub__(self, termin):
        new_dur = 0
        hour_dur = self.__duration // 60
        minute_dur = self.__duration % 60
        if self.__minute + minute_dur > 60:
            end_hour = self.__hour + hour_dur + 1
        else:
            end_hour = self.__hour + hour_dur
        end_minute = (self.__minute + minute_dur) % 60
        if termin.minute <= end_minute:
            new_dur = end_minute - termin.minute + (end_hour - termin.hour)*60
        else:
            new_dur = -(termin.minute - 60) + end_minute + (end_hour - termin.hour - 1)*60
        return Term(termin.hour, termin.minute, new_dur)

    def getEndTime(self):
        hour_dur = self.__duration // 60
        minute_dur = self.__duration % 60
        if self.__minute + minute_dur >= 60:
            end_hour = self.__hour + hour_dur + 1
        else:
            end_hour = self.__hour + hour_dur
        end_minute = (self.__minute + minute_dur) % 60
        return (end_hour, end_minute)

    def printEndTime(self):
        timeTuple = self.getEndTime()
        return f'{timeTuple[0]}:{timeTuple[1]:0>2}'

    def printStartTime(self):
        return f'{self.__hour:0>2}:{self.__minute:0>2}'
