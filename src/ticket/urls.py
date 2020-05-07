from django.urls import path, include
from django_filters.views import FilterView
from . import views
from .filters import TicketFilter
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ticket/follow/', views.AddFollowerView.as_view(), name='follow'),
    # path('user/all', ),
    path('', views.TicketListView.as_view(), name='ticket-home'),
    path('ticket/search/', views.FilteredTicketList.as_view(), name='ticket-search'),
    path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name='ticket-detail'),
    path('about/', views.about, name='ticket-about'),
    path('ticket/new/', views.TicketCreateView.as_view(), name='ticket-create'),
    path('ticket/<int:pk>/update/', views.TicketUpdateView.as_view(), name='ticket-update'),
    path('ticket/<int:pk>/delete/', views.TicketDeleteView.as_view(), name='ticket-delete'),
    # path('create/comment', views.CreateComment.as_view(), name='create-comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
