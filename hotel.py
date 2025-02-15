""" Docstring para una clase?"""
import json
import os


class Hotel:
    """ Create the class """
    def __init__(self, name, location, rooms, reservations):
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def create_hotel(self):
        """use this method to create a new hotel to the list"""
        if type(self.name) is str:
            with open(f'{self.name}.json', 'w', encoding='utf-8') as file:
                json.dump(self.__dict__, file)

    def delete_hotel(self):
        "Use this method to delete a hotel"
        os.remove(f'{self.name}.json')

    def display_hotel_info(self):
        """Use this method to """
        return self.__dict__

    def modify_hotel_info(self, name=None, location=None, rooms=None):
        """ Use this method to modify hotel reservation details"""
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms:
            self.rooms = rooms
        self.create_hotel()

    def reserve_room(self, room_number):
        """ Use this method to book a new reservation"""
        if room_number in self.rooms and room_number not in self.reservations:
            self.reservations.append(room_number)
            return True
        return False

    def cancel_reservation(self, room_number):
        """ Reservation cancel """
        if room_number in self.reservations:
            self.reservations.remove(room_number)
            return True
        return False
