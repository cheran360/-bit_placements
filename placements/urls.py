from django.urls import path
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
	path('', views.HomePage, name="home"),
	path('home/processOfPlacement/', views.processOfPlacement, name="processOfPlacement"),
	path('home/aluminiFeedback/', views.aluminiFeedback, name="aluminiFeedback"),
	path('home/companiesVisitBIT/', views.companiesVisitBit, name="companiesVisitBit"),
	path('home/placementstats/', views.placementstats, name="placementstats"),
	path('home/placementTeam/', views.placementTeam, name="placementTeam"),

	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),   
	path('registerStudent/', views.registerStudent, name="registerStudent"),
	path('companyDetails/', views.CompanyDetails, name="companyDetails"),
  path('resources/', views.Resources, name="resources"),
	path('student/dashboard/', views.StudentDashBoard, name="studentDashBoard"),
	path('student/editdashboard/', views.EditStudentDashboard, name="editStudentDashBoard"),

	path('coordinators/studentDetails/', views.StudentDetails, name="studentDetails"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)