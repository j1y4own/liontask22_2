
from django.urls import URLPattern, path
from cashbookapp import views
import cashbookapp.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',cashbookapp.views.main, name='main'),
    path('write/', cashbookapp.views.write, name='write'),
    path('read/',cashbookapp.views.read, name='read'),
    path('edit/<str:id>/',cashbookapp.views.edit, name='edit'),
    path('delete/<str:id>/',cashbookapp.views.delete, name='delete'),
    path('detail/<str:id>/',cashbookapp.views.detail, name='detail'),
    path('update_comment/<str:id>/<str:com_id>/', cashbookapp.views.update_comment, name='update_comment'),
    path('delete_comment/<str:id>/<str:com_id>/', cashbookapp.views.delete_comment, name='delete_comment'),
    path('hashtag/', cashbookapp.views.hashtag, name='hashtag'),
    path('like/<str:id>/', cashbookapp.views.likes, name="likes"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)