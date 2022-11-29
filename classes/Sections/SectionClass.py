class sectionClass():
    def __init__(self, currentTA, sectionNumber, parentCourse, meetTime):
        self.currentTA = currentTA
        self.sectionNumber = sectionNumber
        self.parentCourse = parentCourse
        self.meetTime = meetTime

    def getParentCourse(self):
        return self.parentCourse

    def getSectionNumber(self):
        return self.sectionNumber

    def getTA(self):
        return self.currentTA

    def setTA(self, newTA):
        self.currentTA = newTA

    def getMeetTime(self):
        return self.meetTime

    def setMeetTime(self, newTime):
        self.meetTime = newTime