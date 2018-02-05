from django.shortcuts import render

def home(request):
    """
    Renders home page
    """
    context={}
    return render(request,'home.html',context)

def resume(request):
    """
    Renders resume page
    """
    name = "Pritha Dutta"
    address = "172 Forest Park, Durham, NH-03824"
    phone = "(603) 285-1724"
    email = "pd1057@wildcats.unh.edu"
    skills = ["Java","Python","Django","Software Testing"]
    context={'my_name':name,'my_addr':address,'my_phone':phone,"my_email":
	email,"my_skills":skills}
    return render(request,'resume.html',context)

def portfolio(request):
    """
    Renders portfolio page
    """
    context={}
    return render(request,'portfolio.html',context)

def contact(request):
    """
    Renders contact page
    """
    context={}
    return render(request,'contact.html',context)
    
