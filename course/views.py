from django.shortcuts import render

from .models import Category, Course
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def course(request, course_id=None):
        
    course = Course.objects.get(id=course_id)
    
    # for x in data:
    #     print(x["exp"])
    #     # Question.objects.create(question="%r" % x["question"], correctAnswerIndex=x["correctAnswerIndex"], exp="%r" % x["exp"], course=course)

    # category = Category.objects.filter(course=course)

    categories = Category.objects.filter(course=course, isMainCategory=True)

    questions = []

    subjects = []

    for x in categories:
        datalist = []

        for y in x.get_children():
            ques = []
            que_ids = []
            my_categories = []
        
            for z in y.question.all():
                ques.append({
                    "question": "",
                    "exp": "",
                    "id": z.id,
                })

                que_ids.append(z.id)

            for i in y.get_children():
                my_categories.append({
                    "name": i.name,
                    "idList": list(i.question.values_list('id', flat=True)),
                    "length": len(i.question.values_list('id', flat=True))
                })

                for question in i.question.all():
                    questions.append({
                        "correctAnswerIndex": question.correctAnswerIndex,
                        "exp": question.exp,
                        "question": question.question,
                        "id": question.id
                })

            datalist.append({
                "categorys": my_categories,
                "name": y.name,
                "length": y.question.count(),
            })
            
        subjects.append({
            "name": x.name,
            "length": x.get_descendant_count(),
            "data": datalist
        })
  
    datax = {
        "courseName": course.courseName,
        "courseUniqueId": course.id,
        "subjects": subjects
    }

    datax = json.dumps(datax)

    q = json.dumps(questions)

    return render(request, "Homepage.html", {"questions": questions, "q": q, "datax": datax})

def course_list(request):
    categories = Category.objects.all()

    return render(request, "courses.html", {"categories": categories})

def index(request):
    courses = Course.objects.all()
    
    return render(request, "index.html", {"courses": courses})

@login_required
def profile(request):
    data = {}
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        
        if request.POST.get('email'):
            request.user.first_name = firstname
            request.user.last_name = lastname
            request.user.email = email
            request.user.save()

        data["profile_update"] = True
    
    return render(request, "profile.html", data)

def pricing(request):
    return render(request, "pricing.html")


