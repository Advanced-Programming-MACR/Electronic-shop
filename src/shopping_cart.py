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
from datetime import datetime

# =================================== Abstract Shoping Cart  ==================================#


class AbstractShoppingCart(ABC):
    """This abstract class is for the shopping cart"""

    @abstractmethod
    def add_item(self, a: int, b: int, c: int) -> None:
        """This is an abstract method for adding an item.

        This abstract method, adds an item to a list, for knowing the items
        the person has added to the shoppgin cart.

        Args:
            a (int): The category of the item.
            b (int): The item that will be add.
            c (int): Quantity of the product.

        Returns:
            This method doesn`t return anything.
        """

    @abstractmethod
    def deletle_item(self, a: int) -> None:
        """This is an abstract method for deleting an item.

        This abstract method, deletes an item to a list, just if the person decides
        to not buying something.

        Args:
            a (int): The item that will be delete.

        Returns:
            This method doesn`t return anything.
        """

    @abstractmethod
    def show_item(self, a: int) -> str:
        """This abstract method sends the info of an item.

        This abstract method is for one of the item from shopping cart list.

        Args:
            a(int): the number of the product on the list.

        Returns:
            The element on the list.
        """

    @abstractmethod
    def checkout(self, a: str, b: str, c: str, d: str) -> None:
        """This abstract method do the checkout.

        This abstract method is for create or modify a file with all checkout data.

        Args:
            a(str): person`s name.
            b(str): person`s email.
            c(str): person`s location.
            d(str): peron`s cerdit or debit card.

        Returns:
            The element on the list.
        """


# ============================= Concrete Shoping Cart  ==================================#


class ShoppingCart(AbstractShoppingCart):
    """This is the concrete class of the Shopping Cart"""

    def __init__(self) -> None:
        self.__products = []
        self.__quantity = []
        self.__prices = []

    def add_item(self, a: int, b: int, c: int) -> None:
        """This method adds an item to products list.

        This method adds the "a" item to the list of the shopping cart.

        Args:
            a (int): The category of the item.
            b (int): The item that will be add.
            c (int): Quantity of the product.

        Returns:
            This method doesn`t returns anything.
        """

        #All this part of the code is just for adding the product to the lists
        if_list = 0
        if a == 1:
            if b == 1:

                for i in range(self.list_length()):
                    if "Logitech g203" == self.__products[i]:
                        num = int(self.__quantity[i] + c)
                        self.__quantity[i] = num
                        if_list = 1

                if if_list == 0:
                    self.__products.append("Logitech g203")
                    self.__quantity.append(c)
                    self.__prices.append(100000)

            elif b == 2:
                for i in range(self.list_length()):
                    if "Genius Dx-101" == self.__products[i]:
                        num = int(self.__quantity[i] + c)
                        self.__quantity[i] = num
                        if_list = 1

                if if_list == 0:
                    self.__products.append("Genius Dx-101")
                    self.__quantity.append(c)
                    self.__prices.append(20000)

        elif a == 2:
            if b == 1:
                for i in range(self.list_length()):
                    if "Redragon kumara k552" == self.__products[i]:
                        num = int(self.__quantity[i] + c)
                        self.__quantity[i] = num
                        if_list = 1

                if if_list == 0:
                    self.__products.append("Redragon kumara k552")
                    self.__quantity.append(c)
                    self.__prices.append(200000)

            elif b == 2:
                for i in range(self.list_length()):
                    if "Logitech mx keys" == self.__products[i]:
                        num = int(self.__quantity[i] + c)
                        self.__quantity[i] = num
                        if_list = 1

                if if_list == 0:
                    self.__products.append("Logitech mx keys")
                    self.__quantity.append(c)
                    self.__prices.append(300000)

        elif a == 3:
            if b == 1:
                for i in range(self.list_length()):
                    if "iPhone 15" == self.__products[i]:
                        num = int(self.__quantity[i] + c)
                        self.__quantity[i] = num
                        if_list = 1

                if if_list == 0:
                    self.__products.append("iPhone 15")
                    self.__quantity.append(c)
                    self.__prices.append(5600000)

            elif b == 2:
                for i in range(self.list_length()):
                    if "Samsung galaxy s23" == self.__products[i]:
                        num = int(self.__quantity[i] + c)
                        self.__quantity[i] = num
                        if_list = 1

                if if_list == 0:
                    self.__products.append("Samsung galaxy s23")
                    self.__quantity.append(c)
                    self.__prices.append(3000000)

        elif a == 4:
            for i in range(self.list_length()):
                if "iMac M3" == self.__products[i]:
                    num = int(self.__quantity[i] + c)
                    self.__quantity[i] = num
                    if_list = 1

                if if_list == 0:
                    self.__products.append("iMac M3")
                    self.__quantity.append(c)
                    self.__prices.append(8900000)

    def deletle_item(self, a: str) -> None:
        """This is a method for deleting an item.

        This abstract method, deletes an item to a list, just if the person decides
        to not buying something.

        Args:
            a (int): The item that will be delete.

        Returns:
            This method doesn`t return anything.
        """
        self.__products.pop(a)
        self.__quantity.pop(a)
        self.__prices.pop(a)

    def show_item(self, a: int) -> str:
        """This abstract method sends the info of an item.

        This abstract method is for one of the item from shopping cart list.

        Args:
            a(int): the number of the product on the list.

        Returns:
            The element on the list.
        """
        return f"{self.__products[a]} --- {self.__quantity[a]}"

    def checkout(self, a: str, b: str, c: str, d: str) -> None:
        """This is a method is for doing the checkout.

        This abstract method is for create or modify a file with all checkout data.

        Args:
            a(str): person`s name.
            b(str): person`s email.
            c(str): person`s location.
            d(str): peron`s cerdit or debit card.

        Returns:
            The element on the list.
        """
        #Just open or create a file and put on it the important information
        with open("Checkout.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{a},{b},{c},{d},bought {self.__products} with a total price of: {self.money}, time: {datetime.now()}"
            )

    def finish(self) -> None:
        """This method workd when the purchase has finished.

        This method just restart all the lists.

        Args:
            This method doesn`t have args.

        Returns:
            This method doesn`t returns anything.
        """

        self.__products.clear()
        self.__quantity.clear()
        self.__prices.clear()

    def money(self) -> int:
        """This method calculate the total price

        This method sum all the products.

        Args:
            This method doesn`t have args.

        Returns:
            An integer number with the total cost of the purchase
        """
        total = 0
        for i in range(self.list_length()):
            total = (self.__prices[i] * self.__quantity[i]) + total
        return total

    def list_length(self) -> int:
        """This method shows the lenght of products.

        This method shows the number of products that have been added to the shopping cart.

        Args:
            This method doesn`t have arguments.

        Returns:
            An integer number with the lenght of the list.
        """
        return len(self.__products)
