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
    path('edit/professor/', views.ListProfessors.as_view(), name='edit_professor'),
    path('edit/student/', views.ListStudents.as_view(), name='edit_student'),
    path('edit/admin/', views.ListAdmins.as_view(), name='edit_admin'),
    path('edit/course/', views.ListCourses.as_view(), name='edit_course'),
    path('edit/module/', views.ListModules.as_view(), name='edit_module'),
    path('delete/professor/', views.ListProfessors.as_view(), name='delete_professor'),
    path('delete/student/', views.ListStudents.as_view(), name='delete_student'),
    path('delete/admin/', views.ListAdmins.as_view(), name='delete_admin'),
    path('delete/course/', views.ListCourses.as_view(), name='delete_course'),
    path('delete/module/', views.ListModules.as_view(), name='delete_module'),
    # Student Paths
    path('list/modules/', views.ListModules.as_view(), name='list_modules'),
    # Professor Paths
]
