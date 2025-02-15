"""Customer Unitest"""
import unittest
import os
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Create the testclass for customer"""
    def setUp(self):
        """Create a setup to improve coding"""
        self.customer = Customer(['Test Customer', 106], 'test@example.com')

    def test_create_customer(self):
        """Test the customer creation"""
        self.customer.create_customer()
        self.assertTrue(os.path.exists('Test Customer.json'))

    def test_delete_customer(self):
        """Test Customer deletion"""
        self.customer.create_customer()
        self.customer.delete_customer()
        self.assertFalse(os.path.exists('Test Customer.json'))

    def test_display_customer_info(self):
        """Test customer display"""
        info = self.customer.display_customer_info()
        self.assertEqual(info['name'], 'Test Customer')

    def test_modify_customer_info(self):
        """ Test customer modification"""
        self.customer.modify_customer_info(name='New Name')
        self.assertEqual(self.customer.name, 'New Name')


if __name__ == '__main__':
    unittest.main()
