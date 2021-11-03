from day import Day
from term import Term

class Lesson():
    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.full_time = self.setFTValue()

    def setFTValue(self):
        if self.term.day.value < 5:
            return True
        elif self.term.day.value > 5:
            return False
        else:
            if self.term.hour < 17:
                return True
            else:
                return False
        

    def earlierDay(self):
        new_day_value = self.term.day.value - 1

        if new_day_value < 1:
            return False
        
        if self.full_time: # stacjoarne
            if new_day_value == 5:
                if self.term.hour >= 17:
                    return False
            if new_day_value in [6, 7]:
                return False
            else:
                new_day = Day(new_day_value)
                self.term.day = new_day
                return True
        else: #weekendowe
            if new_day_value == 5:
                if self.term.hour <= 17:
                    return False
            if new_day_value in [1, 2, 3, 4]:
                return False
            else:
                new_day = Day(new_day_value)
                self.term.day = new_day
                return True

    def laterDay(self):
        new_day_value = self.term.day.value + 1

        if new_day_value > 7:
            return False
        
        if self.full_time: # stacjoarne
            if new_day_value == 5:
                if self.term.hour >= 17:
                    return False
            if new_day_value in [6, 7]:
                return False
            else:
                new_day = Day(new_day_value)
                self.term.day = new_day
                return True
        else: #weekendowe
            if new_day_value == 5:
                if self.term.hour <= 17:
                    return False
            if new_day_value in [1, 2, 3, 4]:
                return False
            else:
                new_day = Day(new_day_value)
                self.term.day = new_day
                return True

    def ealierTime(self):
        hour_dur = self.term.duration // 60
        minute_dur = self.term.duration % 60
        if self.term.minute - minute_dur < 0:
            start_hour = self.term.hour - hour_dur - 1
        else:
            start_hour = self.term.hour - hour_dur
        start_minute = (self.term.minute - minute_dur) % 60
        
        if start_hour < 8:
            return False
        if not self.full_time: #weekendowe
            if self.term.day.value == 5:
                if start_hour < 17:
                    return False
        self.term.hour = start_hour
        self.term.minute = start_minute 
        return True 


    def laterTime(self):
        hour_dur = self.term.duration // 60
        minute_dur = self.term.duration % 60
        if self.term.minute + minute_dur > 60:
            end_hour = self.term.hour + hour_dur + 1
        else:
            end_hour = self.term.hour + hour_dur
        end_minute = (self.term.minute + minute_dur) % 60
        self.term.hour = end_hour
        self.term.minute = end_minute

        if end_hour > 20:
            return False
        if self.full_time: #stacjo
            if self.term.day.value == 5:
                if end_hour > 17:
                    return False
        self.term.hour = end_hour
        self.term.minute = end_minute 
        return True 

    def __str__(self):
        if self.year == 1:
            year_str = 'Pierwszy rok'
        elif self.year == 2:
            year_str = 'Drugi rok'
        elif self.year == 3:
            year_str = 'Trzeci rok'
        elif self.year == 4:
            year_str = 'Czwarty rok'
        elif self.year == 5:
            year_str = 'Piąty rok'

        if self.full_time:
            time_str = 'stacjonarnych'
        else:
            time_str = 'niestacjonarnych'

        return (f'{self.name} ({self.term.day} {self.term.hour}:{self.term.minute}-{self.term.printEndTime()})\n'
                f'{year_str} studiów {time_str}\n'
                f'Prowadzący: {self.teacherName}')

lesson = Lesson(Term(9, 35, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2)
print(lesson)

