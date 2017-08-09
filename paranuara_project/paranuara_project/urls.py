from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^api/v1/', include('company.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
