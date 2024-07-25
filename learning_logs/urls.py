from django.urls import path
from . import views

# Depois da Barra
# Administrar os links
urlpatterns = [
    path('',views.index, name='index'),
    path('topics',views.topics, name='topics'),
    path('topics/<topic_id>/',views.topic, name='topic'),
    # Por ter 3 topicos , para nao criar uma rota para cada assunto vamos colocar topic// mais o assunto especifico
    # Ai coloca o <topic_id>  
]

