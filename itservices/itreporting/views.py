from django.shortcuts import render
from django.db import models
from django.views.generic import ListView, DetailView
#from django.http import HttpResponse (no longer needed )
#create your views here.




def report(request):
    daily_report= {
        'issues': Issue.objects.all()
    }


def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Home'} )#pointing home to HTML file home.html
    #return HttpResponse('<h1> Student IT Services - Home </h1>')

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'} )#pointing home to HTML file about.html
    #return HttpResponse('<h1> Student IT Services - About </h1>')

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact'} )#pointing home to HTML file contact.html
    #return HttpResponse('<h1> Student IT Services - Contact Us </h1>')

def report(request):
    return render(request, 'itreporting/report.html')#pointing home to HTML file report.html

#class PostListView(ListView):
    #model = Issue
    #template_name = 'itreporting/report.html'
    #context_object_name = 'issues'
    #ordering = ['-date_submitted']

#class PostDetailView(DetailView):
    #model = Issue