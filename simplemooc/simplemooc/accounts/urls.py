from django.urls import path, include
from simplemooc.accounts import views
from django.contrib.auth.views import LoginView, LogoutView
from simplemooc.accounts import views

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('cadastre-se/', views.register, name='register'),
    path('editar/', views.edit, name='edit'),
    path('', views.dashboard, name='dashboard'),
    path('editar_senha/', views.edit_password, name='edit_password'),
    # outras URL patterns do seu projeto
]