print("Loading all needed things, please show patient :)")
print("...")
import time, os, getpass
from about import *


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


username = ""
water_enough = False
potato_enough = False
carrot_enough = False
meat_enough = False
oil_enough = False
flour_enough = False
use_username = True
coins = 0
water = 120  # deciliters
lasagna = 0
baked_lasagna = 0
potato = 1000  # grams
carrot = 12  # 12 carrots
meat_packages = 0  # going to be 20 meat packages
meat_achivement = False
soup = 0
soup_with_meat = 0
bread = 0
level = 0
xp = 0
xp_need = 100
xp_rest = 0
bread_achivement = False
flour = 5000  # grams
oil = 100  # deciliters
time.sleep(2)
print("Hello and welcome to Cooking Game! v.0.6.4! New: Typo Fixing (more info in 'log' command)")
input("press Enter to continue...")
while use_username:
    print("\n\nWhat is your name or in this case nickname?")
    username = input("My nickname is... ")
    agree = input(
        "\n\nDo you want to use this username(write 1), PC username(write 2), or change this username(write 3)? ")
    if agree == "1":
        use_username = False
    elif agree == "2":
        username = getpass.getuser()
        use_username = False
    elif agree == "3":
        continue
print(f"Hello {username}. Nice, now can we begin to cook!")
print("Okay, We're ready!")
input("press Enter to continue...")
print("Lets begin with making some soup!")
input("press Enter to continue...")
print("In this game you have desired values of ingredients in recipes, meaning that you can't make very much food, if you dont have enough ingredients.")
input("press Enter to continue...")
print("But we should have it enough to make some Soup!")
input("press Enter to continue...")

