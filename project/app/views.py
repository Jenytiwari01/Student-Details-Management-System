from django.shortcuts import render
from .models import Student
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def insertData(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        print(name, email, age, gender)
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request, "Data inserted successfully")
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST["gender"]
        edit = Student.objects.get(id=id)
        edit.name=name #added becasue it was reductanting rather than changing
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        
        return redirect("/")

    student = Student.objects.get(id=id)
    context = {"d": student}  # Pass the student data to the context with key 'd'
    return render(request, "edit.html", context)


def deleteData(request, id):
    d = Student.objects.get(id=id)
    # context = {"data": data}
    # return render(request, "index.html", context)
    d.delete()
    messages.error(request, "Data deleted successfully")
    return redirect("/")

def about(request):
    return render(request, "about.html")
