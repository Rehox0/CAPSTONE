from django.urls import path
from .views import MenuView, SingleItemMenuView, BookingView, SingleBookingView

urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleItemMenuView.as_view(), name='signle_item_menu'),
    path('booking/', BookingView.as_view()),
    path('booking/<int:pk>', SingleBookingView.as_view()),
]
