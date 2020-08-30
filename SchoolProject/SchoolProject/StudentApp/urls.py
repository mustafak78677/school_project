from django.urls import path
from StudentApp.views import index, add_student, all_student, add, student_delete, Student_list, student_detail
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.index),
    path('add_student/',views.add_student),
    path('all_student/',views.all_student),
    path('<int:student_id>/', views.details, name='details'),
    path('add/', views.add),
    path('<int:student_id>/student_delete', views.student_delete, name='student_delete'),
    path('student_api/students/', views.Student_list),
    path('student_api/students/<int:pk>/', views.student_detail),
]