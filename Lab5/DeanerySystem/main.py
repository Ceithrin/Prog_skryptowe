from day import Day
from term import Term
from lesson import Lesson
from timetable1 import Timetable1
from timetable2 import Timetable2
from break1 import Break
from basicterm import BasicTerm

term1 = Term(8, 0, Day.WED)
term2 = Term(11, 30, Day.WED)
term3 = Term(13, 30, Day.SAT)
break1 = Break(BasicTerm(9, 30, 5))
break2 = Break(BasicTerm(11, 5, 10))
break3 = Break(BasicTerm(12, 45, 5))

tt2 = Timetable2([break1, break2, break3])

less1 = Lesson(tt2, term1, 'less1', 'less1', 2)
less2 = Lesson(tt2, term2, 'less2', 'less2', 2)
less3 = Lesson(tt2, term3, 'less3', 'less3', 2)


tt2.put(less1)
tt2.put(less2)
tt2.put(less3)

print(tt2)

tt2.perform(tt2.parse(['t-', 'd-', 't+', 'd-']))

print(tt2)