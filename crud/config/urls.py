
from django.contrib import admin
from django.urls import path
from crud.tickets.views import TicketList, TicketDetail, LoginView, RegisterView, UsersView, DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TicketList.as_view(), name='home'),
    path('users/', UsersView.as_view(), name='users-list'),
    path('tickets/', TicketList.as_view(), name='tickets-list'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]
