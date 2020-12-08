from django.urls import path
from .views import IndexView
from . import views

app_name = 'ReviewApp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search', views.Search, name='search'),

]
