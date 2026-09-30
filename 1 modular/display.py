from menu import menu


def display_menu():
    print("\n======================================")
    print("          VAN'S FAST FOOD")
    print("======================================")
    print("MENU")
    print("--------------------------------------")

    for item, price in menu.items():
        print(item, "- P", format(price, ".2f"))

    print("======================================")


def print_receipt(orders):
    subtotal = 0

    for item, quantity in orders.items():
        price = menu[item]
        subtotal += price * quantity

    if subtotal >= 500:
        discount = subtotal * 0.10
    elif subtotal >= 300:
        discount = subtotal * 0.05
    else:
        discount = 0

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
