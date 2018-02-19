from django.shortcuts import render
from .models import Education, Experience
# Create your views here.

def home(request):
	"""
	renders the resume home template
	"""
	name = "Pritha Dutta"
	address = "172 Forest Park, Durham, NH-03824"
	email = "pd1057@wildcats.unh.edu"
	skills = ["Java","C++", "Python", "Django", "Software Testing"]
	context = {}
	educations = Education.objects.order_by('degree')
	experiences = Experience.objects.order_by('title')
	context = {'my_education':educations,'my_experiences':experiences,
	'my_name':name,'my_addr':address,"my_email":email,
	"my_skills":skills}
	return render(request,'resume/home.html',context)
