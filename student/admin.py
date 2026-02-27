from django.contrib import admin
from . import models
# Register your models here.
class Student(admin.ModelAdmin):
    list_display=('is_student','user')
admin.site.register(models.Student,Student)

class Gardian(admin.ModelAdmin):
    list_display=('user','g_1','g_2','g_3','g_4','g_5')
admin.site.register(models.Gardian,Gardian)

class Score(admin.ModelAdmin):
    list_display=('user','right_answer','wrong_answer','total_qustion','percentage')
admin.site.register(models.Score,Score)



class Result_count(admin.ModelAdmin):
    list_display=('user','right_answer','wrong_answer','total_qustion','percentage')
admin.site.register(models.Result_count,Result_count)

class Exam(admin.ModelAdmin):
    list_display=('exam_name','id')
admin.site.register(models.Exam,Exam)

class Subject(admin.ModelAdmin):
    list_display=('exam_name','subject_name','subject_code')
admin.site.register(models.Subject,Subject)

class Chapter(admin.ModelAdmin):
    list_display=('subject_code','chapter_code','chapter_name')
admin.site.register(models.Chapter,Chapter)

class Result(admin.ModelAdmin):
    list_display=('user','qustion','student_option','answer','right_answer')
admin.site.register(models.Result,Result)

class Qustion(admin.ModelAdmin):
    list_display=('chapter_code','qno','qustion','option_1','option_2','option_3','option_4','right_option')
admin.site.register(models.Qustion,Qustion)

class Feedback(admin.ModelAdmin):
    list_display=('name','feedback','email')
admin.site.register(models.Feedback,Feedback)

class Qustion_count(admin.ModelAdmin):
    list_display=('user','qustion_count')
admin.site.register(models.Qustion_count,Qustion_count)

