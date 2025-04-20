import menu
coffe_menu = menu.MENU
resources = menu.resources
money = 0
change = 0
is_active = True

def report():
    """print out the remaining resources and the money"""
    for key in resources:
        print(key + " : " + str(resources[key]))

    print(f"${money}")

def calc_resources(resources,ingredients):
    """Check the resources , subtract the ingredients if its possible, returns an error message if not."""
    for key in ingredients:
        if resources.get(key,0) < ingredients[key]:
            print(f"Sorry there is not enough {key}!")
            return None
    for key in ingredients :
        
            resources[key] -= ingredients[key]
                    
    return resources

def calc_coins():
    """returns the value of the inserted coins """
    inserted_coins = 0
    penny = float(input("How many pennies?")) * 0.01
    nickel =float(input("How many nickels?")) * 0.05
    dimes =float(input("How many dimes?")) * 0.10
    quarter =float(input("How many quarters?")) * 0.25

    inserted_coins += sum([penny, nickel,dimes,quarter])

    return inserted_coins


    

       

while is_active:   
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "report":
        report()
    elif user_choice in ["latte", "espresso", "cappuccino"]:
        result = calc_resources(resources,coffe_menu[user_choice]["ingredients"])
        if result is not None :
            resources = result
            inserted_coins = calc_coins()
            if inserted_coins < coffe_menu[user_choice]["cost"] :
                print("Sorry that's not enough money. Money refunded.")
            elif inserted_coins == coffe_menu[user_choice]["cost"] : 
                money += inserted_coins
                print(f"Here is your {user_choice}!☕ Enjoy! ")
        
            elif inserted_coins > coffe_menu[user_choice]["cost"] :
                change = inserted_coins - coffe_menu[user_choice]["cost"]
                money += coffe_menu[user_choice]["cost"]
                print(f"Here is ${change} in change!")
                print(f"Here is your {user_choice}!☕ Enjoy! ")
            

                
        
    
        

    


    





