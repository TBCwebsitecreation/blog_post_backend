
from django.contrib import admin
from django.urls import path, include, repath
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# all routes will be handled here

urlpatterns += [repath(r'^.*', TemplateView.as_view(template_name="index.html"))]
