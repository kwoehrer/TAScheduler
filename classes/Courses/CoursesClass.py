import abc
from abc import ABC

import classes.Sections.SectionClass as Sections
from app.models import Course, Instructor, InstructorAssignments, TACourseAssignments, TA, Section
from classes.Users.users import AbstractUser, InstructorUser, TAUser


class AbstractCourse(ABC):
    @abc.abstractmethod
    def get_course_id(self):
        pass

    @abc.abstractmethod
    def get_course_name(self):
        pass

    @abc.abstractmethod
    def set_course_name(self, course_name):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass

    @abc.abstractmethod
    def set_description(self, description):
        pass

    @abc.abstractmethod
    def get_credits(self):
        pass

    @abc.abstractmethod
    def set_credits(self, credit):
        pass

    @abc.abstractmethod
    def get_semester(self):
        pass

    @abc.abstractmethod
    def set_semester(self, semester):
        pass

    @abc.abstractmethod
    def get_year(self):
        pass

    @abc.abstractmethod
    def set_year(self, year):
        pass

    @abc.abstractmethod
    def get_instructors(self):
        pass

    @abc.abstractmethod
    def add_instructor(self, instructor):
        pass

    @abc.abstractmethod
    def remove_instructor(self, instructor):
        pass

    @abc.abstractmethod
    def get_tas(self):
        pass

    @abc.abstractmethod
    def add_ta(self, ta):
        pass

    @abc.abstractmethod
    def remove_ta(self, ta):
        pass

    @abc.abstractmethod
    def get_sections(self):
        pass

    @abc.abstractmethod
    def add_section(self, section):
        pass

    @abc.abstractmethod
    def remove_section(self, section):
        pass



class ConcreteCourse(AbstractCourse):

    def __init__(self, course: Course):
        self.course = course

    def get_course_id(self) -> int:
        return self.course.course_ID

    def get_course_name(self) -> str:
        return self.course.name

    def set_course_name(self, course_name: str):
        if isinstance(course_name, str):
            if len(course_name) <= 30:
                self.course.name = course_name
                self.course.save()
            else:
                raise ValueError("The name is too long")
        else:
            raise TypeError("Input is not string")

    def get_description(self) -> str:
        return self.course.description

    def set_description(self, description: str):
        self.course.description = description
        self.course.save()

    def get_credits(self) -> int:
        return self.course.credits

    def set_credits(self, credit: int):
        if 9 >= credit >= 1:
            self.course.credits = credit
            self.course.save()
        else:
            raise ValueError("Incorrect credits provided, should be 9 >= credit >= 1")

    def get_semester(self) -> str:
        return self.course.semester

    def set_semester(self, semester: str):
        if semester not in Course.SemesterTypes:
            raise ValueError("Incorrect semester type provided to course")

        self.course.semester = semester
        self.course.save()

    def get_year(self) -> int:
        return self.course.year

    def set_year(self, year: int):
        if (2022 + 10) >= year >= (2022 - 10):
            self.course.year = year
            self.course.save()
        else:
            raise ValueError("No more than 10 years after this year should be included")


    def get_instructors(self) -> []:
        instructors = InstructorAssignments.objects.filter(course_ID=self.course.course_ID)
        instr_pk_list = instructors.values_list('account_ID', flat=True)
        instr_table = Instructor.objects.filter(account_ID__instructor__in=instr_pk_list)


        result_list = []

        for instr in instr_table:
            result_list.append(InstructorUser(instr))

        return result_list


    def add_instructor(self, newInstructor):
        if isinstance(newInstructor, InstructorUser):
            instr_id = newInstructor.getID()
            new_instructor_model = Instructor.objects.get(account_ID__account_ID=instr_id)
            row = InstructorAssignments(account_ID=new_instructor_model, course_ID=self.course)
            row.save()
        else:
            raise TypeError("newInstructor was not an instructor object.")

    def remove_instructor(self, instructor):
        if isinstance(instructor, InstructorUser):
            instr_id = instructor.getID()
            old_instructor_model = Instructor.objects.get(account_ID__account_ID=instr_id)
            row = InstructorAssignments.objects.get(account_ID=old_instructor_model, course_ID=self.course).delete()
        else:
            raise TypeError("newInstructor was not an instructor object.")

    def get_tas(self) -> []:
        ta_models = TACourseAssignments.objects.filter(course_ID=self.course.course_ID)
        ta_pk_list = ta_models.values_list('account_ID', flat=True)
        ta_table = TA.objects.filter(account_ID__ta__in=ta_pk_list)

        result_list = []
        for ta in ta_table:
            result_list.append(TAUser(ta))

        return result_list

    def add_ta(self, newta):
        if isinstance(newta, TAUser):
            ta_id = newta.getID()
            row = TACourseAssignments(account_ID=TA.objects.get(account_ID__account_ID=ta_id), course_ID=self.course)
            row.save()
        else:
            raise TypeError("New TA was not a TA_User.")

    def remove_ta(self, oldta: AbstractUser) -> bool:
        if isinstance(oldta, TAUser):
            ta_id = oldta.getID()
            TACourseAssignments.objects.filter(account_ID=ta_id, course_ID=self.course_ID).delete()
        else:
            raise TypeError("Old TA was not a TA_User.")

    def get_sections(self) -> []:
        section_table = list(Section.objects.filter(course_ID=self.course))
        section_list = []

        for section in section_table:
            section_list.append(Sections.ConcreteSection(section))

        return section_list

    # Factory method, creates a section related to this course.
    def add_section(self, sectionTA_ID: int, sectionNumber: int, MeetingTimes: str):
        if len(TA.objects.filter(account_ID=sectionTA_ID)) != 1:
            raise ValueError("TA Id was not a valid TA ID.")

        for sec in self.get_sections():
            if int(sectionNumber) == int(sec.getSectionNumber()):
                raise ValueError("duplicate course section numbers.")

        ta_obj = TA.objects.get(account_ID=sectionTA_ID)
        self.add_ta(TAUser(ta_obj))

        newSection = Section(course_ID=self.course, section_num=sectionNumber, MeetingTimes=MeetingTimes,
                             ta_account_id=ta_obj)
        newSection.save()
        
    def remove_section(self, section: Sections.AbstractSection) -> bool:
        if isinstance(section, Sections.ConcreteSection):
            section_id = section.getSectionNumber()
            Section.objects.filter(course_ID=self.course.course_ID, section_num=section_id).delete()
        else:
            raise ValueError("Section is not included, cannot be deleted")
