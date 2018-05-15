from django.urls import path
from apps.mascota.views import index,mascota_view,mascota_list

app_name = 'apps'
urlpatterns = [
    path('', index,name='index'),
    path('nuevo', mascota_view,name='mascota_crear'),
    path('listar', mascota_list,name='mascota_listar'),
]
