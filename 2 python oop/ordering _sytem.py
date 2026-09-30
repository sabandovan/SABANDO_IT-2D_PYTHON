# ============================================
# PRELIM PERFORMANCE TASK
# RESTAURANT ORDERING SYSTEM - OOP VERSION
# ============================================


class RestaurantOrderingSystem:

    def __init__(self):
        self.menu = {
            "Burger": 50.00,
            "Fries": 35.00,
            "Chicken": 85.00,
            "Spaghetti": 75.00,
            "Soft Drink": 25.00,
            "Ice Cream": 40.00
        }

        self.orders = {}

    # ---------- DISPLAY MENU ----------
    def display_menu(self):
        print("\n======================================")
        print("          VAN'S FAST FOOD")
        print("======================================")
        print("MENU")
        print("--------------------------------------")

        for item, price in self.menu.items():
            print(item, "- P", format(price, ".2f"))

        print("======================================")

    # ---------- ASK YES OR NO ----------
    def ask_yes_no(self, message):
        while True:
            answer = input(message).lower().strip()

            if answer == "yes" or answer == "y":
                return True

            elif answer == "no" or answer == "n":
                return False

            else:
                print("Invalid input. Please enter yes or no.")

    # ---------- GET QUANTITY ----------
    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Invalid quantity. Please enter a number.")

    # ---------- GET ORDER ----------
    def get_order(self):
        while True:
            print("\nAvailable Items:")

            for item in self.menu:
                print("-", item)

            item_name = input("Enter menu item: ").strip()

            # Check if item exists
            selected_item = ""

            for item in self.menu:
                if item.lower() == item_name.lower():
                    selected_item = item
                    break

            if selected_item == "":
                print("Invalid menu item!")
                print("Please choose an item from the menu.")
                continue

            quantity = self.get_quantity()

            # Save order
            if selected_item in self.orders:
                self.orders[selected_item] += quantity
            else:
                self.orders[selected_item] = quantity

            print("Order added successfully!")

            another = self.ask_yes_no(
                "Would you like to order another item? (yes/no): "
            )

            if not another:
                break

    # ---------- CALCULATE TOTAL ----------
    def calculate_total(self):
        subtotal = 0

        for item, quantity in self.orders.items():
            price = self.menu[item]
            item_total = price * quantity
            subtotal += item_total

        return subtotal

    # ---------- CALCULATE DISCOUNT ----------
    def calculate_discount(self, subtotal):
        if subtotal >= 500:
            discount = subtotal * 0.10

        elif subtotal >= 300:
            discount = subtotal * 0.05

        else:
            discount = 0

        return discount

    # ---------- PRINT RECEIPT ----------
    def print_receipt(self):
        subtotal = self.calculate_total()
        discount = self.calculate_discount(subtotal)
        total = subtotal - discount

        print("\n")
        print("==============================================")
        print("             VAN'S FAST FOOD")
        print("              OFFICIAL RECEIPT")
        print("==============================================")
        print("Item              Qty     Price       Total")
        print("----------------------------------------------")

        for item, quantity in self.orders.items():
            price = self.menu[item]
            item_total = price * quantity

            print(
                item,
                " " * max(1, 18 - len(item)),
                quantity,
                "     P" + format(price, ".2f"),
                "     P" + format(item_total, ".2f")
            )

        print("----------------------------------------------")
        print("Subtotal:                         P" + format(subtotal, ".2f"))
        print("Discount:                         P" + format(discount, ".2f"))
        print("TOTAL:                            P" + format(total, ".2f"))
        print("==============================================")
        print("        Thank you for ordering!")
        print("             Please come again!")
        print("==============================================")

    # ---------- RUN PROGRAM ----------
    def run(self):
        print("\n======================================")
        print("     WELCOME TO VAN'S FAST FOOD")
        print("======================================")

        self.display_menu()

        wants_order = self.ask_yes_no(
            "Would you like to order? (yes/no): "
        )

        if not wants_order:
            print("\nThank you for visiting!")
            print("Goodbye!")
            return

        self.get_order()

        self.print_receipt()
