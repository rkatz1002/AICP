from django.contrib import admin
from django.urls import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginAndSignUp.urls')),
    path('', include('farmacia.urls')),
    path('', include('medicos.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
