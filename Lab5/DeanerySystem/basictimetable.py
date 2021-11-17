from typing import List
from day import Day
from term import Term
from lesson import Lesson
from action import Action
from abc import ABC, abstractmethod


class BasicTimetable(ABC):

    def __init__(self):
        self.lesson_dict = {} #wygląda tak 9:30-11:00-Poniedziałek : obiekt Lesson
    
    def put(self, lesson: Lesson) -> bool:
        """
    Add the given lesson to the timetable.

    Parameters
    ----------
    lesson : Lesson
        The added  lesson

    Returns
    -------
    bool
        **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
            """ 
        if type(lesson) is not Lesson:
            raise TypeError('Argument \'put()\' musi być obiektem klasy \'Lesson\'')
        else:
            if not self.busy(lesson.term):
                self.lesson_dict[f'{lesson.term.printStartTime()}-{lesson.term.printEndTime()}-{lesson.term.day}'] = lesson
                return True
            else:
                raise ValueError(f'Podany termin jest zajęty')

    @abstractmethod
    def busy(self, term: Term) -> bool:
        pass

    def parse(self, actions: List[str]) -> List[Action]:
        """
    Converts an array of strings to an array of 'Action' objects.

    Parameters
    ----------
    actions:  List[str]
        A list containing the strings: "d-", "d+", "t-" or "t+"

    Returns
    -------
        List[Action]
            A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
            """
        action_list = []
        values = [item.value for item in Action]
        for action in actions:
            if action in values:
                action_list.append(Action(action))
            else:
                raise ValueError(f'Translation {action} is incorrect')
        return action_list

    def perform(self, actions: List[Action]):
        """
    Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

    Parameters
    ----------
    actions : List[Action]
        Actions to be performed
            """
        counter = 0
        for action in actions:
            if action == Action.DAY_EARLIER:
                list(self.lesson_dict.values())[counter].earlierDay()
            elif action == Action.DAY_LATER:
                list(self.lesson_dict.values())[counter].laterDay()
            elif action == Action.TIME_EARLIER:
                list(self.lesson_dict.values())[counter].earlierTime()
            elif action == Action.TIME_LATER:
                list(self.lesson_dict.values())[counter].laterTime()

            counter += 1
            counter = counter % len(list(self.lesson_dict.values()))

    def get(self, term: Term) -> Lesson:
        """
    Get object (lesson) indicated by the given term.

    Parameters
    ----------
    term: Term
        Lesson date

    Returns
    -------
    lesson: Lesson
        The lesson object or None if the term is free     
        """
        lesson_termin = None
        for lesson in list(self.lesson_dict.values()):
            if lesson.term == term:
                lesson_termin = lesson
                break
        return lesson_termin
