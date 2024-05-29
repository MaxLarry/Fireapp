from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, map_Incidents, LocationList,LocationCreateView, LocationUpdateView, LocationDeleteView, FirestationList, FirestationCreateView, FirestationUpdateView, FirestationDeleteView, FireincidentList, FireincidentCreateView, FireincidentUpdateView, FireincidentDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', map_station, name='map-station'),
    path('Incidents', map_Incidents, name='map-incidents'),

    path('location_list', LocationList.as_view(), name='location-list'),
    path('location_list/add', LocationCreateView.as_view(), name='location-add'),
    path('location_list/<pk>',LocationUpdateView.as_view(), name='location-update'),
    path('location_list/<pk>/delete',LocationDeleteView.as_view(), name='location-delete'),

    path('firestation_list', FirestationList.as_view(), name='firestation-list'),
    path('firestation_list/add', FirestationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>',FirestationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete',FirestationDeleteView.as_view(), name='firestation-delete'),

    path('fireincident_list', FireincidentList.as_view(), name='fireincident-list'),
    path('fireincident_list/add', FireincidentCreateView.as_view(), name='fireincident-add'),
    path('fireincident_list/<pk>',FireincidentUpdateView.as_view(), name='fireincident-update'),
    path('fireincident_list/<pk>/delete',FireincidentDeleteView.as_view(), name='fireincident-delete'),
]
