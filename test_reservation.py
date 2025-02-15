"""Reservation testing"""
import unittest
import os
from reservation import Reservation
from customer import Customer
from hotel import Hotel


class TestReservation(unittest.TestCase):
    """Unitest for reservation"""
    def setUp(self):
        """Create a setup for easier backtracking"""
        self.customer = Customer('Test Customer', 'test@example.com')
        self.hotel = Hotel('Hotel A', ['Location A', 'Location B'], [101, 102, 201, 202, 203, 301, 302, 303, 401, 402, 403], [101,102, 508, '0', 303, 302])
        self.reservation = Reservation(self.customer, self.hotel, 101)

    def test_create_reservation(self):
        """Test new reservations"""
        self.reservation.create_reservation()
        self.assertTrue(os.path.exists('Test Customer_Test Hotel.json'))

    def test_cancel_reservation(self):
        """Test reservation cancelation"""
        self.reservation.create_reservation()
        self.reservation.cancel_reservation()
        self.assertFalse(os.path.exists('Test Customer_Test Hotel.json'))


if __name__ == '__main__':
    unittest.main()
