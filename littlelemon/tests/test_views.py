from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from decimal import Decimal

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MenuItemsViewTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_superuser(
            username='testuser', 
            email='test@example.com', 
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.menu_item1 = Menu.objects.create(
            title="Burger", 
            price=Decimal('12.50'), 
            inventory=50
        )
        self.menu_item2 = Menu.objects.create(
            title="Pizza", 
            price=Decimal('15.00'), 
            inventory=30
        )
        self.menu_item3 = Menu.objects.create(
            title="Salad", 
            price=Decimal('8.75'), 
            inventory=70
        )

    def test_getall(self):
        url = reverse('menu') 
        response = self.client.get(url)
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_item(self):
        url = reverse('menu')
        data = {
            'title': 'Fries',
            'price': Decimal('4.00'),
            'inventory': 200
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 4)
        self.assertEqual(Menu.objects.get(title='Fries').price, Decimal('4.00'))

    def test_unauthenticated_access(self):
        unauthenticated_client = APIClient()
        url = reverse('menu')
        response = unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

