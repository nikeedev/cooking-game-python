print("Loading all needed things, please show patient :)")
import random#temporally
print("...")
import time
def print_pause():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
water_enough = False
potato_enough = False
carrot_enough = False
meat_enough = False
coins = 0
water = 120 #desiliters
potato = 1000 #grams
carrot = 12 #12 carrots
meat_packages = 0 # going to be 20 meat packages
meat_achivement = False
soup = 0
soup_with_meat = 0
time.sleep(2)
print("Hello and welcome to Cooking Game! v.0.4.1: Small Meat update(More coming soon!)!")
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
    if water < 0:
        water = 0
    if potato < 0:
        potato = 0
    if carrot < 0:
        carrot = 0
    if coins < 0:
        coins = 0
    if meat_packages < 0:
        meat_packages = 0
    if meat_achivement == False:
       if soup == 2:
            meat_achivement = True
            print("You got Meat achievement, which means you can have meat in inventory, and you're able to make new Soup type!")
            meat_packages += 20
    print("List of Coammands:      ")
    print("                   Recipes")
    print("                   Inventory")
    print("                   Make something")
    print("                   Market(Sell and Buy food)")
    command = input("                   ")
    if "recipe" in command:
        print_pause()
        print("                   Current Recipes:")
        print("                   ")
        print("                   Soup:")
        print("                         Water: 10 Desiliters")
        print("                         Potato: 200 grams")
        print("                         Carrots: 3")
        print("                         ")
        print("                   Soup With Meatballs:")
        print("                         Water: 12 Desiliters")
        print("                         Potato: 200 grams")
        print("                         Carrots: 3")
        print("                         Meat Packages: 2")
    if "inventory" in command:
        print_pause()
        print("                   You have ", water, " desiliters of water")
        print("                   You have ", potato, " grams of potato")
        print("                   You have ", carrot, " carrots")
        print("                   You have ", soup, "soup")
        print("                   You have ", soup_with_meat, "soup with meatballs")
        print("                   You have ", coins, "coins")
        if meat_achivement == True:
            print("                   You have ", meat_packages, "meat packages")
        print("                   Tip: If you have small amount of required amount of ingredients, you won't be able to make food!")
    if "make something" in command:
        print_pause()
        print("                   Write name of any food above:")
        print("                   Soup")
        print("                   Soup With Meatballs")
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
            else:
                print("You can't make soup, because you dont have enough ingredients!")
                print("You have " + water + ", instead of 10 desiliters!")
                print("You have " + potato + ", instead of 200 grams!")
                print("You have " + carrot + ", instead of 3 carrots!")
            water_enough = False
            potato_enough = False
            carrot_enough = False
        
        elif make_something == "soup with meat":
            print("In order to make Soup with Meatballs, you need self write in amounts of ingrendients. If you don't remember you must check recipes!")
            soup_water = int(input("Write desiliters of water you want to add: "))
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
            if water_enough == True and potato_enough == True and carrot_enough == True and meat_enough == True:
                print("Yeah! All ingredients is here! You succesfully made some Soup!")
                print("- You got 1 Soup with Meatballs! It lies in inventory now -")
                soup_with_meat += 1
            else:
                print("You can't make soup, because you dont have enough ingredients!")
                print("You have now " + water + " dl of water, instead of 12 desiliters!")
                print("You have now " + potato + " grams of potatoes, instead of 200 grams!")
                print("You have now " + carrot + " sticks of carrots, instead of 3 carrots!")
                print("You have now " + meat_packages + " meat packages, instead of 2 packages")
            water_enough = False
            potato_enough = False
            carrot_enough = False
            meat_enough = False
    if "market" in command:
        print_pause()
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
            if soup < 0:
                print("You dont have anything to sell, redirecting back in 3 sec")
                time.sleep(3)
                continue
            elif soup > 0:
                print("You can sell only food you made.")
                time.sleep(2)
                print("Prices on foods change after time(update), so be in right time to get much coins!")
                time.sleep(3)
                print("You can sell ", soup, " soup.")
                time.sleep(2)
                print("If you want to sell write: name of food you want to sell.")
                sell_command = input()
                if "soup" in sell_command:
                    print("One soup costs: 25 coins")
                    print("Want to sell 1 one soup for current price? If not, you will be redirected back to main commands!")
                    sell_soup_answer = input("Write yes or no...")
                    if "yes" in sell_soup_answer:
                        print("Selling soup!")
                        time.sleep(2)
                        print("You got 25 coins")
                        coins += 25
        if "buy" in market_commands:
            if coins == 0:
                print("You dont have enough money! Leaving Market in 2 sec.")
                time.sleep(2)
                continue
            else:
                print("You can buy vegetables, water and other!")
                time.sleep(2)
                print("Here is what you can buy:")
                print("Water, 20 desiliters: 10 coins")
                print("Potato, 400 grams: 5 coins")
                print("Carrots, 6: 7 coins")
                time.sleep(3)
                print("Write in commands below what you want to buy:")
                print("Water")
                print("Potato")
                print("Carrot")
                buy_commands = input()
                if "water" in buy_commands:
                    print("Adding 20 desiliters, minus 10 coins")
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



    else:
        continue 



#Now on Github!