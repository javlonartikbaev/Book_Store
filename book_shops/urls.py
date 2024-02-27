from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from books import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls")),
    path("extended_search/", include("search.urls")),
    path("registration/", include("auth_reg.urls")),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
