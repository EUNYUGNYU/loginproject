from django.contrib import admin
from django.urls import path,include
import blog.urls
import blog.views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.welcome,name='welcome'),
    path('funccrud/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

