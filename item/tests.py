from django.test import TestCase
from item.models import Item
from user.models import User
from category.models import Category

from rest_framework.test import APIClient
from rest_framework import status


class TestModel(TestCase):
    def setUp(self):
        self.title = 'Test title'

        self.user = User(
            name='test', user_name='te-st', email='test@gmail.com', age=20)
        self.user.save()

        self.category = Category(category_name=1)
        self.category.save()

        self.item = Item(title=self.title, user=self.user,
                         category=self.category)

    def test_item_model(self):
        old_item = Item.objects.count()
        self.item.save()
        new_item = Item.objects.count()
        self.assertNotEqual(old_item, new_item)


class TestItemViewSet(TestCase):
    """
        All test functions into the TestItemViewSet are for ItemViewSet
    """

    def setUp(self):
        """
            Before each the test function
        """
        self.client = APIClient()

        # Create a fake todo item
        self.user = User(name='test', user_name='te-st',
                         email='test@gmail.com', age=20)
        self.user.save()

        self.category = Category(category_name=1)
        self.category.save()

        self.item_data = {
            'title': 'Test',
            'user': self.user.id,
            'category': self.category.id
        }

        # Fake post request
        self.response = self.client.post(
            '/api/todo/',
            self.item_data,
            format='json'
        )

    # Post Request
    def test_post_method(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # Get Request
    def test_get_method(self):
        todo_count = Item.objects.count()
        response = self.client.get(
            '/api/todo/',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo_count, len(response.data))

    # Retrieve Request
    def test_retrieve_method(self):
        todo_item = Item.objects.get(title='Test')
        response = self.client.get(
            '/api/todo/',
            kwargs={'pk': todo_item.id},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todo_item)
