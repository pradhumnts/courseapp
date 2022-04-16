from django.shortcuts import render

from .models import Category, Course, Question
import json
# Create your views here.
from django.templatetags.static import static

def course(request, course_id=None):
        
    course = Course.objects.get(id=course_id)
    
    # for x in data:
    #     print(x["exp"])
    #     # Question.objects.create(question="%r" % x["question"], correctAnswerIndex=x["correctAnswerIndex"], exp="%r" % x["exp"], course=course)

    # category = Category.objects.filter(course=course)
    categories = Category.objects.filter(course=course)
    
    questions_ids = list(categories.values_list('question__id', flat=True))

    questions = []
    categories_list = []

    for x in categories:
        for question in x.question.all():
            questions.append({
                "correctAnswerIndex": question.correctAnswerIndex,
                "exp": question.exp,
                "question": question.question,
                "id": question.id
        })  

        categories_list.append(
            {
                "name": x.name, 
                "idList": questions_ids, 
                "length": len(questions_ids)
            }
        )

    data = {
        "courseName": course.courseName, 
        "courseUniqueId": course.pk, 
        "data": categories_list
    }

    data = json.dumps(data)
    q = json.dumps(questions)

    return render(request, "Homepage.html", {"data": data, "questions": questions, "q": q})

def course_list(request):
    categories = Category.objects.all()

    return render(request, "courses.html", {"categories": categories})

def index(request):
    courses = Course.objects.all()
    
    return render(request, "index.html", {"courses": courses})

def profile(request):
    return render(request, "profile.html")

def pricing(request):
    return render(request, "pricing.html")

def login(request):
    return render(request, "auth/login-basic.html")

def signup(request):
    return render(request, "auth/register-basic.html")

