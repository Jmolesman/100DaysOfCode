from time import process_time_ns
from traceback import print_tb


resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": {
        "Quarter": 0,
        "Dime": 0,
        "Nickel": 0,
        "Penny": 0
    }
}

coinValues = {
        "Quarter": 0.25,
        "Dime": 0.10,
        "Nickel": 0.05,
        "Penny": 0.01
}

drinks = {
    "Espresso":{
        "Water":50,
        "Coffee": 18,
        "Price": 1.50
    },
    "Latte": {
        "Water": 200,
        "Milk": 150,
        "Coffee": 24,
        "Price": 2.50
    },
    "Cappuccino":{
        "Water": 250,
        "Milk": 100,
        "Coffee": 24,
        "Price": 3.00
    }
}

def report():
    for resource,quantity in resources.items():
        if (resource == "Money"):
            total = 0
            for coinName,quantity in resources["Money"].items():
                total += resources["Money"][coinName] * coinValues[coinName]
            print(f"Money = ${total}")
        elif (resource == "Water" or resource == "Milk"):
            print(f"{resource} = {quantity}ml")
        else:
            print(f"{resource} = {quantity}g")

def insertCoins(drinkName):
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    resources["Money"]["Quarter"] += quarters
    resources["Money"]["Dime"] += dimes
    resources["Money"]["Nickel"] += nickels
    resources["Money"]["Penny"] += pennies

    total = 0
    total += coinValues["Quarter"]* quarters
    total += coinValues["Dime"]* dimes
    total += coinValues["Nickel"] * nickels
    total += coinValues["Penny"] * pennies


    if (total < returnPrice(drinkName)):
        print("Sorry thats not enought money. Money refunded")
        return False
    elif (total > returnPrice(drinkName)):
        diff = round(total - returnPrice(drinkName),2)
        removeCoins(diff)
        print(f"Here is ${diff} in change.")
        return True
    else:
        return True

def removeCoins(difference):
    #recorremos todas las monedas y sus cantidades
    for name, quantity in resources["Money"].items():
        coinName = name
        coinQuantity = quantity

        #si la cantidad de la moneda evaluada es mayor o igual a 1, se puede usar para devolver
        #como cambio
        if (coinQuantity >= 1):
            for quantity in range (1,coinQuantity):
                if (difference >= coinValues[coinName]):
                    difference -= coinValues[coinName]
                    resources["Money"][coinName] -=1
                else:
                    break

def returnPrice(drinkName):
    return drinks[drinkName]["Price"]

def bootUp():
    return input("What would you like? (espresso/latte/cappuccino): ").lower().capitalize()

def removeResources(drinkName):
    resources["Milk"] -= drinks[drinkName]["Milk"]
    resources["Coffee"] -= drinks[drinkName]["Coffee"]
    resources["Water"] -= drinks[drinkName]["Water"]

def checkResources(drinkName):
    if (drinks[drinkName]["Milk"] > resources["Milk"]):
        print(f'Not enought Milk needed for the drink {drinks[drinkName]["Milk"]} have right now {resources["Milk"]}')
        return False
    if (drinks[drinkName]["Coffee"] > resources["Coffee"]):
        print(f'Not enought Coffee needed for the drink {drinks[drinkName]["Coffee"]} have right now {resources["Coffee"]}')
        return False
    if (drinks[drinkName]["Water"] > resources["Water"]):
        print(f'Not enought Water needed for the drink {drinks[drinkName]["Water"]} have right now {resources["Water"]}')
        return False
    return True

def optionMenu(option):
    global continueCoffee
    if (option == "Exit"):
        continueCoffee = False
    elif(option == "Espresso" or option == "Latte" or option == "Cappuccino"):
        if(checkResources(option)):
            if (insertCoins(option)):
                removeResources(option)
                print(f"Have a nice day, enjoy your {option}!")
    elif (option == "Report"):
        report()
    else:
        print("Wrong answer, please select a correct option.")

continueCoffee = True

while (continueCoffee):
    option = bootUp()
    optionMenu(option)


