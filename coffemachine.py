MENU = {
    "madras_coffee": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "American_coffee": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "strong_coffee": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profits=0

def prices(ordered_item,ingredient):
    for item in ingredient:
        if ingredient[item]>resources[item]:
            print(f"sorry you dont have sufficient items{item}")
            return True
    return True
def process_coins():
    coin_1=int(input("enter the 1 rupee coin"))*0.5
    coin_2=int(input("enter the two rupee_coin"))*2
    coin_3=int(input("enter the 5 rupee coin"))*5
    return(f'{coin_1}+{coin_2}+{coin_2}')
def check_resources(amount_needed,drink_coast):
    global profits
    if amount_needed >=drink_coast:
        profits+=drink_coast
        print(f"sufficient balance")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
 
def make_coffe(drink_name,ordered_items):
    for i in ordered_items:
        resources[i]-=ordered_items[i]
        print(f"you are {drink_name}has done ")
is_done=True
while is_done:
    choice=input("enter which coffe do you like to have madras_coffee ,American_coffee or strong_coffee")
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profits}")
    else:
         drink = MENU[choice]
         if prices(drink,drink['ingredients']):
             payment=process_coins()
             make_coffe(choice,drink["ingredients"])
                 
        
    
