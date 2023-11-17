from django.test import TestCase
from accounts.models import User

class UserCreationTests(TestCase):

    def test_valid_user_creation(self):
        """Test that a new user can be created with valid credentials."""
        user = User.objects.create_user(username='testuser', email='test@example.com', password='123456')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('123456'))
