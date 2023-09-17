from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='alluser'),
    path('request-reset-email',views.RequestPasswordResetEmail.as_view(),name ='request-reset-email'),
    path('password-reset/<uidb64>/<token>/',views.PasswordTokenCheckAPI.as_view(),name='password_reset_confrim'),
    path('reset_password_complate/',views.SetNewPasswordAPI.as_view(),name='reset_password_complate'),
]
