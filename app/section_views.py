from django.shortcuts import render
from django.views import View

from app.models import Course, Section
from classes.Sections.SectionClass import ConcreteSection


class SingleSection(View):
    def get(self, request):
        course_id = request.GET.get('current_course')
        section_num = request.GET.get('current_section')

        course_model = Course.objects.get(course_ID=course_id)
        section_model = Section.objects.get(course_ID=course_model, section_num=section_num)
        concrete_section = ConcreteSection(section_model)

        return render(request, 'Section.html',
                      {'section': concrete_section, 'course': course_model})

        def post(self, request):
            pass
