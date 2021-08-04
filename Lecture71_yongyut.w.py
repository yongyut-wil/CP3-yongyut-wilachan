menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        totalPrice += int(priceList[number])
    print("Total :", totalPrice)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()