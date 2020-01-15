from django.conf.urls import url

from .views import (
    medicinesList,
    medicinesDetail,
    medicinesCreation,
    medicinesUpdate,
    medicinesDelete
)

urlpatterns = [

    url(r'get^$', medicinesList.as_view(), name='list'),
    url(r'^new$', medicinesCreation.as_view(), name='new'),
    url(r'^update/(?P<pk>\d+)$', medicinesUpdate.as_view(), name='edit'),
    url(r'detail^(?P<pk>\d+)$', medicinesDetail.as_view(), name='detail'),
    url(r'^remove/(?P<pk>\d+)$', medicinesDelete.as_view(), name='delete'),

]