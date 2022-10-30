from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
import cashbookapp.views
import cuapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cashbookapp.urls')),
    path('',include('cuapp.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
