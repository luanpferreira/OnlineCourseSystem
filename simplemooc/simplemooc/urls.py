from django.urls import path, include
from django.contrib import admin
from simplemooc.core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('simplemooc.core.urls', 'core'))), # Esse nome é o que vai referenciar dentro dos HTMLs
    path('cursos/', include(('simplemooc.courses.urls', 'courses'))),
    path('conta/', include(('simplemooc.accounts.urls', 'accounts'))),
    # Outras rotas...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)