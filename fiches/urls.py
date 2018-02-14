from django.conf.urls import url

from .views import list_fiche



app_name = 'fiches'
urlpatterns = [
    url(r'^$', list_fiche, name='list-fiche'),
]