from django.shortcuts import render
#from django.http import HttpResponse (no longer needed )


#create your views here.

def home(request):
    return render(request, 'itreporting/home.html')#pointing home to HTML file home.html
    #return HttpResponse('<h1> Student IT Services - Home </h1>')

def about(request):
    return render(request, 'itreporting/about.html')#pointing home to HTML file about.html
    #return HttpResponse('<h1> Student IT Services - About </h1>')

def contact(request):
    return render(request, 'itreporting/contact.html')#pointing home to HTML file contact.html
    #return HttpResponse('<h1> Student IT Services - Contact Us </h1>')