from django.test import TestCase
from decimal import Decimal
from restaurant.models import Menu, Booking

class MenuModelTest(TestCase):

    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Ice Cream",
            price=Decimal('5.99'),
            inventory=100
        )

    def test_menu_creation(self):
        retrieved_menu = Menu.objects.get(title="Ice Cream")
        
        self.assertEqual(retrieved_menu.title, "Ice Cream")
        self.assertEqual(retrieved_menu.price, Decimal('5.99'))
        self.assertEqual(retrieved_menu.inventory, 100)
        self.assertIsNotNone(retrieved_menu.pk)

    def test_menu_str_method(self):
        expected_str = "Ice Cream : 5.99"
        self.assertEqual(str(self.menu_item), expected_str)


class BookingModelTest(TestCase):
    
    def setUp(self):
        self.booking_item = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            booking_date="2025-07-20",
            number_table=7,
        )

    def test_booking_creation(self):
        retrieved_booking = Booking.objects.get(name="John Doe")
        
        self.assertEqual(retrieved_booking.name, "John Doe")
        self.assertEqual(retrieved_booking.number_of_guests, 4)
        self.assertEqual(str(retrieved_booking.booking_date), "2025-07-20")
        self.assertEqual(retrieved_booking.number_table, 7)
        self.assertIsNotNone(retrieved_booking.pk)

    def test_booking_str_method(self):
        expected_str = "John Doe for 4 guests on 2025-07-20 for table #7"
        self.assertEqual(str(self.booking_item), expected_str)