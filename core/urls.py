from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title = 'Banking API',
        default_version = 'v1',
    ),
    public = True,
    permission_classes = (AllowAny,),
    authentication_classes = [],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'swagger-ui'),
    path('api/accounts/', include('accounts.urls')),
]
