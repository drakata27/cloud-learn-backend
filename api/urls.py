from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # API
    path('', views.get_routes, name="routes"),
    path('section/', views.get_sections, name="sections"),
    path('section/<int:section_id>/topic/', views.get_topics, name="topics"),
    path('section/<int:section_id>/topic/<int:topic_id>/', views.get_subtopics, name="subtopics"),

    # Auth
    path('token/', views.MyTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('test/', views.test_endpoint, name="test"),
]