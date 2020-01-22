from django.test import TestCase
from .models import Category


class ModelTestCase(TestCase):
    def setUp(self):
        self.category_item = create_category(name='1')

    def test_category_model(self):
        old_Category = Category.objects.count()
        self.category_item.save()
        new_Category = Category.objects.count()
        self.assertNotEqual(old_Category, new_Category)


def create_category(name):
    return Category(category_name=name)
