from django.urls import path

from group.views import student_view, detailed_student_view

urlpatterns = [
    path('', student_view),
    path('<int:id>/', detailed_student_view),
]