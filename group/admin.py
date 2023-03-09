from django.contrib import admin

from group.models import Teacher, GroupStudents, Student, Group

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(GroupStudents)
# admin.site.register(Group)


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count', 'list_of_students',)

    def list_of_students(self, obj):
        qs = GroupStudents.objects.filter(group_id=obj)
        return [f'{x.student_id.name} {x.student_id.last_name}' for x in qs]

    def count(self, obj):
        return GroupStudents.objects.filter(group_id=obj).count()
