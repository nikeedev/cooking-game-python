print("Loading all needed things, please show patient :)")
import random#temporally
print("...")
import time
water_enough = False
potato_enough = False
carrot_enough = False
water = 120 #desiliters
potato = 1000 #grams
carrot = 12 #12 carrots
meat_packages = 0 # going to be 20 meat packages
meat_achivement = False
soup = 0
time.sleep(2)
print("Hello and welcome to Cooking Game! v.0.3.03")
input("click ENTER to continue...")
print("What is your name or in this case nickname?")
username = input("My nickname is... ")
print("Hello " + username + ". Nice, now can we begin to cook!")
print("Okay, We're ready!")
input("click ENTER to continue...")
print("Lets begin with making some soup!")
input("click ENTER to continue...")
print("In this game you have values of ingredients, meaning that you can't make very much food.")
input("click ENTER to continue...")
print("But we should have it enough to make some Soup!")
input("click ENTER to continue...")

while True:
    print("List of Coammands:      ")
    print("                   Recipes")
    print("                   Inventory")
    print("                   Make something")
    print("                   Market(Sell and Buy food)")
    command = input("                   ")
    if water < 0:
        water = 0
    if potato < 0:
        potato = 0
    if carrot < 0:
        carrot = 0
    if meat_achivement == False:
        if soup == 1:
            meat_achivement = True
            print("You got Meat achievement meaning you can have meat, in inventory")
            meat_packages += 20

    if "recipe" in command:
        print("                   Current Recipes:")
        print("                   ")
        print("                   Soup:")
        print("                         Water: 10 Desiliters")
        print("                         Potato: 200 grams")
        print("                         Carrots: 3")
    if "inventory" in command:
        print("                   You have ", water, " desiliters of water")
        print("                   You have ", potato, " grams of potato")
        print("                   You have ", carrot, " carrots")
        print("                   You have ", soup, "soup")
        if meat_achivement == True:
                    print("                   You have ", meat_packages, "meat packages")
        print("                   Tip: If you have small amount of required amount of ingredients, you won't be able to make food!")
    if "make something" in command:
        print("                   Write name of any food above:")
        print("                   Soup")
        make_something = input("                   ")
        if make_something == "soup":
            print("In order to make Soup, you need self write in amounts of ingrendients. If you don't remember you must check recipes!")
            soup_water = int(input("Write desiliters of water you want to add: "))
            soup_potato = int(input("Write grams of potatoes you want to add: "))
            soup_carrot = int(input("Write amount of carrot(s) you want to add: "))
            if soup_water >= 10:
                water = water - soup_water
                water_enough = True
            if soup_potato >= 200:
                potato = potato - soup_potato
                potato_enough = True
            if soup_carrot >= 3:
                carrot = carrot - soup_carrot
                carrot_enough = True
            if water_enough == True and potato_enough == True and carrot_enough == True:
                print("Yeah! All ingredients is here! You succesfully made some Soup!")
                print("- You got 1 Soup! It lies in inventory now -")
                soup = soup + 1
                water
            elif water_enough == False or potato_enough == False or carrot_enough == False:
                print("You can't make soup, because you dont have enough ingredients!")
                print("You have " + water + ", instead of 10 desiliters!")
                print("You have " + potato + ", instead of 200 grams!")
                print("You have " + carrot + ", instead of 3 carrots!")
            water_enough = False
            potato_enough = False
            carrot_enough = False
    if "market" in command:
        print("Welcome to The Market!")
        time.sleep(2)
        print("Here, can you buy and sell things, such like food.")
        time.sleep(3)
        print("And here it is!")
        time.sleep(2)
        print("List of Market commands:")
        print("                          Sell")
        print("                          Buy")
        print("                          Exit")
        market_commands = input()
        if "exit" in market_commands:
            continue
        if "Sell" in market_commands:
            print("You can sell only food you made.")
            print("You have ", soup, " to sell.")
            print("If you want to sell write: Sell and name of food you want to sell.")
    else: 
        continue 


