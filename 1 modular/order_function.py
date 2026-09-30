from menu import menu
from input_functions import ask_yes_no, get_quantity


def get_order():
    orders = {}

    while True:
        print("\nAvailable Items:")

        for item in menu:
            print("-", item)

        item_name = input("Enter menu item: ").strip()

        selected_item = ""

        for item in menu:
            if item.lower() == item_name.lower():
                selected_item = item
                break

        if selected_item == "":
            print("Invalid menu item!")
            print("Please choose an item from the menu.")
            continue

        quantity = get_quantity()

        if selected_item in orders:
            orders[selected_item] += quantity
        else:
            orders[selected_item] = quantity

        print("Order added successfully!")

        another = ask_yes_no(
            "Would you like to order another item? (yes/no): "
        )

        if not another:
            break

    return orders
