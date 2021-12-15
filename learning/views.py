from django.contrib import auth
from django.urls.base import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from learning.constants import INSTITUTE_NAME
from learning.models import Professor, User, Course, Module
from learning.forms import CreateProfessorForm, CreateStudentForm, CreateAdminForm, CreateCourseForm, CreateModuleForm


def home(request):
	return render(request, 'home.html', {'INSTITUTE_NAME': INSTITUTE_NAME})

def contact(request):
	return render(request, 'contact.html', {'INSTITUTE_NAME': INSTITUTE_NAME})

def logoutView(request):
    logout(request)
    return redirect('home')


class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if (request.method == "GET"):
            return self.login_page(request, *args, **kwargs)
        elif (request.method == "POST"):
            return self.login(request, *args, **kwargs)

    def login(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('login')

    def login_page(self, request, *args, **kwargs):
        return render(request, 'login.html', {'INSTITUTE_NAME': INSTITUTE_NAME})


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_admin:
                context = {
                    'INSTITUTE_NAME': INSTITUTE_NAME,
                    'total_courses': Course.objects.all().count(),
                    'total_students': User.objects.filter(is_student=True).count(),
                    'total_professors': User.objects.filter(is_professor=True).count(),
                    'total_modules': Module.objects.all().count(),
                }
                return render(request, 'dashboard/admin/home.html', context)
            elif request.user.is_professor:
                return render(request, 'dashboard/professor/home.html', {'INSTITUTE_NAME': INSTITUTE_NAME})
            elif request.user.is_student:
                return render(request, 'dashboard/student/home.html', {'INSTITUTE_NAME': INSTITUTE_NAME})
        else:
            return redirect('login')

# Admin dashboard views
class CreateProfessor(LoginRequiredMixin, CreateView):
    form_class = CreateProfessorForm
    model = User
    template_name = 'dashboard/admin/create-professor.html'
    success_url = reverse_lazy('create_professor')


class CreateStudent(LoginRequiredMixin, CreateView):
    form_class = CreateStudentForm
    model = User
    template_name = 'dashboard/admin/create-student.html'
    success_url = reverse_lazy('create_student')


class CreateAdmin(LoginRequiredMixin, CreateView):
    form_class = CreateAdminForm
    model = User
    template_name = 'dashboard/admin/create-admin.html'
    success_url = reverse_lazy('create_admin')


class CreateCourse(LoginRequiredMixin, CreateView):
    form_class = CreateCourseForm
    model = Course
    template_name = 'dashboard/admin/create-course.html'
    success_url = reverse_lazy('create_course')


class CreateModule(LoginRequiredMixin, CreateView):
    form_class = CreateModuleForm
    model = Module
    template_name = 'dashboard/admin/create-module.html'
    success_url = reverse_lazy('create_module')



class ListProfessors(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/admin/list-professors.html'
    queryset = User.objects.filter(is_professor=True)


class ListStudents(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/admin/list-students.html'
    queryset = User.objects.filter(is_student=True)


class ListAdmins(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/admin/list-admins.html'
    queryset = User.objects.filter(is_admin=True)


class ListCourses(ListView):
    model = Course
    template_name = 'dashboard/admin/list-courses.html'
    queryset = Course.objects.all()


class ListModules(ListView):
    model = Module
    template_name = 'dashboard/admin/list-modules.html'
    queryset = Module.objects.all()
