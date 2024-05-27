from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.get_routes, name="routes"),
    # Section
    path('section/', views.get_sections, name="sections"),
    path('section/<str:pk>/', views.get_section, name="section"),
    path('section/<str:pk>/edit/', views.update_section, name="update_section"),

    # Topic
    path('section/<int:section_id>/topic/', views.get_topics, name="topics"),
    path('section/<int:section_id>/topic/<int:topic_id>/', views.get_subtopics, name="subtopics"),

    # Auth
    path('token/', views.MyTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('test/', views.test_endpoint, name="test"),
]