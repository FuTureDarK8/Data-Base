import unittest
from entities import User
from use_cases import UserManager
from adapters import InMemoryUserRepository

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_repository = InMemoryUserRepository()
        self.user_manager = UserManager(self.user_repository)

    def test_create_user(self):
        email = "test@example.com"
        password = "securepassword"
        role = "User"
        
        user = self.user_manager.create_user(email, password, role)
        
        self.assertEqual(user.email, email)
        self.assertEqual(user.role, role)

    def test_create_user_duplicate_email(self):
        email = "test@example.com"
        password = "securepassword"
        role = "User"
        
        self.user_manager.create_user(email, password, role)
        
        with self.assertRaises(ValueError):
            self.user_manager.create_user(email, password, role)

if __name__ == '__main__':
    unittest.main()