# ============================================
# PRELIM PERFORMANCE TASK
# RESTAURANT ORDERING SYSTEM - OOP VERSION
# ============================================

from ordering_system import RestaurantOrderingSystem


# ---------- MAIN PROGRAM ----------
def main():

    # Create an object
    ordering_system = RestaurantOrderingSystem()

    print("\n======================================")
    print("     WELCOME TO VAN'S FAST FOOD")
    print("======================================")

    # Display menu
    ordering_system.display_menu()

    # Ask if customer wants to order
    wants_order = ordering_system.ask_yes_no(
        "Would you like to order? (yes/no): "
    )

    if wants_order == False:
        print("\nThank you for visiting!")
        print("Goodbye!")
        return

    # Get customer's orders
    ordering_system.get_order()

    # Print receipt
    ordering_system.print_receipt()


# ---------- START PROGRAM ----------
if __name__ == "__main__":
    main()
