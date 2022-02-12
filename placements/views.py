from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User


# Create your views here.
@unauthenticated_user
def registerStudent(request):
  try:
    if request.method == "POST":
      
      username = request.POST.get('username')
      first_name = request.POST.get('firstname')
      last_name = request.POST.get('lastname')
      usn = request.POST.get('usn')
      branch = request.POST.get('branch')
      checking_values = Student.objects.filter(usn=usn)
      if checking_values:
        messages.info(request, 'usn already registered')
      else:
        password = request.POST.get('password')
        ConfirmPassword = request.POST.get('Confirmpassword')
        email = request.POST.get('email')
        if password == ConfirmPassword:
          user = User.objects.create_user(username,email,password)
          group = Group.objects.get(name='student')
          user.groups.add(group) 
          user.save()
          student = Student.objects.create(
            user=user,
            usn=usn,
            branch=branch,
            first_name=first_name,
            last_name=last_name,
          )
          student.save()

          return redirect('login')
        else:
          messages.info(request, 'password not matching')
  except:
    messages.info(request, 'username was already taken')
  context = {}
  return render(request, 'placements/registerStudent.html', context)

@unauthenticated_user
def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request, 'Username or password is incorrect')

  context = {}
  return render(request, 'placements/login.html', context)

def logoutUser(request): 
	logout(request)
	return redirect('login')
#-------------------

def HomePage(request):
  context = {}
  return render(request, 'placements/home.html', context)

def processOfPlacement(request):
  context = {}
  return render(request, 'placements/placementProcess.html', context)

def aluminiFeedback(request):
  context = {}
  return render(request, 'placements/aluminiFeedback.html', context)

def companiesVisitBit(request):
  context = {}
  return render(request, 'placements/companiesVisitBit.html', context)

def placementstats(request):
  context = {}
  return render(request, 'placements/placementStats.html', context)

def placementTeam(request):
  context = {}
  return render(request, 'placements/placementTeam.html', context)

#---end of home

def CompanyDetails(request):
  context = {}
  return render(request, 'placements/companyDetails.html', context)

def Resources(request):
  context = {}
  return render(request, 'placements/resources.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def StudentDashBoard(request):
  try:
    user = request.user
    studentInformation = Student.objects.get(user=user)
    context = {'studentInfo':studentInformation}
    return render(request, 'placements/studentdashboard.html', context)
  except:
    return HttpResponse('Sorry technical error')

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def EditStudentDashboard(request):
  # try:
  user = request.user
  student = Student.objects.get(user=user)

  if request.method == 'POST':
    query = request.POST
    username = query.get('username')
    phone = query.get('phone')
    first_name = query.get('first_name')
    last_name = query.get('last_name')
    student_profiles = query.getlist('stu_profiles')
    student_certificates = query.getlist('stu_certificates')
    student_projects = query.getlist('stu_projectslinks')
    user.username = username
    student.phone = phone
    student.first_name = first_name
    student.last_name = last_name
    student.profiles = student_profiles
    student.certificates = student_certificates
    student.projectslinks = student_projects
    user.save()
    student.save()
    
    return redirect('/')

  context = {'studentInfo':student}
  return render(request, 'placements/Editstudentdashboard.html',context)
  # except:
  #   return HttpResponse('Sorry technical error')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'facultycoordinator'])
def StudentDetails(request):
  students = Student.objects.all()

  context = {'students':students}
  return render(request, 'placements/StudentDetails.html',context)
