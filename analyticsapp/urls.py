from django.urls import path
from .views import *

urlpatterns = [
    path('sites/', SiteListView.as_view(), name='site-list'),
    path('sites/<int:pk>/', SiteDetailView.as_view(), name='site-detail'),
    path('sites/create/', SiteCreateView.as_view(), name='site-create'),
    path('sites/<int:pk>/edit/', SiteUpdateView.as_view(), name='site-edit'),
    path('sites/<int:pk>/delete/', SiteDeleteView.as_view(), name='site-delete'),

    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('visitors/', VisitorListView.as_view(), name='visitor-list'),
    path('activities/', ActivityListView.as_view(), name='activity-list'),
]