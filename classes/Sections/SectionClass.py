from app.models import Section, TA, Course, TACourseAssignments
import classes.Courses.CoursesClass as CourseClass
import classes.Users.users as UserClass
from abc import ABC, abstractmethod
import abc


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
        return CourseClass.ConcreteCourse(Course.objects.get(course_ID=self.section.course_ID))

    def getSectionNumber(self):
        return self.section.section_num

    def setSectionNumber(self, newNumber: int):
        self.section = newNumber

    def getTA(self):
        ta = TA.objects.get(account_ID=self.section.ta_account_id_id)
        return UserClass.TAUser(ta)

    def setTA(self, newTA: UserClass.AbstractUser):
        if isinstance(newTA, UserClass.TAUser):
            ta_id = newTA.getID()
            self.section.ta_account_id = ta_id
            self.section.save()
            course_model = self.section.course_ID
            TACourseAssignments(course_ID=course_model, ta_id=ta_id).save()
        else:
            raise TypeError("User was not a TA but was assigned to section as a TA.")

    def getMeetTime(self) -> str:
        return self.section.MeetingTimes

    def setMeetTime(self, new_meeting_time: str):
        if len(new_meeting_time) > 50:
            raise ValueError("Meeting time must be below 50 chars")

        self.section.MeetingTimes = new_meeting_time
        self.section.save()
