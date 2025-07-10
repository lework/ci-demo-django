from django.urls import path
from . import views

# hello应用的URL配置
urlpatterns = [
    path('healthz', views.healthz, name='healthz'),
    path('info', views.info, name='info'),
] 

