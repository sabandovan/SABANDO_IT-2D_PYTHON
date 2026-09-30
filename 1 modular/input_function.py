def ask_yes_no(message):
    while True:
        answer = input(message).lower().strip()

        if answer == "yes" or answer == "y":
            return True

        elif answer == "no" or answer == "n":
            return False

        else:
            print("Invalid input. Please enter yes or no.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0.")

        except ValueError:
            print("Invalid quantity. Please enter a number.")
