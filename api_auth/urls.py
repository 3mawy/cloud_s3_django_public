from django.urls import include, path
from rest_framework import routers
from api_auth.views import register
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

urlpatterns = [
    path('register', register, name='register'),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
