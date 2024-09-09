from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.get_routes, name="routes"),
    # Section
    path('public-section/', views.get_public_sections, name="public_sections"),
    path('section/', views.get_sections, name="sections"),
    path('section/<str:pk>/', views.get_section, name="section"),
    path('section/<str:pk>/edit/', views.update_section, name="update_section"),

    # Topic
    path('section/<int:section_id>/topic/', views.get_topics, name="topics"),
    path('section/<int:section_id>/topic/<str:pk>/', views.get_topic, name="topic"),
    path('section/<int:section_id>/topic/<str:pk>/edit/', views.update_topic, name="update_topic"),
    
    # Subtopic
    path('section/<int:section_id>/topic/<int:topic_id>/subtopic/', views.get_subtopics, name="subtopics"),
    path('section/<int:section_id>/topic/<int:topic_id>/subtopic/<str:pk>/', views.get_subtopic, name="subtopic"),
    path('section/<int:section_id>/topic/<int:topic_id>/subtopic/<str:pk>/edit/', views.update_subtopic, name="update_subtopic"),

    # Flash Card
    path('subtopic/<str:subtopic_id>/flashcard/', views.get_flashcards, name="flash_cards"),
    path('subtopic/<str:subtopic_id>/flashcard/<str:pk>/', views.get_flashcard, name="flash_card"),
    path('subtopic/<str:subtopic_id>/flashcard/<str:pk>/edit/', views.update_flashcard, name="update_flash_card"),

    # Auth
    path('token/', views.MyTokenObtainPairView.as_view(), name='token'),
    path('register/', views.RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('test/', views.test_endpoint, name="test"),

    # Health
    path('health/', views.health, name="health"),
    
    # Profiles
    path('profiles/', views.get_profiles, name="profiles"),
    path('<str:username>/', views.get_profile, name="profile"),

]