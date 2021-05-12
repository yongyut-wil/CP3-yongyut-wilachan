usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "admin"  and passwordInput == "1234":
        print("----- Welcome to water Shop -----")
        print("1. Minaral Water  20 Thb")
        print("2. Drinking Water 10 Thb")
        userSelected = int(input(">>"))
        if userSelected == 1:
            rateMinaral = 20
            amount = int(input("Amount : "))
            print ("result  = ",rateMinaral*amount ,"Thb.")
        elif userSelected == 2:
            rateDrink = 10
            amount = int(input("Amount : "))
            print("result  = ", rateDrink * amount , "Thb.")
