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

    #This is where all the menus are
    MENU1 = """Please choose an option:
    \t1. See device categories.
    \t2. See shopping cart.
    \t3. Close.\n"""

    MENU_CAT = """\t1. Mouses.
    \t2. Keyboards.
    \t3. Phones.
    \t4. PC.
    \t5. Return.\n"""

    MENU_MOUS = """\t1. Logitech g203 ($100.000)
    \t2. Genius Dx-101 ($20.000)
    \t3. Return.\n"""

    MENU_KEY = """\t1. Redragon kumara k552. ($200.000)
    \t2. Logitech mx keys. ($300.000)
    \t3. Return.\n"""

    MENU_PHO = """\t1. iPhone 15. ($5.600.000)
    \t2. Samsung galaxy s23. ($3.000.000)
    \t3. Return.\n"""

    MENU_PC = """\t1. iMac M3. ($8.900.000)
    \t2. Return.\n"""

    MENU_SHOPPING = """\t1. See products on the shopping cart.
    \t2. Deletle an item.
    \t3. Chekcout.
    \t4. Return.
    """

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
                            quantity = int(input("How many products do you want?\n"))
                            while quantity < 0:
                                print("Incorrect, please choose a valid option")
                                quantity = int(
                                    input("How many products do you want?\n")
                                )
                            if quantity != 0:
                                print(
                                    "The product/s was/were added to the shopping cart\n"
                                )
                                ShpCrt.add_item(option2, mouse, quantity)
                            break

                        mouse = int(input(MENU_MOUS))

                elif option2 == 2:

                    keyboard = int(input(MENU_KEY))
                    while keyboard != 3:
                        if keyboard in (1, 2):
                            quantity = int(input("How many products do you want?\n"))
                            while quantity < 0:
                                print("Incorrect, please choose a valid option")
                                quantity = int(
                                    input("How many products do you want?\n")
                                )
                            if quantity != 0:
                                print(
                                    "The product/s was/were added to the shopping cart\n"
                                )
                                ShpCrt.add_item(option2, keyboard, quantity)
                            break

                        keyboard = int(input(MENU_KEY))

                elif option2 == 3:

                    phone = int(input(MENU_PHO))
                    while phone != 3:
                        if phone in (1, 2):
                            quantity = int(input("How many products do you want?\n"))
                            while quantity < 0:
                                print("Incorrect, please choose a valid option")
                                quantity = int(
                                    input("How many products do you want?\n")
                                )
                            if quantity != 0:
                                print(
                                    "The product/s was/were added to the shopping cart\n"
                                )
                                ShpCrt.add_item(option2, phone, quantity)
                            break

                        phone = int(input(MENU_PHO))

                elif option2 == 4:

                    pc = int(input(MENU_PC))
                    while pc != 2:
                        if pc == 1:
                            quantity = int(input("How many products do you want?\n"))
                            while quantity < 0:
                                print("Incorrect, please choose a valid option")
                                quantity = int(
                                    input("How many products do you want?\n")
                                )
                            if quantity != 0:
                                print(
                                    "The product/s was/were added to the shopping cart\n"
                                )
                                ShpCrt.add_item(option2, pc, quantity)
                            break

                        pc = int(input(MENU_PC))
                else:
                    print("Incorrect, please choose a valid option")

                option2 = int(input(MENU_CAT))

        elif option == 2:

            if ShpCrt.list_length() == 0:
                print("You haven`t add anything to your shopping cart.")
            else:
                option2 = int(input(MENU_SHOPPING))
                while option2 != 4 or option2 != 3:

                    if option2 == 1:

                        print("\tThe products you`ve add to the shopping cart are:\n")
                        for i in range(ShpCrt.list_length()):
                            print(f"\t{ShpCrt.show_item(i)}")
                            print("\n")
                        print(f"with a total cost of: {ShpCrt.money()}\n")

                    elif option2 == 2:

                        print("\tChoose the number of a product for delete it:\n")
                        for i in range(ShpCrt.list_length()):

                            print(f"\t {i+1}. {ShpCrt.show_item(i)}")
                            print("\n")

                        delete = int(input())
                        while delete < 1 or delete > (ShpCrt.list_length()):
                            print("Please, enter a valid number")
                            delete = int(input())

                        ShpCrt.deletle_item(delete - 1)

                    elif option2 == 3:

                        confirmation = input(
                            "Are you sure do you want to checkout? write: (YES)"
                        )
                        if confirmation == "YES":
                            confirm_data = 0
                            while confirm_data == 0:
                                name = input("Please enter your full name:\n")
                                email = input("Please enter an email:\n")
                                location = input("Please enter a location:\n")
                                credit_card = input(
                                    "Please enter a credit or debit card\n"
                                )

                                confirm_data = int(
                                    input(
                                        "Are all this personal information correct? (0 for no)\n"
                                    )
                                )
                                ShpCrt.checkout(name, email, location, credit_card)
                                print("You have been succesfully bought the items")
                                ShpCrt.finish()

                    if ShpCrt.list_length() == 0 and option2 != 2:
                        print("There are no more items on the shopping cart.")
                        break

                    option2 = int(input(MENU_SHOPPING))

        else:
            print("Incorrect, please choose a valid option")

        option = int(input(MENU1))
