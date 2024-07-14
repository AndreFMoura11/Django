from django.shortcuts import render
from .models import Topic

def index(request):
    """Pagina principal do learning_log"""
    return render(request,'learning_logs/index.html')

def topics(request):    
    """Mostrar todos os assuntos"""
    topic = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'learning_logs/topics.html', context)