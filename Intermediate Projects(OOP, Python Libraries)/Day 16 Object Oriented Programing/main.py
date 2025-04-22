from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
user_choice = ""
is_active = True




while is_active :
    user_choice = input(f"What would you like? ({menu.get_items()}):").lower()
    if user_choice == "report":
        coffee_maker.report()
        money.report()
        
    elif user_choice == "off" :
        is_active = False
    else:
        selected = menu.find_drink(user_choice)
        if selected:
                
            if coffee_maker.is_resource_sufficient(selected) : 
                if money.make_payment(selected.cost) :
                    coffee_maker.make_coffee(selected)
   

        
        
    



       


                  
        



