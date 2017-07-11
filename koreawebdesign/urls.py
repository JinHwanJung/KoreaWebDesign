from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'koreawebdesign'
urlpatterns = [
    url(r'^$',views.index, name='index'), # index
    url(r'^page/(?P<page>\d+)/$',views.kwdListView, name='kwd_list'), # page
    url(r'^kwd(?P<pk>\d+)/$',views.KWDDetailView.as_view(), name='kwd_detail'),
    url(r'^tag/(?P<tag>[^/]+(?u))/$',views.KwdTeggedObjectList.as_view(), name="kwd_tagged_object_list"),
    url(r'^search/$', views.SearchFormView.as_view(), name='search')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
