from django.shortcuts import render
from django.http import HttpResponse
from .models import Resume, Experience, Education


def home(request):
	"""
	renders the resume page from resume app
	"""
	resume_obj = Resume.objects.first()

	return render(request, "resume/home.html",
	context={"resume": resume_obj})
