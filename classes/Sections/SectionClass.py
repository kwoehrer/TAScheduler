from app.models import Section, TA, Course
import classes.Courses.CoursesClass as CourseClass
import classes.Users.users as UserClass
from abc import ABC, abstractmethod


# from classes.Courses.CoursesClass import AbstractCourse, ConcreteCourse
# from classes.Users.users import AbstractUser, TAUser
# import abc

class AbstractSection(ABC):
    @ABC.abstractmethod
    def getParentCourse(self):
        pass

    @ABC.abstractmethod
    def getSectionNumber(self):
        pass

    @ABC.abstractmethod
    def setSectionNumber(self):
        pass

    @ABC.abstractmethod
    def getTA(self) -> CourseClass.AbstractUser:
        pass

    @ABC.abstractmethod
    def setTA(self, newTA):
        pass

    @ABC.abstractmethod
    def getMeetTime(self):
        pass

    @ABC.abstractmethod
    def setMeetTime(self, newTime):
        pass


class ConcreteSection(AbstractSection):
    def __init__(self, section: Section):
        self.section = section

    def getParentCourse(self) -> CourseClass.AbstractCourse:
        return CourseClass.ConcreteCourse(Course.objects.get(course_ID=self.section.course_ID))

    def getSectionNumber(self):
        return self.section.section_num

    def setSectionNumber(self, newNumber: int):
        self.section = newNumber

    def getTA(self) -> UserClass.AbstractUser:
        ta = TA.objects.get(account_ID=self.section.ta_account_id)
        return UserClass.TAUser(ta)

    def setTA(self, newTA: UserClass.AbstractUser):
        if isinstance(newTA, UserClass.TAUser):
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
