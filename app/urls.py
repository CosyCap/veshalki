
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf.urls import handler404
from app import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.handler404'