from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from article.views import detail
from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>/', detail, name='detail'),
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)