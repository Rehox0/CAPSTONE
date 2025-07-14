from django.urls import path
from .views import MenuView, SingleItemMenuView, BookingView, SingleBookingView

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('menu/<int:pk>', SingleItemMenuView.as_view()),
    path('booking/', BookingView.as_view()),
    path('booking/<int:pk>', SingleBookingView.as_view()),
]
