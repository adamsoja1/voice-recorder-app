from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('upload/',views.upload),
    path('home/',views.home),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








