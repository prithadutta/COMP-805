from django.shortcuts import render

def home(request):
    '''
    renders homepage
    '''
    greeting= "uStudy-The best study site in the world!"
    days_of_week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    today='tuesday'
    context={'our_greeting':greeting, 'weekday_list':days_of_week}
    return render(request, 'home.html', context)
