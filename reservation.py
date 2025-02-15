"""This code is a class"""
import json
import os


class Reservation:
    """Class to book reservations"""
    def __init__(self, customer, hotel, room_number):
        self.customer = customer
        self.hotel = hotel
        self.room_number = room_number

    def create_reservation(self):
        """Method to create a new reservation"""
        reservation = {
            'customer': self.customer.display_customer_info(),
            'hotel': self.hotel.display_hotel_info(),
            'room_number': self.room_number
        }
        with open(f'{self.customer.name}_{self.hotel.name}.json',
                  'w', encoding='utf-8') as file:
            json.dump(reservation, file)

    def cancel_reservation(self):
        """ Method to cancel a reservation"""
        os.remove(f'{self.customer.name}_{self.hotel.name}.json')
