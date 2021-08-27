from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('enternumber', views.enternumber, name='enternumber'),
    # path(r'^one/$', RedirectView.as_view(url='http://127.0.0.1:8000')),
]
