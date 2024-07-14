from django.contrib import admin
from django.urls import path , include

# Adiministrar os links
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('learning_logs.urls')),
]

