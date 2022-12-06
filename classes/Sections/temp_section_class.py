from app.models import Section, TA, Course, User
from classes.Sections.temp_course_class import AbstractCourse, ConcreteCourse
from classes.Users.users import AbstractUser, TAUser
from abc import ABC
import abc
from django.core.exceptions import ObjectDoesNotExist


# import classes.Courses.CoursesClass as CourseClass
# import classes.Users.users as UserClass


# from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
# from classes.Users.users import AbstractUser, TAUser
# import abc

class AbstractSection(ABC):
    @abc.abstractmethod
    def getParentCourse(self):
        pass

    @abc.abstractmethod
    def getSectionNumber(self):
        pass

    @abc.abstractmethod
    def setSectionNumber(self):
        pass

    @abc.abstractmethod
    def getTA(self):
        pass

    @abc.abstractmethod
    def setTA(self, newTA):
        pass

    @abc.abstractmethod
    def getMeetTime(self):
        pass

    @abc.abstractmethod
    def setMeetTime(self, newTime):
        pass


class ConcreteSection(AbstractSection):
    def __init__(self, section: Section):
        self.section = section

    def getParentCourse(self):
        try:
            return ConcreteCourse(self.section.course_ID)
        except ObjectDoesNotExist:
            ("parent class does not exist")

    def getSectionNumber(self):
        return self.section.section_num

    def setSectionNumber(self, newNumber):
        if isinstance(newNumber, int):
            if newNumber <= 999 and newNumber >= 100:
                self.section.section_num = newNumber
            else:
                raise ValueError("new section number too long or loo short")
        else:
            raise TypeError("new section number not an integer")

    def getTA(self):
        # ta = TA.objects.get(self.section.ta_account_id)
        # return TAUser(ta)
        return TAUser(self.section.ta_account_id)

    def setTA(self, newTA: AbstractUser):
        if isinstance(newTA, TAUser):
            ta_id = newTA.getID()
            self.section.ta_account_id = ta_id
            self.section.save()

        else:
            raise TypeError("User was not a TA but was assigned to section as a TA.")

    def getMeetTime(self) -> str:
        return self.section.MeetingTimes

    def setMeetTime(self, new_meeting_time: str):
        if len(new_meeting_time) > 50:
            raise ValueError("Meeting time must be below 50 chars")

        self.section.MeetingTimes = new_meeting_time
        self.section.save()
