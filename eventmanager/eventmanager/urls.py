"""eventmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.conf.urls import handler500
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import notifications.urls

from eventmanager import settings

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='EventManager API')

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('events/', include('stats.urls')),
    path('', include('exporting.urls')),
    path('', include('homepage.urls')),
    path('events/', include('events.urls')),
    path('', include('tasks.urls')),
    path('categories/', include('categories.urls')),
    url(
        '^inbox/notifications/',
        include(notifications.urls,
                namespace='notifications')
    ),
    url(r'^api/', include('api.urls')),
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^swagger/', schema_view),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
] + static(settings.STORAGE_URL, document_root=settings.STORAGE_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'custom_errors.views.error_404_view'
# handler500 = 'custom_errors.views.error_404_view'

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
