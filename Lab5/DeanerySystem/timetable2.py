from typing import List
from day import Day
from term import Term
from lesson import Lesson
from action import Action
from break1 import Break
from basictimetable import BasicTimetable


class Timetable2(BasicTimetable):
    skipBreaks = False
    
    def __init__(self, breaks = []):
        self.breaks = breaks
        super().__init__()
    """ Class containing a set of operations to manage the timetable """

##########################################################
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        """
    Informs whether a lesson can be transferred to the given term

    Parameters
    ----------
    term : Term
        The term checked for the transferability
    full_time : bool
        Full-time or part-time studies

    Returns
    -------
    bool
        **True** if the lesson can be transferred to this term
    """
        if term.hour < 8 or term.hour > 20:
            return False
        
        end_time = term.getEndTime()
        if end_time[0] > 20 or (end_time[0] == 20 and end_time[1] > 0):
            return False
        

        if not self.busy(term): #jeśli termin nie zajęty
            # teraz sprawdzam warunki dla stacjo i nie i czy się zgadza nowy termin z trybem studiów
            if term.day.value > 5:
                is_full_time = False
            elif term.day.value < 5:
                is_full_time = True
            else:
                if term.hour < 17:
                    is_full_time = True
                else:
                    is_full_time = False
            
            if is_full_time == full_time:
                return True
        return False


    def overlapsBreak(self, term: Term) -> bool:
        ts = term.getStartTime()
        te = term.getEndTime()
        for bre in self.breaks:
            bs = bre.term.getStartTime()
            be = bre.term.getEndTime()
            if ts > bs and ts < be:
                return (True, bre.term.duration)
            if te > bs and te < be:
                return (True, bre.term.duration)
            if ts == bs and te > be:
                return (True, bre.term.duration)
            if ts < bs and te == be:
                return (True, bre.term.duration)
        return False
 
##########################################################

    def busy(self, term: Term) -> bool:
        """
        Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
        since there might be free term where the lesson cannot be transferred.

        Parameters
        ----------
        term : Term
            Checked term

        Returns
        -------
        bool
            **True** if the term is busy
        """
        # Term = hour, minute, day, duration=90
        if self.overlapsBreak(term):
            return True

        for lesson in list(self.lesson_dict.values()):
            if lesson.term == term:
                return True
            if lesson.term.day == term.day:
                termin_start = (term.hour, term.minute)
                termin_end = term.getEndTime()
                lesson_start = (lesson.term.hour, lesson.term.minute)
                lesson_end = lesson.term.getEndTime()
                #lesson - juz jest
                # termin - sprawdzam czy nachodzi na lesson
                if termin_start < lesson_start and termin_end > lesson_start: #
                    return True
                if termin_start == lesson_start:
                    return True
                if termin_start > lesson_start and termin_start < lesson_end:
                    return True
        return False
                
    
##########################################################

    def __str__(self):
        
        strtab = []
        timetab = []
        for lesson in list(self.lesson_dict.values()):
            timetab.append(lesson.term) # z day
        
        for bre in self.breaks:
            timetab.append(bre.term)  # bez day

        timetab = sorted(timetab, key=lambda t: t.printStartTime())
        
        #mam juz posortowane terminy
        line = '\n            ********************************************************************************************\n' #92 gwiazdki
        blank = '            *'

        for i in range(len(timetab) + 1):
            strtab.append([])
            for j in range(8):
                strtab[i].append(blank)

        for d in Day:
            strtab[0][d.value] = f'{str(d): ^12}*'  

        for counter, element in enumerate(timetab):
            strtab[counter + 1][0] = f'{element.printStartTime(): >5}-{element.printEndTime(): <6}*'

        for lesson in list(self.lesson_dict.values()):
            strtab[timetab.index(lesson.term) + 1][lesson.term.day.value] = f'{lesson.name: ^12}*'

        for bre in self.breaks:
            for i in range(1, 8):
                strtab[timetab.index(bre.term) + 1][i] = f'-------------'

        string = ''
        for i in range(len(timetab) + 1):
            for j in range(8):
                string += strtab[i][j]
            string += line


        return string