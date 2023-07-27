from django.shortcuts import render, get_object_or_404
from .models import Courses
from .forms import ContactCourse

def index(request):
    courses = Courses.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

def details(request, slug):
    courses = get_object_or_404(Courses, slug=slug)
    context = {}
    if request.method == 'POST':
        forms = ContactCourse(request.POST)
        if forms.is_valid():
            context['is_valid'] = True
            forms = ContactCourse(courses)
    else:
        forms = ContactCourse()
    context['forms'] = forms
    context['course'] = courses
    template_name = 'courses/details.html'
    return render(request, template_name, context)

# def details(request, pk):
#     course= get_object_or_404(Courses, pk=pk)
#     context = {
#         'course': course
#     }
#     template_nome = 'courses/details.html'
#     return render(request, template_nome, context)