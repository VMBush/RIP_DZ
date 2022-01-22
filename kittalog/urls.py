from django.urls import include, path
from . import views



urlpatterns = [
    path("", views.ShelterListView.as_view(), name='shelter_list'),
    path("<int:sh>/", views.KitListView.as_view(),  name='kittalog'),
    path("kit/<int:pk>", views.KitDetailView.as_view(), name='kit_detail'),
    

]
