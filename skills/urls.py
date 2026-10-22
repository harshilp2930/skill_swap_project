from django.urls import path
from django.views.generic import RedirectView # Import RedirectView
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('listings/', views.listings_view, name='listings'),
    path('profile/', views.profile_view, name='profile'),
    path('add/', views.add_skill_view, name='add_skill'),
    path('edit/<int:skill_id>/', views.edit_skill_view, name='edit_skill'),
    path('delete/<int:skill_id>/', views.delete_skill_view, name='delete_skill'),
    path('update_profile/', views.update_profile_view, name='update_profile'),
    path('user_data/submit/', RedirectView.as_view(pattern_name='index', permanent=False)),            
]



