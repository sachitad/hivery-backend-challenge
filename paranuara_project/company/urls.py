from django.conf.urls import url, include

from .views import EmployeeListView, EmployeeAttributeListView

urlpatterns = [
    url(r'^employee/$', EmployeeListView.as_view(), name='employee_list'),
    url(r'^employee/attribute/$', EmployeeAttributeListView.as_view(),
        name='employee_attribute_list'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework_auth')),
]