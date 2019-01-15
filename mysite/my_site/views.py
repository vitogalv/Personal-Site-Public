from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Place, Photo, Project, Position, Skill, Quote, School
from django.template import loader

# Create your views here.
def about(request):
	about = About.objects.get(pk=1)
	quote = Quote.objects.get(pk=1)
	template = loader.get_template('about/about.html')
	context = {
		'about' : about,
		'quote' : quote,
	}
	return HttpResponse(template.render(context, request))

def travel(request):
	about = About.objects.get(pk=1)
	places = Place.objects.all()
	template = loader.get_template('travel/travel.html')
	context = {
		'places' : places,
		'about' : about,
	}
	return HttpResponse(template.render(context, request))

def article(request, location):
	about = About.objects.get(pk=1)
	place = Place.objects.get(place_name=location)
	pics = Photo.objects.filter(place__place_name=place)
	template = loader.get_template('travel/article.html')
	context = {
		'place' : place,
		'pics' : pics,
		'about' : about,
	}
	return HttpResponse(template.render(context, request))

def projects(request):
	about = About.objects.get(pk=1)
	projects = Project.objects.all()
	template = loader.get_template('projects/projects.html')
	context = {
		'projects' : projects,
		'about' : about,
	}
	return HttpResponse(template.render(context, request))

def resume(request):
	about = About.objects.get(pk=1)
	schools = School.objects.all().order_by('-grad_date')
	skills = Skill.objects.all()
	positions = Position.objects.all().order_by('-start_date')
	template = loader.get_template('resume/resume.html')
	context = {
		'schools' : schools,
		'positions' : positions,
		'skills' : skills,
		'about' : about,
	}
	return HttpResponse(template.render(context, request))