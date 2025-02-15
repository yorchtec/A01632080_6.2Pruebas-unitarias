"""Unitest"""
import unittest
import os
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """Class creating"""
    def setUp(self):
        """Improve coding with TestHotel"""
        self.hotel = Hotel('Hotel A', ['Location A', 'Location B'], [101, 102, 201, 202, 203, 301, 302, 303, 401, 402, 403], [101,102, 508, '0', 303, 302])

    def test_create_hotel(self):
        """Check if creating a hotel works"""
        self.hotel.create_hotel()
        self.assertTrue(os.path.exists('Hotel A.json'))

    def test_display_hotel_info(self):
        """Check if displayng a hotel works"""
        info = self.hotel.display_hotel_info()
        self.assertEqual(info['name'], 'Hotel A')

    def test_modify_hotel_info(self):
        """Check if modifyng a hotel works"""
        self.hotel.modify_hotel_info(name='New Name')
        self.assertEqual(self.hotel.name, 'New Name')

    def test_reserve_room(self):
        """Check if reserving a hotel works"""
        result = self.hotel.reserve_room(103)
        self.assertTrue(result)

    def test_cancel_reservation(self):
        """Check if cancelling a reservation works"""
        self.hotel.reserve_room(103)
        result = self.hotel.cancel_reservation(103)
        self.assertTrue(result)

    def test_delete_hotel(self):
        """Check if deleting ahotel works"""
        self.hotel.create_hotel()
        self.hotel.delete_hotel()
        self.assertFalse(os.path.exists('Test Hotel.json'))


if __name__ == '__main__':
    unittest.main()
