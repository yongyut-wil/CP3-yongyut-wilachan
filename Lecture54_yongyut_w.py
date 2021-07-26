def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Wrong Username or Password! Please Try Again.")
        return login()


def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. exit")
    return menuSelect()


def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        pricevat = int(input("Input Total Price : "))
        print("Total Price (VAT 7% Included) is", vatCalculator(pricevat), "THB")
        return showMenu()
    elif userSelected == 2:
        print("Total Price (VAT 7% Included) is", priceCalculator(), "THB")
        return showMenu()
    elif userSelected == 3:
        return exit()
    else:
        print("Please select available actions!")
        return showMenu()


def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result


def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print("Total Price (VAT 7% NOT Included", price1+price2)
    return vatCalculator(price1 + price2)


login()