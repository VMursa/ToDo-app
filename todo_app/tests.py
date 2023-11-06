from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()

    def test_login(self):
        # Test login with correct credentials
        response = self.client.post(reverse('login'), {'username': 'testuser1', 'password': '12345'})
        self.assertEqual(response.status_code, 302)  # Should redirect to next page

        # Test login with incorrect credentials
        response = self.client.post(reverse('login'), {'username': 'testuser1', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Stays on the same page

    def test_logout(self):
        # Login first
        self.client.login(username='testuser1', password='12345')

        # Test logout
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect to next page
