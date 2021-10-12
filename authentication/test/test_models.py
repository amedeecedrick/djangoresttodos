from rest_framework.test import APITestCase
from authentication.models import User
class TestModel(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user('amedee', 'amedee@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email,'amedee@gmail.com')
        self.assertFalse(user.is_staff)

    def test_raises_error_when_no_username_is_supplied(self):

        self.assertRaises(ValueError,User.objects.create_user,username = "",email= 'amedee@gmail.com',password= 'password123!@')
    def test_raises_error_when_no_email_is_supplied(self):

        self.assertRaises(ValueError,User.objects.create_user,username = "amedee",email= '',password= 'password123!@')
 

    def test_creates_super_user(self):
        user = User.objects.create_superuser('amedee', 'amedee@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email,'amedee@gmail.com')
        self.assertTrue(user.is_staff)
    def test_create_super_user_with_staff_user_status(self):
        with self.assertRaisesMessage(ValueError, "Super user must have is staff= True."):
            User.objects.create_superuser(username = "amedee", email = 'amedee@gmail.com', password = 'password123!@', is_staff = False)
    
    def test_create_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, "Super user must have is superuser= True."):
            User.objects.create_superuser(username = "amedee", email = 'amedee@gmail.com', password = 'password123!@', is_superuser = False)