while True:
    if xp == 2:
        print("You achieved 'Bread Achivement'! You can now make bread!")
        bread_achivement = True
    if xp > xp_need:
        xp_rest = xp - xp_need
        xp = xp_rest
        level += 1
        xp_rest = 0
        xp_need *= 1.15
        print("")
        print(f"- New level achieved! - Level {level}, XP {xp} / {xp_need}")
    if water < 0:
        water = 0
    if potato < 0:
        potato = 0
    if carrot < 0:
        carrot = 0
    if coins < 0:
        coins = 0
    if flour < 0:
        flour = 0
    if oil < 0:
        oil = 0
    if meat_packages < 0:
        meat_packages = 0
    if not meat_achivement:
        if soup == 2:
            print("")
            print("")
            print("")
            meat_achivement = True
            print(
                "You got Meat achievement, which means you can have meat in inventory, and you're able to make new Soup type!")
            meat_packages += 20
            print("")
            print("")
            print("")
    print("")
    print("Hello + " + username + "! What do you want to do now?")
    print("List of Commands:      ")
    print("                   Recipes ( Write 'recipe' ) ")
    print("                   Inventory ( Write 'inventory' )")
    print("                   Make something ( Write 'make something' )")
    print("                   Market(Sell and Buy food) ( Write 'market' )")
    print("                   Boosts (Buy and list your boosts!) ( Write 'boosts' )")
    print("                   Info ( Write 'info' )")
    print("                   Update Log ( Write 'update' or 'log' )")
    print("                   Exit ( Write 'exit' ) ")
    command = input("                   ")
    if "recipe" in command:
        clearConsole()
        print("                   Current Recipes:")
        print("                   ")
        print("                   Soup:")
        print("                         Water: 10 Deciliters")
        print("                         Potato: 200 grams")
        print("                         Carrots: 3")
        print("                         ")
        if meat_achivement:
            print("                   Soup With Meatballs:")
            print("                         Water: 12 Deciliters")
            print("                         Potato: 200 grams")
            print("                         Carrots: 3")
            print("                         Meat Packages: 2")
        if bread_achivement:
            print("                   Bread:")
            print("                         Water: 5 Deciliters")
            print("                         Flour: 2 Deciliters")
            print("                         Oil: 1 Deciliters")

    if "inventory" in command:
        clearConsole()
        print("                   You have " + water + " deciliters of water")
        print("                   You have " + potato + " grams of potato")
        print("                   You have " + carrot + " carrots")
        print("                   You have " + soup + " soup")
        if meat_achivement:
            print("                   You have " + meat_packages + " meat packages")
            print("                   You have " + soup_with_meat + " soup with meatballs")

        if bread_achivement:
            print("                         You have" + water + " deciliters of water")
            print("                         You have" + flour + " deciliters of flour")
            print("                         You have " + oil + " deciliters of oil")
            print("                         You have " + bread + " bread")

        print("                   You have " + lasagna + " lasagna's")
        print("                   You have " + baked_lasagna + " baked lasagna's\n")
        print("\n \n                   You have " + coins + " coins")
        print("                   Your level is: Level: " + level + ". XP to next level is: " + xp + " / " + xp_need)
        print(
            "                   Tip: If you have small amount of required amount of ingredients, you won't be able to make food!")
    if "make something" in command:
        clearConsole()
        print("                   Write name of any food above:")
        print("                   Soup")
        if meat_achivement:
            print("                   Soup With Meatballs")
        elif lasagna >= 1:
            print("                   Lasagna")
        elif bread_achivement:
            print("                   Bread")
        make_something = input("                   ")
        if make_something == "soup":
            print(
                "In order to make Soup, you need self write in amounts of ingredients. If you don't remember you must check recipes!")
            soup_water = int(input("Write deciliters of water you want to add: "))
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
            if water_enough and potato_enough and carrot_enough:
                print("Yeah! All ingredients is here! You successfully made some Soup!")
                print("- You got 1 Soup! It lies in inventory now, +10 XP -")
                soup = soup + 1
                xp += 10
            else:
                print("You can't make soup, because you don't have enough ingredients!")
                print("You used " + soup_water + "dl, instead of 10 deciliters!")
                print("You used " + soup_potato + " grams, instead of 200 grams!")
                print("You used " + soup_carrot + " sticks of carrots, instead of 3 carrots!")
            water_enough = False
            potato_enough = False
            carrot_enough = False
            soup_water = 0
            soup_potato = 0
            soup_carrot = 0
        elif meat_achivement:
            if make_something == "soup with meat":
                print(
                    "In order to make Soup with Meatballs, you need self write in amounts of ingredients. If you don't remember you must check recipes!")
                soup_water = int(input("Write deciliters of water you want to add: "))
                soup_potato = int(input("Write grams of potatoes you want to add: "))
                soup_carrot = int(input("Write amount of carrot(s) you want to add: "))
                soup_meat = int(input("Write amount of meat packages you want to add: "))
                if soup_water >= 12:
                    water = water - soup_water
                    water_enough = True
                if soup_potato >= 200:
                    potato = potato - soup_potato
                    potato_enough = True
                if soup_carrot >= 3:
                    carrot = carrot - soup_carrot
                    carrot_enough = True
                if soup_meat >= 2:
                    meat_packages = meat_packages - soup_meat
                    meat_enough = True
                if water_enough and potato_enough and carrot_enough and meat_enough:
                    print("Yeah! All ingredients is here! You successfully made some Soup!")
                    print("- You got 1 Soup with Meatballs! It lies in inventory now, +15 XP -")
                    soup_with_meat += 1
                    xp += 15
                else:
                    print("You can't make soup, because you don't have enough ingredients!")
                    print("You used " + soup_water + "dl of water, instead of 12 deciliters!")
                    print("You used " + soup_potato + " grams of potatoes, instead of 200 grams!")
                    print("You used " + soup_carrot + " sticks of carrots, instead of 3 carrots!")
                    print("You used " + soup_meat + " meat packages, instead of 2 packages")
                water_enough = False
                potato_enough = False
                carrot_enough = False
                meat_enough = False
                soup_water = 0
                soup_potato = 0
                soup_carrot = 0
                soup_meat = 0
        elif lasagna >= 1:
            if "lasagna" in make_something:
                print("You are lucky to buy Lasagna! It costed you much...")
                input("press Enter to continue...")
                print("All you need is to say Yes or Y to make that lasagna...")
                lasagna_accept = input("Write yes/y or no/n: ")
                if "y" or "yes" in lasagna_accept:
                    print("Well you did it. But you lose whole 20 Deciliters of water... :|")
                    input("press Enter to continue...")
                    water -= 20
                    baked_lasagna += 1
                    print("- You made 1 Baked Lasagna -")
                if "n" or "no" in lasagna_accept:
                    print("Well you won't regret next time...")
                    input("Press That Enter button to Continue!!!!!!")
        elif bread_achivement:
            if make_something == "bread":
                print(
                    "In order to make Bread, you need self write in amounts of ingredients. If you don't remember you must check recipes!")
                bread_water = int(input("Write deciliters of water you want to add: "))
                bread_flour = int(input("Write deciliters of flour you want to add: "))
                bread_oil = int(input("Write deciliters of oil you want to add: "))
                if bread_water >= 5:
                    water = water - bread_water
                    water_enough = True
                if bread_flour >= 2:
                    flour = flour - bread_flour
                    flour_enough = True
                if bread_oil >= 1:
                    oil = oil - bread_oil
                    oil_enough = True
                if water_enough and flour_enough and oil_enough:
                    print("Yeah! All ingredients is here! You successfully made some Bread!")
                    print("- You got 1 Bread! It lies in inventory now, +20 XP -")
                    bread += 1
                    xp += 20
                else:
                    print("You can't make Bread, because you don't have enough ingredients!")
                    print("You used " + bread_water + "dl of water, instead of 5 deciliters!")
                    print("You used " + bread_flour + "dl of flour, instead of 2 deciliters!")
                    print("You used " + bread_oil + "dl of oil, instead of 1 deciliters!")
                water_enough = False
                flour_enough = False
                oil_enough = False
                bread_water = 0
                bread_potato = 0
                bread_carrot = 0

        else:
            continue

    if "market" in command:
        clearConsole()
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
        if "sell" in market_commands:
            if soup < 0 or soup_with_meat < 0 or bread < 0:
                print("You don't have anything to sell, redirecting back in 3 sec")
                time.sleep(3)
                continue
            elif soup > 0 or soup_with_meat > 0:
                print("You can sell only food you made.")
                time.sleep(2)
                print("Prices on foods change after time(after updates), so be in right time to get much coins!")
                time.sleep(3)
                print("You can sell " + soup + " soup.")
                if meat_achivement:
                    print("You can sell " + soup_with_meat + " soup with meatballs.")
                if bread_achivement:
                    print("You can sell " + bread + " bread.")
                time.sleep(2)
                print("If you want to sell write: name of food you want to sell.")
                sell_command = input()
                if "soup" in sell_command:
                    print("One soup could be sold for: 25 coins")
                    print(
                        "Want to sell 1 soup for current price? If not, you will be redirected back to main commands!")
                    sell_answer = input("Write yes or no...")
                    if "yes" in sell_answer:
                        print("Selling soup!")
                        soup -= 1
                        time.sleep(2)
                        print("You got 25 coins")
                        coins += 25
                elif meat_achivement:
                    if "soup with meatballs" in sell_command:
                        print("One soup with meatballs could be sold for: 30 coins")
                        print("Want to sell 1 soup with meatballs for current price?")
                        print("If not, you will be redirected back to main commands!")
                        sell_answer = input("Write yes or no...")
                        if "yes" in sell_answer:
                            print("Selling soup!")
                            soup_with_meat -= 1
                            time.sleep(2)
                            print("You got 30 coins")
                            coins += 30
                if bread_achivement:
                    if "bread" in sell_command:
                        print("One bread could be sold for: 35 coins")
                        print("Want to sell 1 bread for current price?")
                        print("If not, you will be redirected back to main commands!")
                        sell_answer = input("Write yes or no...")
                        if "yes" in sell_answer:
                            print("Selling bread!")
                            bread -= 1
                            time.sleep(2)
                            print("You got 30 coins")
                            coins += 30
        if "buy" in market_commands:
            if coins == 0:
                print("You don't have enough money! Leaving Market in 2 sec.")
                time.sleep(2)
                continue
            else:
                print("You can buy vegetables, water and much other!")
                time.sleep(2)
                print("Here is what you can buy:")
                print("Water, 20 deciliters: 10 coins")
                print("Potato, 400 grams: 5 coins")
                print("Carrots, 6 sticks: 7 coins")
                if bread_achivement:
                    print("Flour, 200 grams: 8 coins")
                    print("Oil, 12 deciliters: 10: coins")
                if meat_achivement:
                    print("Meat, 4 packages: 5 coins")
                print("Lasagna, 1: 150 coins(being rich to buy this recommended)")
                time.sleep(3)
                print("Write in commands below what you want to buy:")
                print("Water")
                print("Potato")
                print("Carrot")
                print("Lasagna")
                if bread_achivement:
                    print("Flour")
                    print("Oil")
                if meat_achivement:
                    print("Meat")
                buy_commands = input()
                if "water" in buy_commands:
                    print("Adding 20 deciliters, minus 10 coins")
                    water += 20
                    coins -= 10
                elif "potato" in buy_commands:
                    print("Adding 400 grams potatoes, minus 5 coins")
                    potato += 400
                    coins -= 5
                elif "carrot" in buy_commands:
                    print("Adding 6 carrots, minus 7 coins")
                    carrot += 6
                    coins -= 7
                if meat_achivement:
                    if "meat" in buy_commands:
                        print("Adding 4 meat packages, minus 5 coins")
                        meat_packages += 4
                        coins -= 5
                elif "lasagna" in buy_commands:
                    print("Adding 1 lasagna, minus 150 coins(JESUS!)")
                    lasagna += 1
                    coins -= 150
                if bread_achivement:
                    if "flour" in buy_commands:
                        print("Adding 200 grams flour, minus 8 coins")
                        flour += 200
                        coins -= 8
                    elif "oil" in buy_commands:
                        print("Adding 12 deciliters, minus 12 coins")
                        oil += 12
                        coins -= 12

    if "boosts" in command:
        clearConsole()
        print("\n\nBoosts!")
        print(" Currently under construction! Come back later!")
        """
        print("\n List of Boosts commands:")
        print("                          List")
        print("                          Buy")
        print("                          Exit")
        boosts_commands = input()
        
        if "list" in boosts_commands:
            print("Under Development")
        
        if coins != 0:
            elif "buy" in boosts_commands:
                print("Under Development")
        
        elif "exit" in boosts_commands:
            print("Exiting...")
            continue
        
            
        else
        """
    elif "info" in command:
        clearConsole()
        info()



    elif "update" in command or "log" in command:
        clearConsole()
        update()


    elif "exit" in command:
        exit()


    else:
        continue
