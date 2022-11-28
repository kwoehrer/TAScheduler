class CoursesClass:

    def __init__(self, course_id, course_name, description, credit, semester, year):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description
        self.credits = credit
        self.semester = semester
        self.year = year
        self.instructor = None
        self.ta = []
        self.section = []

    def get_course_id(self):
        return self.course_id

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_credits(self):
        return self.credits

    def set_credits(self, credit):
        self.credits = credit

    def get_semester(self):
        return self.semester

    def set_semester(self, semester):
        self.semester = semester

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_instructor(self):
        return self.instructor

    def set_instructor(self, instructor):
        self.instructor = instructor

    def get_tas(self):
        return self.ta

    def add_ta(self, ta):
        self.ta.append(ta)

    def remove_ta(self, ta):
        if ta in self.ta:
            self.ta.remove(ta)

    def get_section(self):
        return self.section

    def add_section(self, section):
        self.section.append(section)

    def remove_section(self, section):
        if section in self.section:
            self.section.remove(section)




