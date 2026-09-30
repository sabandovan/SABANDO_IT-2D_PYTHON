from display import display_menu, print_receipt
from input_functions import ask_yes_no
from order_functions import get_order


def main():
    print("\n======================================")
    print("     WELCOME TO VAN'S FAST FOOD")
    print("======================================")

    display_menu()

    wants_order = ask_yes_no(
        "Would you like to order? (yes/no): "
    )

    if not wants_order:
        print("\nThank you for visiting!")
        print("Goodbye!")
        return

    orders = get_order()

    print_receipt(orders)


main()
