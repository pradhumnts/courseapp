from django.db import models

# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.courseName

class Question(models.Model):
    question = models.TextField()
    correctAnswerIndex = models.IntegerField()
    exp = models.TextField()
    course = models.ForeignKey(Course, related_name='questions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    question = models.ManyToManyField(Question, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name