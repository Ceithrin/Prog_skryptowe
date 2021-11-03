from day import Day
# import regex

class Term():
    def __init__(self, hour, minute, day, duration = 90):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration
    
    def __str__(self):
        return f'{self.day}  {self.hour}:{self.minute} [{self.duration}]'

    def earlierThan(self, termin):
        if self.day.difference(termin.day) < 0:
            return False
        if self.day.difference(termin.day) == 0:
            if termin.hour < self.hour:
                return False
            if termin.hour == self.hour and termin.minute <= self.minute:
                return False
            else:
                return True
        return True

    def laterThan(self, termin):
        if self.day.difference(termin.day) > 0:
            return False
        if termin.hour > self.hour:
            return False
        if termin.hour == self.hour and termin.minute >= self.minute:
            return False
        else:
            return True

    def equals(self, termin):
        if termin.hour == self.hour and termin.minute == self.minute and termin.duration == self.duration and self.day.difference(termin.day) == 0:
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
        hour_dur = self.duration // 60
        minute_dur = self.duration % 60
        if self.minute + minute_dur > 60:
            end_hour = self.hour + hour_dur + 1
        else:
            end_hour = self.hour + hour_dur
        end_minute = (self.minute + minute_dur) % 60
        if termin.minute <= end_minute:
            new_dur = end_minute - termin.minute + (end_hour - termin.hour)*60
        else:
            new_dur = -(termin.minute - 60) + end_minute + (end_hour - termin.hour - 1)*60
        return Term(termin.hour, termin.minute, new_dur)

    def getEndTime(self):
        hour_dur = self.duration // 60
        minute_dur = self.duration % 60
        if self.minute + minute_dur > 60:
            end_hour = self.hour + hour_dur + 1
        else:
            end_hour = self.hour + hour_dur
        end_minute = (self.minute + minute_dur) % 60
        return (end_hour, end_minute)

    def printEndTime(self):
        timeTuple = self.getEndTime()
        return f'{timeTuple[0]}:{timeTuple[1]:0>2}'