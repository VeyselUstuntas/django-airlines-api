
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/",include('account.urls')),
    path('', include('airlines.urls')),
    path('api/api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/api-token-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
