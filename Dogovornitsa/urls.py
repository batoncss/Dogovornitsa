from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("participants/", include("Dogovornitsa.apps.participants.urls")),
    path("templates/", include("Dogovornitsa.apps.templates.urls")),
    path("orders/", include("Dogovornitsa.apps.orders.urls")),
    path("", include("Dogovornitsa.apps.pages.urls")),
    path("", include("Dogovornitsa.apps.iam.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
