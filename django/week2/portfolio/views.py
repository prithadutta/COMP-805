from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''

    return render(request,'home.html')

def resume(request):


    return render(request, 'resume.html')

def contact(request):


    return render(request, 'contact.html')
    
def portfolio(request):

    return render(request, 'portfolio.html')
