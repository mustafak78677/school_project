from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def hello_world(request):
    message = "Hello World"
    return HttpResponse(message)


def index_page(request):
    message = "<h1>Welcome to School Project</h1>"
    message += "<a href='student/'>Go to Students App</a>"
    return HttpResponse(message)


def home(request):
    return render(request,'home.html')


class AboutUs(View):
      def get(self, request):
          message = "We Provide All Services"
          return HttpResponse(message)