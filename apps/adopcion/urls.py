from django.urls import path
from apps.adopcion.views import index,SolicitudList,SolicitudCreate

app_name = 'apps'
urlpatterns = [
	path('',index),
	path('solicitud/listar',SolicitudList.as_view(),name='solicitud_listar'),
	path('solicitud/nuevo',SolicitudCreate.as_view(),name='solicitud_crear'),
]