from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms.widgets import Widget
from learning.models import User, Course, Student, Module


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password') 

# Admin Dashboard Forms
class CreateProfessorForm(UserCreationForm):
    modules = forms.ModelMultipleChoiceField(
        queryset=Module.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
            super(CreateProfessorForm, self).__init__(*args, **kwargs)

    @transaction.atomic            
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_professor = True
        if commit:
            user.save()
        return user


class CreateAdminForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
            super(CreateAdminForm, self).__init__(*args, **kwargs)

    @transaction.atomic            
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user


class CreateStudentForm(UserCreationForm):
    email = forms.EmailField()
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(
            user=user,
            course=self.cleaned_data['course'],
            email=self.cleaned_data['email'],
        )
        return student


class CreateCourseForm(forms.ModelForm):
    id = forms.CharField(max_length=50, required=True)
    name = forms.CharField(max_length=50, required=True)
    description = forms.Textarea()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description')


class CreateModuleForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Module
        fields = ('name', 'courses')
