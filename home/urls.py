from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('add-post/', views.add_post, name='add_post'),
    path('', views.loginPage, name='login'),
    path('create-account/', views.create_account, name='create_account'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/update/', views.update_post, name='update_post'),
    path('api/', include('home.api.urls')),
  
]