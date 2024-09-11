from django.urls import path
from . import views

# Depois da Barra
# Administrar os links
urlpatterns = [
    path('',views.index, name='index'),
    path('topics',views.topics, name='topics'),
    path('topic/<topic_id>/',views.topic, name='topic'),
    path('new_topic',views.new_topic,name='new_topic'),# Notas VVVV Abaixo
    # Por ter 3 topicos , para nao criar uma rota para cada assunto vamos colocar topic// mais o assunto especifico
    # Ai coloca o <topic_id>
    path('new_entry/<topic_id>', views.new_entry, name='new_entry')  
]

# PRECISA ARRUMAR A TELA DE NEW_ENTRY QUANDO CLIK EM ALGU TOPICO ELE NAO ABRI FICA COM ERRO