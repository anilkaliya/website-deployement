from django.conf.urls import url
from prop import views
app_name = 'prop'
urlpatterns=[url(r'^create/$',views.Propercreateview.as_view(),name='create'),
url(r'^getbychandigarh/$',views.propertyfromchandigarh,name='chandigarh'),
url(r'^getbymohali/$',views.propertyfrommohali,name='mohali'),
url(r'^getbykahrar/$',views.propertyfromkharar,name='kharar'),
  url(r'^search/$', views.search, name='search'),

]
