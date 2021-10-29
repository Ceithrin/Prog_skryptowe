from enum import Enum


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def __str__(self):
        if self.value == 1:
            day_name = 'Poniedziałek'
        elif self.value == 2:
            day_name = 'Wtorek'
        elif self.value == 3:
            day_name = 'Środa'
        elif self.value == 4:
            day_name = 'Czwartek'
        elif self.value == 5:
            day_name = 'Piątek'
        elif self.value == 6:
            day_name = 'Sobota'
        elif self.value == 7:
            day_name = 'Niedziela'

        return day_name

    def difference(self, day):
        # print(day.value)
        # print(self.value)
        # print(day.value - self.value)
        diff = day.value - self.value
        if diff > 3:
            return diff - 7
        elif diff < -3:
            return diff + 7
        else:
            return diff



def nthDayFrom(n, day):
    nthDay = n + day.value
    if nthDay > 7:
        nthDay -= 7
        return Day(nthDay)
    elif nthDay < 1:
        nthDay += 7
        return Day(nthDay)
    else:
        return Day(nthDay)

if __name__ == "__main__":
    result = Day.MON.difference(Day.SUN)
    print(result)