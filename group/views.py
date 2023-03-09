from django.http import HttpResponse, Http404
from .models import Student


def first_view(request):
    html = '<html><body><h1>John Snow</h1></body></html>'
    return HttpResponse(bytes(html, 'utf-8'))


def student_view(request):
    qs = Student.objects.all()
    html = ''.join(f'<h3>{stud}</h3>' for stud in qs)
    return HttpResponse(html)


def detailed_student_view(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('Student Not Found')
    return HttpResponse(f'<h2>{student}</h2><p>{student.contacts} -- {student.passport}</p>')


def index(request):
    return HttpResponse('<h1>hELOO</h1>')
