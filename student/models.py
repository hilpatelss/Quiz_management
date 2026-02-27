from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default = False)
   
   
    
    
class Gardian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    g_1 = models.IntegerField(default=0000 )
    g_2 = models.IntegerField(default=0000 )
    g_3 = models.IntegerField(default=0000 )
    g_4 = models.IntegerField(default=0000 )
    g_5 = models.IntegerField(default=0000 )
    def __str__(self):
        return self.user 
    
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer = models.IntegerField(default=0 )
    wrong_answer = models.IntegerField( default=0 )
    total_qustion = models.IntegerField(default=0  )
    percentage = models.IntegerField(default=0  )
    
class Result_count(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer = models.IntegerField(default=0 )
    wrong_answer = models.IntegerField( default=0 )
    total_qustion = models.IntegerField(default=0  )
    percentage = models.IntegerField(default=0  )  
    
class Exam(models.Model):
    exam_name = models.CharField( max_length=50) 
    def __str__(self):
        return self.exam_name

class Subject(models.Model):
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject_name = models.CharField( max_length=200) 
    subject_code = models.CharField( unique=True ,max_length=50)
    def __str__(self):
        return self.subject_code
    
class Chapter(models.Model):
    subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter_name =models.CharField( max_length=150)
    chapter_code = models.CharField( max_length=50)
    def __str__(self):
        return self.chapter_code

       
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qustion = models.TextField()
    student_option=models.CharField(blank=True, null= True ,max_length=50)
    answer = models.CharField( max_length=50)
    right_answer =models.BooleanField(default=False)
    

class Qustion(models.Model):
    chapter_code = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    qno = models.IntegerField()
    qustion = models.TextField()
    option_1 = models.CharField( max_length=50)
    option_2 = models.CharField( max_length=50)
    option_3 = models.CharField( max_length=50)
    option_4 = models.CharField( max_length=50)
    right_option = models.CharField(blank=True, null= True, max_length=50)

class Qustion_count(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qustion_count= models.IntegerField(blank=True, null= True ,default=0)


   
class Feedback (models.Model):
    name = models.CharField(blank=True, null= True , max_length=50)
    email= models.EmailField( blank=True, null= True ,max_length=254)
    feedback = models.TextField(blank=True, null= True )
    
