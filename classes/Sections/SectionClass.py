from app.models import Section, TA, Course
import classes.Courses.CoursesClass as CourseClass
from abc import ABC
import abc

from classes.Users.users import TAUser, AbstractUser


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
    def getTA(self) -> AbstractUser:
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
        CourseClass.ConcreteCourse(Course.objects.get(course_ID=self.section.course_ID))

    def getSectionNumber(self):
        return self.section.section_num

    def getTA(self) -> AbstractUser:
        ta = TA.objects.get(account_ID=self.section.ta_account_id)
        return TAUser(ta)

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
