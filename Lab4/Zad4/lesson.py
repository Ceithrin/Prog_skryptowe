from day import Day
from term import Term
from teacher import Teacher



class Lesson():
    def __init__(self, timetable, term, name, year, teacher=None):
        self.__timetable = timetable
        self.__term = term
        self.__name = name
        self.__year = year
        self.__teacher = teacher
        self.__full_time = self.setFTValue()

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

    @property
    def timetable(self):
        return self.__timetable

    @timetable.setter
    def timetable(self, value):
        from timetable1 import Timetable1
        if type(value) is not Timetable1:
            raise TypeError('timetable musi być typu \'Timetable1\'')
        else:
            self.__timetable = value

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        if type(value) is not Term:
            raise TypeError('term musi być typu \'Term\'')
        else:
            self.__term = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name musi być typu \'str\'')
        else:
            self.__term = value

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, value):
        if type(value) is not str:
            raise TypeError('teacherName musi być typu \'str\'')
        else:
            self.__teacherName = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if type(value) is not int:
            raise TypeError('rok musi być typu int')
        elif value <= 0:
            raise ValueError('rok musi być dodatni')
        else:
            self.__year = value

    @property
    def full_time(self):
        return self.__full_time
        

    def earlierDay(self):
        new_day_value = self.__term.day.value - 1

        if new_day_value < 1:
            return False
        
        new_term = Term(self.__term.hour, self.__term.minute, Day(new_day_value))

        if not self.__timetable.can_be_transferred_to(new_term, self.__full_time):
            return False

        self.__term.day = Day(new_day_value)
        return True

    def laterDay(self):
        new_day_value = self.term.day.value + 1

        if new_day_value > 7:
            return False
        
        new_term = Term(self.__term.hour, self.__term.minute, Day(new_day_value))

        if not self.__timetable.can_be_transferred_to(new_term, self.__full_time):
            return False

        self.__term.day = Day(new_day_value)
        return True

    def earlierTime(self):
        hour_diff = self.term.duration // 60
        minute_diff = self.term.duration % 60
        if self.__term.minute - minute_diff < 0:
            minute_diff -= 60 # może być ujemna
            hour_diff += 1
        
        new_term = Term(self.__term.hour - hour_diff, self.__term.minute - minute_diff, self.__term.day)

        if not self.timetable.can_be_transferred_to(new_term, self.full_time):
            return False

        self.__term.hour -= hour_diff
        self.__term.minute -= minute_diff
        return True


    def laterTime(self):
        hour_diff = self.term.duration // 60
        minute_diff = self.term.duration % 60
        if self.__term.minute + minute_diff >= 60:
            minute_diff -= 60 # może być ujemna
            hour_diff += 1
        
        new_term = Term(self.__term.hour + hour_diff, self.__term.minute + minute_diff, self.__term.day)

        if not self.timetable.can_be_transferred_to(new_term, self.full_time):
            return False

        self.__term.hour += hour_diff
        self.__term.minute += minute_diff
        return True

    def __add__(self, teacher1):
        #lesson.__add__teacher
        if self.__teacher != None:
            return self
        if teacher1.hours <= 6:
            self.__teacher = teacher1
            return self
        return self

    def __sub__(self, teacher1):
        self.__teacher = None
        teacher1.hours -= self.__term.duration / 45
        return self
        


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
                f'Prowadzący: {self.__teacher}')


