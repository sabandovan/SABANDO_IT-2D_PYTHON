# ============================================
# PRELIM PERFORMANCE TASK
# RESTAURANT ORDERING SYSTEM
# ============================================

# ---------- MENU ----------
menu = {
    "Burger": 50.00,
    "Fries": 35.00,
    "Chicken": 85.00,
    "Spaghetti": 75.00,
    "Soft Drink": 25.00,
    "Ice Cream": 40.00
}


# ---------- DISPLAY MENU ----------
def display_menu():
    print("\n======================================")
    print("          VAN'S FAST FOOD")
    print("======================================")
    print("MENU")
    print("--------------------------------------")

    for item, price in menu.items():
        print(item, "- P", format(price, ".2f"))

    print("======================================")


# ---------- ASK YES OR NO ----------
def ask_yes_no(message):
    while True:
        answer = input(message).lower().strip()

        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Invalid input. Please enter yes or no.")


# ---------- GET ORDER ----------
def get_order():
    orders = {}

    while True:
        print("\nAvailable Items:")

        for item in menu:
            print("-", item)

        item_name = input("Enter menu item: ").strip()

        # Check if item exists
        selected_item = ""

        for item in menu:
            if item.lower() == item_name.lower():
                selected_item = item

        if selected_item == "":
            print("Invalid menu item!")
            print("Please choose an item from the menu.")
            continue

        # Get quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Invalid quantity. Please enter a number.")

        # Save order
        if selected_item in orders:
            orders[selected_item] = orders[selected_item] + quantity
        else:
            orders[selected_item] = quantity

        print("Order added successfully!")

        # Ask for another item
        another = ask_yes_no(
            "Would you like to order another item? (yes/no): "
        )

        if another == False:
            break

    return orders


# ---------- CALCULATE TOTAL ----------
def calculate_total(orders):
    subtotal = 0

    for item, quantity in orders.items():
        price = menu[item]
        item_total = price * quantity
        subtotal = subtotal + item_total

    return subtotal


# ---------- CALCULATE DISCOUNT ----------
def calculate_discount(subtotal):

    if subtotal >= 500:
        discount = subtotal * 0.10
    elif subtotal >= 300:
        discount = subtotal * 0.05
    else:
        discount = 0

    return discount


# ---------- PRINT RECEIPT ----------
def print_receipt(orders):

    subtotal = calculate_total(orders)
    discount = calculate_discount(subtotal)
    total = subtotal - discount

    print("\n")
    print("==============================================")
    print("             VAN'S FAST FOOD")
    print("              OFFICIAL RECEIPT")
    print("==============================================")
    print("Item              Qty     Price       Total")
    print("----------------------------------------------")

    for item, quantity in orders.items():

        price = menu[item]
        item_total = price * quantity

        print(
            item,
            " " * (18 - len(item)),
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


# ---------- MAIN PROGRAM ----------
def main():

    print("\n======================================")
    print("     WELCOME TO VAN'S FAST FOOD")
    print("======================================")

    # Display menu
    display_menu()

    # Ask if customer wants to order
    wants_order = ask_yes_no(
        "Would you like to order? (yes/no): "
    )

    if wants_order == False:
        print("\nThank you for visiting!")
        print("Goodbye!")
        return

    # Get customer's orders
    orders = get_order()

    # Calculate and print receipt
    print_receipt(orders)


# ---------- START PROGRAM ----------
main()