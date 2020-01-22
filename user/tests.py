from django.test import TestCase
from .models import User

# Create your tests here.


class ModelTest(TestCase):
    def setUp(self):
        self.user = create_user(name='test name', user_name='te-st',
                                email='test@gmail.com', age=24)

    def test_user_model(self):
        old_user = User.objects.count()
        self.user.save()
        new_user = User.objects.count()
        self.assertNotEqual(old_user, new_user)


def create_user(name, user_name, email, age):
    return User(name=name, user_name=user_name, email=email, age=age)
