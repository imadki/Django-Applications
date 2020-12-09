from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('Demo/', include('Demo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Demo/', TemplateView.as_view(template_name='voie_form.html'), name='add_voie'),
    path('Demo/', TemplateView.as_view(template_name='chaussee_form.html'), name='add_chaussee'),
    url(r'^Demo/', include (('Demo.urls', 'Demo') , namespace='Demo'))
]
