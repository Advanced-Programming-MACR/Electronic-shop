"""
This module is about the shopping cart and all its functionalities.

Copyright (C) 2024  Miguel Andres Contreras Rodriguez <macontrerasr@udistrital.edu.co>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from abc import ABC, abstractmethod

# =================================== Abstract Shoping Cart  ==================================#


class AbstractShoppingCart(ABC):
    """This abstract class is for the shopping cart"""

    @abstractmethod
    def add_item(self, a: str) -> None:
        """This is an abstract method for adding an item.

        This abstract method, adds an item to a list, for knowing the items
        the person has added to the shoppgin cart.

        Args:
            a (str): The item that will be add.

        Returns:
            This method doesn`t return anything.
        """

    @abstractmethod
    def deletle_item(self, a: str) -> None:
        """This is an abstract method for deleting an item.

        This abstract method, deletes an item to a list, just if the person decides
        to not buying something.

        Args:
            a (str): The item that will be delete.

        Returns:
            This method doesn`t return anything.
        """

    @abstractmethod
    def send_item(self, a: str) -> str:
        """This abstract method sends the info of an item.

        This abstract method is for sending the item that is requiered.

        Args:
            a(int): the id of the item.

        Returns:
            The element on the list.
        """


# ============================= Concrete Shoping Cart  ==================================#


class ShoppingCart(AbstractShoppingCart):
    """This is the concrete class of the Shopping Cart"""

    def __init__(self) -> None:
        self.__products = [None]

    def add_item(self, a: str) -> None:
        """This method adds an item to products list.

        This method adds the "a" item to the list of the shopping cart.

        Args:
            a(int): the item that will be add.

        Returns:
            This method doesn`t returns anything.
        """
        a = a.capitalize
        self.__products.append(a)

    def deletle_item(self, a: str) -> None:
        """This method delete an item of the products list.

        This method delete the "a" item of the list of the shopping cart.

        Args:
            a(int): the item that will be delete.

        Returns:
            This method doesn`t returns anything.
        """

        a = a.capitalize
        self.__products.remove(a)

    def send_item(self, a: str) -> str:
        pass

    def list_length(self) -> int:
        """This method shows the lenght of products.

        This method shows the number of products that have been added to the shopping cart.

        Args:
            This method doesn`t have arguments.

        Returns:
            An integer number with the lenght of the list.
        """
                
        return self.__products.__len__
