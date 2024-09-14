"""
This module is for the code of an electronic shop.

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

from shopping_cart import ShoppingCart

# ================================= Client CLI ===========================================#

if __name__ == "__main__":

    MENU1 = """Please choose an option:
    \t1. See device categories.
    \t2. See shopping cart.
    \t3. Close.\n"""

    MENU_CAT = """\t1. Mouses.
    \t2. Keyboards.
    \t3. Phones.
    \t4. PC.
    \t5. Return.\n"""

    MENU_MOUS = """\t1. Logitech g203
    \t2. Genius Dx-101
    \t3. Return.\n"""

    MENU_KEY = """\t1. Redragon kumara k552.
    \t2. Logitech mx keys.
    \t3. Return.\n"""

    MENU_PHO = """\t1. iPhone 15.
    \t2. Samsung galaxy s23.
    \t3. Return.\n"""

    MENU_PC = """\t1. iMac M3.
    \t2. Return.\n"""

    ShpCrt = ShoppingCart()

    print("Welcome to our Electronic shop")

    option = int(input(MENU1))
    while option != 3:
        if option == 1:
            option2 = int(input(MENU_CAT))
            while option2 != 5:
                if option2 == 1:
                    mouse = int(input(MENU_MOUS))
                    while mouse != 3:
                        if mouse in (1, 2):
                            quantity = int(input("How many products do you want?"))
                            while quantity < 0:
                                if quantity != 0:
                                    print("The product/s was/were added to the shopping cart")
                                    ShpCrt.add_item(option2,mouse,quantity)
                            break
                        else:
                            print("Incorrect, please choose a valid option")

                        mouse = int(input(MENU_MOUS))

                elif option2 == 2:

                    keyboard = int(input(MENU_KEY))
                    while keyboard != 3:
                        if keyboard in (1, 2):
                            quantity = int(input("How many products do you want?"))
                            while quantity < 0:
                                if quantity != 0:
                                    print("The product/s was/were added to the shopping cart")
                                    ShpCrt.add_item(option2,keyboard,quantity)
                            break
                        else:
                            print("Incorrect, please choose a valid option")

                        keyboard = int(input(MENU_KEY))

                elif option2 == 3:

                    phone = int(input(MENU_PHO))
                    while phone != 3:
                        if phone in (1, 2):
                            quantity = int(input("How many products do you want?"))
                            while quantity < 0:
                                if quantity != 0:
                                    print("The product/s was/were added to the shopping cart")
                                    ShpCrt.add_item(option2,phone,quantity)
                            break
                        else:
                            print("Incorrect, please choose a valid option")

                        phone = int(input(MENU_PHO))
                elif option2 == 4:
                    pc = int(input(MENU_PC))
                    while pc != 2:
                        if pc == 1:
                            quantity = int(input("How many products do you want?"))
                            while quantity < 0:
                                if quantity != 0:
                                    print("The product/s was/were added to the shopping cart")
                                    ShpCrt.add_item(option2,pc,quantity)
                            break
                        else:
                            print("Incorrect, please choose a valid option")

                        pc = int(input(MENU_PC))
                else:
                    print("Incorrect, please choose a valid option")

                option2 = int(input(MENU_CAT))

        elif option == 2:
            if ShpCrt.__sizeof__() == 0:
                print("You haven`t add anything to your shopping cart.")
            else:
                for i in range(0, ShpCrt.__sizeof__):
                    pass

        else:
            print("Incorrect, please choose a valid option")

        option = int(input(MENU1))
