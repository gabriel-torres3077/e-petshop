from django.contrib import admin
from django.urls import path
from pet_store import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store', views.store, name='store'),
    path('test', views.test, name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











