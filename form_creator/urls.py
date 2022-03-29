from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
       path('', TemplateView.as_view(template_name="form_creator/upload_sheet.html")),
]
