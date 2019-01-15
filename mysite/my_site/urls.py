from django.urls import path
from . import views

urlpatterns = [
	#urls to views here
	path('', views.about, name='index'),
	path('about/', views.about, name='about'),
	path('travel/', views.travel, name='travel'),
	path('projects/', views.projects, name='projects'),
	path('resume/', views.resume, name='resume'),
	path('travel/<location>/', views.article, name='article')
]