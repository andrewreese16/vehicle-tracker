from django.urls import path
from . import views
from .views import SignUpView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
    path("", views.vehicle_list, name="home"),
    path("vehicles/", views.vehicle_list, name="vehicle_list"),
    path("vehicles/<int:vehicle_id>/", views.vehicle_detail, name="vehicle_detail"),
    path("vehicles/new/", views.vehicle_create, name="vehicle_create"),
    path(
        "vehicles/<int:vehicle_id>/edit/", views.vehicle_update, name="vehicle_update"
    ),
    path(
        "vehicles/<int:vehicle_id>/delete/", views.vehicle_delete, name="vehicle_delete"
    ),
    path(
        "vehicles/<int:vehicle_id>/maintenance/new/",
        views.maintenance_create,
        name="maintenance_create",
    ),
    path(
        "vehicles/<int:vehicle_id>/maintenance/<int:maintenance_id>/update/",
        views.maintenance_update,
        name="maintenance_update",
    ),
    path(
        "vehicles/<int:vehicle_id>/maintenance/<int:maintenance_id>/delete/",
        views.maintenance_delete,
        name="maintenance_delete",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', SignUpView.as_view(), name='signup'),
]
