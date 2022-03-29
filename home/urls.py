from django.urls import path,include
from django.views.generic import TemplateView
from .views import Login

urlpatterns = [
       path('', TemplateView.as_view(template_name="home/base.html")),
       path('login/', Login, name ='login'),

]

