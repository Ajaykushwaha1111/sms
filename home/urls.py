from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name= 'home'),
    path('startexam/', views.startexam, name= 'startexam'),
    path('endexam/', views.end_exam, name= 'endexam'),
    path('count/',views.count_quetion, name='count_quetion'),
    path('signup/',views.student_signup, name='student_signup'),
    path('logouts/',views.logout_student, name='logouts'),
    path('dashboard/',views.dashboard_student, name='dashboard'),
    path('help/',views.help, name='help'),
    path('change_password/',views.change_password, name='change_password'),
    path('forget_password',views.forget_password, name='forget_password'),



]