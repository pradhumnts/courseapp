from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

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
    subject = models.CharField(max_length=100, blank=True)
    topic = models.CharField(max_length=100, blank=True)
    course = models.ForeignKey(Course, related_name='questions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(MPTTModel):

    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    question = models.ManyToManyField(Question, related_name='categories', blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    isMainCategory = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Child(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='child', on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    siblings = models.ManyToManyField("self")

    def __str__(self):
        return self.title


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
        
    class MPTTMeta:
        order_insertion_by = ['name']