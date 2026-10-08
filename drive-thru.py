def main():
    welcome()
    choice = int(input("Select your order: "))
    get_item(choice)
def welcome():
    menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]
    print("Welcome to burgers chumas!")
    print("Here's the menu:")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[food]}")


def get_item(order):
    kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    if 1 <= order <= 5:
        print(kitchen[order - 1])
    else:
        print("not in our menu.")

    # if order == 1:
    #     print("🍔")
    # elif order == 2:
    #     print("🍟")
    # elif order == 3:
    #     print("🥤")
    # elif order == 4:
    #     print("🍦")
    # elif order == 5:
    #     print("🍪")
    # else:
    #     print("that is not in the menu pick something 😡")










if __name__ == "__main__":
    main()
