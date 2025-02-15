"""This code is class"""
import json
import os


class Customer:
    """Define the class of the customer"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_customer(self):
        """Method to create a new customer"""
        with open(f'{self.name}.json', 'w', encoding='utf-8') as file:
            json.dump(self.__dict__, file)

    def delete_customer(self):
        """ Method to delete a customer"""
        os.remove(f'{self.name}.json')

    def display_customer_info(self):
        """Method to display the information of a customer"""
        return self.__dict__

    def modify_customer_info(self, name=None, email=None):
        """Method to modify the information of a customer"""
        if name:
            self.name = name
        if email:
            self.email = email
        self.create_customer()
