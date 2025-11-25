from django.urls import path
from .views import ReservaCreateView

urlpatterns = [
    path('nova/', ReservaCreateView.as_view(), name='reservar_recurso'),
]