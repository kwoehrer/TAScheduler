from app.models import Section, TA, TASectionAssignments, Course
from classes.Courses import Course

class ConcreteSection():
    def __init__(self, section:Section):
        ta_pk = TASectionAssignments.Objects.get(section_ID=section.ID).account_ID
        self.ta = TA.objects.get(account_ID=ta_pk)
        self.parentCourse = Course.objects.get(course_ID=section.course_ID)
        self.meetingTime = Section.MeetingTimes
        self.sectionNumber = Section.section_num

    def getParentCourse(self)->AbstractCourse:
        return ConcreteCourse(self.parentCourse)

    def getSectionNumber(self):
        return self.sectionNumber

    def getTA(self)->AbstractUser:
        return TA_User(self.ta)

    def setTA(self, newTA):
        self.ta = newTA

    def getMeetTime(self):
        return self.meetTime

    def setMeetTime(self, newTime):
        self.meetTime = newTime