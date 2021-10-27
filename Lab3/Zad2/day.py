from enum import Enum
from typing import no_type_check_decorator

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

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

result = Day.MON.difference(Day.SUN)
print(result)