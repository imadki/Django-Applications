from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('list/voie/', views.VoieListView.as_view(), name='voie_changelist'),
    path('add/voie/', views.VoieCreateView.as_view(), name='voie_add'),
    
    path('load-voies/', views.load_voies, name='load_voies'),
    path('load-cities/', views.load_cities, name='load_cities'),

    path('accounts/', include('accounts.urls')),
    url(r'^accounts/', include (('accounts.urls', 'accounts') , namespace='accounts')),
]
