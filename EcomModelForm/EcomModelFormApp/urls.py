from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enter', views.enter),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('view_list', views.view_list, name='view_list'),
    path('account/login',views.loginview,name="login"),
    path('logout',views.logout_view),  
    path('account/sign_up/',views.sign_up,name='register'),
    path('reset',views.Resethome,name='reset'),
    path('passwordreset',views.resetPassword)
    
]