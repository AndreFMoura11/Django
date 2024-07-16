from django.urls import path
from . import views

# Depois da Barra
# Adiministrar os links
urlpatterns = [
    path('',views.index, name='index'),
    path('topics',views.topics, name='topics'),
    #path('topic//',views.topic, name='topic'),
]

