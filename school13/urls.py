
from django.contrib import admin
from django.urls import path
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.userprofile, name='userprofile'),
    path('logout/', views.userlogout, name='userlogout'),
    path('changepawd1/', views.changeuserPassword1, name='changepwd1'),
    path('changepwd2/', views.changeuserPassword2, name='changepwd2'),

]
