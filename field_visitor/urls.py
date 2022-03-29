from django.urls import path,include
from django.views.generic import TemplateView
from .views import form_list,track_list

urlpatterns = [
       path('', TemplateView.as_view(template_name="field_visitor/field_visitor.html")),
       path('formlisting/', form_list, name ='form_lists'),
       path('tracklisting/', track_list, name ='track_list'),

]
