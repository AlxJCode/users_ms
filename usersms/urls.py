
from django.contrib import admin
from django.urls import path, include
from .utils.auth_views import CustomTokenObtainPairView, ValidateTokenView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/auth/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/verify/', ValidateTokenView.as_view(), name='token_verify'),


    path('api/users/', include('users.urls')),

]
