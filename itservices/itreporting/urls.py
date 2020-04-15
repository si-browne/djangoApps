from django.urls import path
from . import views
#from .views import PostListView, PostDetailView

urlpatterns =[
path('', views.home, name='itreporting-home'),
path('about/', views.about, name='itreporting-about'),
path('contact/', views.contact, name='itreporting-contact'),
path('report/', views.report, name='itreporting-report'),
#path('report/', PostListView.as_view(), name='itreporting-report'),
#path('issue/<int:pk>', PostDetailView.as_view(), name='issue-detail'),
]