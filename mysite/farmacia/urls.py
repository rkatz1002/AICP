from django.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastrarMedicamento', views.cadastrarMedicamento, name = 'cadastrarMedicamento'),
    re_path('buscarMedicamento', views.buscarMedicamento, name="buscarMedicamento"),
    re_path('saidaPrescricao', views.saidaPrescricao, name="saidaPrescricao"),
<<<<<<< HEAD
    re_path('algo',views.teste,name="algo")
=======
    re_path('retirarMedicamento', views.retirarMedicamento, name="retirarMedicamento"),
    re_path('algo', views.teste, name="algo"),
>>>>>>> 3653af6dbf86b5dfb037e4e9905db4bbcb2cf995
]