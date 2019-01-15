from django.db import models

# Create your models here.
class About(models.Model):
    bio_title = models.CharField(max_length=100)
    bio = models.TextField()
    git_link = models.URLField(default="https://github.com/vitogalv")
    linkedin = models.URLField(default="www.linkedin.com/in/vito-galvez-50413714a")

    def __str__(self):
    	return self.bio_title

class Place(models.Model):
	place_name = models.CharField(max_length=200)
	thumbnail = models.ImageField(upload_to='places/')
	article = models.TextField()

	def __str__(self):
		return self.place_name

class Photo(models.Model):
	place = models.ForeignKey('Place', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='photos/')

	def __str__(self):
		return self.place.place_name

class Project(models.Model):
	title = models.CharField(max_length=100, unique=True)
	summary = models.TextField()
	git_link = models.URLField()

	def __str__(self):
		return self.title

class Position(models.Model):
	title = models.CharField(max_length=200)
	company = models.CharField(max_length=300)
	city = models.CharField(max_length=50, default="City")
	state = models.CharField(max_length=50, default="State")
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField()

	def __str__(self):
		return self.title

class Skill(models.Model):
	skill = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.skill

class Quote(models.Model):
	quote = models.TextField()
	author = models.CharField(max_length=100)

	def __str__(self):
		return self.author

class School(models.Model):
	name = models.CharField(max_length=150)
	grad_date = models.DateField()
	description = models.TextField()

	def __str__(self):
		return self.name
