from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                 path('admin/', admin.site.urls),
                 path('', include('Django_blog.urls')),
                 path('members/', include('django.contrib.auth.urls')),  # using djagos authentication system
                 path('members/', include('authentication_system.urls')),
                 path('news/', include('news_site.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
