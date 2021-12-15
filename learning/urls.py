from django.urls import path, include
from . import views


urlpatterns = [
    # Shared Paths
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    # Admin Paths
    path('create/professor/', views.CreateProfessor.as_view(), name='create_professor'),
    path('create/student/', views.CreateStudent.as_view(), name='create_student'),
    path('create/admin/', views.CreateAdmin.as_view(), name='create_admin'),
    path('create/course/', views.CreateCourse.as_view(), name='create_course'),
    path('create/module/', views.CreateModule.as_view(), name='create_module'),
    path('list/professors/', views.ListProfessors.as_view(), name='list_professors'),
    path('list/students/', views.ListStudents.as_view(), name='list_students'),
    path('list/admins/', views.ListAdmins.as_view(), name='list_admins'),
    path('list/courses/', views.ListCourses.as_view(), name='list_courses'),
    path('list/modules/', views.ListModules.as_view(), name='list_modules'),
    # Student Paths
    # Professor Paths
]
