from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # API
    path('', views.get_routes, name="routes"),

    # Auth
    path('token/', views.MyTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('test/', views.test_endpoint, name="test"),
]