MENU = {
    "e": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "l": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "c": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

sources={
    "water": 300,
    "milk":200,
    "coffee":100,
}
def sufficient_source(d_e):
    """the func to check the sources """
    global counter
    counter= 0
    for key in sources:
        if sources[key] >= d_e[key]:
            print(f"{key} is sufficient!")
            counter += 1
        else:
            print(f"sorry,there isn't enough {key}.")

def process_coin(m):
    print("plz enter coins.")
    q = int(input("how many quarters?"))
    d = int(input("how many dimes?"))
    n = int(input("how many nickles?"))
    p = int(input("how many pennies?"))
    m += q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    return m

def money_check(o,d_c):
    """the func to check the price and money to serve the coffee """
    global money
    global money_etc
    #print(d_c)
    if o=="l":
        o="latte"
    elif o=="c":
        o="cappuccino"
    elif o=="e":
        o="espresso"

    money_etc = round(money - d_c,2)
    #print(money_etc)
    if money==d_c:
        print(f"here is your {o}. enjoy it.\nmoney=${money_etc}")
        return True
    elif money> d_c:
        print(f"here is your {o}. enjoy it.\nextra money= ${money_etc}")
        return True
    else:
        print(f"you have less money= ${abs(money_etc)}")

#TODO:1.ask for coffee type ,report , off button
money_etc=0
money=0
is_working=True
while is_working:
    order=input("what would u like? (espresso:'e',latte:'l',cappuccino:'c')\n").lower()
    if order=="off":
        if money_etc>0:
            print(f"your money=$ {money_etc} is refunded")
        print("the machine is off. good bye")
        is_working=False
    elif order=="report":
        print(f"water={sources['water']}ml,\nmilk={sources['milk']}ml,\ncoffee={sources['coffee']}gr,\nmoney={money_etc}")

# TODO:3.check coins
    else:
        drink=MENU[order]
        print(drink)
        sufficient_source(drink["ingredients"])
        if counter==3:
            #print("all the sources are sufficient!")
            money=process_coin(money)
            print(f"your payment is ${money}")
# TODO:4.transaction successful?
# TODO:5.make coffee
            if money_check(order,drink["cost"]):
# TODO:2.check resources
                for key in sources:
                    sources[key]-=MENU[order]["ingredients"][key]
                    print(key,sources[key])
