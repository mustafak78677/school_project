from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from StudentApp.models import Student
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
def index(request):
    content = "<h1>Welcome to Students App</h1><br><br>"
    content = content + "<a href='all_student/'>All Students</a><br><br>"
    content = content + "<a href='add_student/'>Add Students</a><br><br>"
    return HttpResponse(content)


def add_student(request):
    return render(request, 'StudentApp/add_student.html')


def all_student(request):
    latest_student_list = Student.objects.all()
    context = {'latest_student_list':latest_student_list}
    return render(request, 'StudentApp/student_list.html', context)


def details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student':student}
    return render(request, 'StudentApp/student_details.html', context)


def add(request):
    get_name = request.POST['name']
    get_course = request.POST['course']
    get_gender = request.POST['gender']
    get_roll = request.POST['roll']
    get_fees = request.POST['fees']
    
    stud = Student(
        name=get_name,course=get_course,gender=get_gender,rollno=get_roll,fees=get_fees,pub_date=timezone.now()
    )

    message = ""

    try:
        stud.save()
        message = "Student Record added Successfully!"
    except:
        message = "Cant save student record, try again"
    context = {'message':message}
    return render(request, "StudentApp/add_student.html",context)


def student_delete(request, student_id):
    stud = get_object_or_404(Student, pk=student_id)
    message=""
    try:
        stud.delete()
        message="Student Record deleted Successfully!"
    except:
        message="Can't delete the record, try again"
    message = message + "<br><br><a href='../../student/all_student'>Back</a>"
    return HttpResponse(message)


#django-rest-framework

@csrf_exempt
def Student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except student.DoesNotExist:
        return HttpResponse(staus=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    if request.method == 'DELETE':
        student.delete()
        return HttpResponse("Record Deleted Successfully")



