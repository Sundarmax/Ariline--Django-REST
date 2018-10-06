from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from flight.views import login
from flight import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'flight',views.flightViewSet)
router.register(r'flight_details',views.flightDViewSet)
router.register(r'passenger_profile',views.passengerViewSet)
router.register(r'ticket_info',views.ticketViewSet)
router.register(r'card_info',views.cardViewSet)
router.register(r'admin_user',views.AdminViewSet)
#router.register(r'^flight_list/$',views.flight_list)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login',login),
    url(r'^',include(router.urls)),
    url(r'^flight_list/(?P<pk>[0-9]+)$', views.flight_list),
    url(r'^flight_list/$', views.flight_listAll),
    #url(r'^admin_user/$',views.adminUser_Add)
    #url(r'^flight_details/$', views.flight_detail)
]