from django.urls import path
from .views import IndexView
from . import views

app_name = 'ReviewApp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search', views.Search, name='search'),
    path('shop_info/<str:restid>', views.ShopInfo, name='shop_info'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

]
