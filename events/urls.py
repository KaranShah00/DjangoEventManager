from django.urls import path, include

from .views import (
    start, home, EventListView, EventCreateView, EventUpdateView, EventDeleteView,
    MonthlyEventListView
)

urlpatterns = [
    path('', start, name = 'start'),
    path('home/', EventListView.as_view(), name = 'home'),
    path('monthly', MonthlyEventListView.as_view(), name = 'monthly'),
    path('add/', EventCreateView.as_view(), name='add'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name = 'update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name = 'delete'),
]