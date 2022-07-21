from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.core.views import page_not_found

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
                  path('', include('apps.core.urls')),
                  path('', include('apps.accounts.urls')),
                  path('manager/', include('apps.manager.urls')),
                  path('cart/', include('apps.cart.urls')),
                  path('admin/', admin.site.urls),
                  path('api/', include('apps.api.urls')),
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('__debug__/', include('debug_toolbar.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
