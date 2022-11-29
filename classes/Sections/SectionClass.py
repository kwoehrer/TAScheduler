from app.models import Section, TA, TASectionAssignments, Course
from classes.Courses import Course
import abc

class AbstractSection(abc):
    @abc.abstractmethod
    def getParentCourse(self):
        pass

    @abc.abstractmethod
    def getSectionNumber(self):
        pass
    @abc.abstractmethod
    def getSectionNumber(self):
        pass

    @abc.abstractmethod
    def getTA(self)->AbstractUser:
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
    def __init__(self, section:Section):
        self.section = section

    def getParentCourse(self)->AbstractCourse:
        return ConcreteCourse(Course.objects.get(course_ID=self.section.course_ID))

    def getSectionNumber(self):
        return self.section.section_num

    def getTA(self)->AbstractUser:
        ta_pk = TASectionAssignments.Objects.get(section_ID= self.section.ID).account_ID
        ta = TA.objects.get(account_ID=ta_pk)
        return TA_User(ta)

    def setTA(self, newTA:AbstractUser):
        if isinstance(newTA, TA_User):
            ta_id = newTA.getID()

        else:
            raise TypeError


    def getMeetTime(self):
        return self.meetTime

    def setMeetTime(self, newTime):
        self.meetTime = newTime