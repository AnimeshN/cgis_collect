from django.shortcuts import render

# Create your views here.

def form_list(request):
    return render(request, 'field_visitor/form_list.html')

def track_list(request):
    return render(request, 'field_visitor/track_list.html')