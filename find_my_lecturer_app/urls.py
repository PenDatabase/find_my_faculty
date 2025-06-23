# find_my_lecturer_app/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = "find_my_lecturer_app"

urlpatterns = [
    path('', views.home, name='home'),
    path("model-diagram/", views.ModelsOverviewView.as_view(), name="models-overview"),
    path("find-lecturer/", views.LecturerListView.as_view(), name="lecturer-search"),

    # for lecturers only
    path('lecturer/dashboard/', views.LecturerDashboardView.as_view(), name='lecturer-dashboard'),
    path("lecturer/<str:lecturer_id>/", views.LecturerDetailView.as_view(), name="lecturer-detail"),
    path('lecturer/edit/<str:pk>/', views.LecturerUpdateView.as_view(), name='lecturer-edit'),
    path("login/",  LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
