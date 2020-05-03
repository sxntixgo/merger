from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve
from main import urls as main_urls
from reports import urls as reports_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls)),
    path('report/', include(reports_urls)),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]
