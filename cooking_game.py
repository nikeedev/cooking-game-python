print("Loading all needed things, please show patient :)")
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
lasagna = 0
baked_lasagna = 0
potato = 1000 #grams
carrot = 12 #12 carrots
meat_packages = 0 # going to be 20 meat packages
meat_achivement = False
soup = 0
soup_with_meat = 0
time.sleep(2)
print("Hello and welcome to Cooking Game! v.0.6: Lasagna is here! (more info in info command)")
input("press Enter to continue...")
print("What is your name or in this case nickname?")
username = input("My nickname is... ")
print("Hello " + username + ". Nice, now can we begin to cook!")
print("Okay, We're ready!")
input("press Enter to continue...")
print("Lets begin with making some soup!")
input("press Enter to continue...")
print("In this game you have values of ingredients, meaning that you can't make very much food.")
input("press Enter to continue...")
print("But we should have it enough to make some Soup!")
input("press Enter to continue...")

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
           print("")
           print("")
           print("")
           meat_achivement = True
           print("You got Meat achievement, which means you can have meat in inventory, and you're able to make new Soup type!")
           meat_packages += 20
           print("")
           print("")
           print("")
    print("")
    print("Good Joke: What is called Caveman's fart? Blast from past!")
    print("Hello, " + username + " ! What do you want to do now?")
    print("List of Coammands:      ")
    print("                   Recipes")
    print("                   Inventory")
    print("                   Make something")
    print("                   Market(Sell and Buy food)")
    print("                   Info")
    print("                   Update Log")
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
        if meat_achivement == True:
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
        if meat_achivement == True:
            print("                   You have ", soup_with_meat, "soup with meatballs")
        print("                   You have ", coins, "coins")
        if meat_achivement == True:
            print("                   You have ", meat_packages, "meat packages")
        print("                   You have ", lasagna, "lasagna's")
        print("                   You have ", baked_lasagna, "baked lasagna's")
        print("                   Tip: If you have small amount of required amount of ingredients, you won't be able to make food!")
    if "make something" in command:
        print_pause()
        print("                   Write name of any food above:")
        print("                   Soup")
        if meat_achivement == True:
            print("                   Soup With Meatballs")
        elif lasagna >= 1:
            print("                   Lasagna")
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
        elif meat_achivement == True:
            if make_something == "soup with meat":
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
        elif lasagna >= 1:
            if "lasagna" in make_something:
                print("You are lucky to buy Lasagna! It costed you much...")
                input("press Enter to continue...")
                print("All you need is to say Yes or Y to make that lasagna...")
                lasagna_accept = input("Write yes/y or no/n: ")
                if "y" or "yes" in lasagna_accept:
                    print("Well you did it. But you lose whole 20 Desilliters of water... :|")
                    input("press Enter to continue...")
                    water -= 20
                    baked_lasagna += 1
                    print("- You made 1 Baked Lasagna -")
                if "n" or "no" in lasagna_accept:
                    print("Well you won't regret next time...")
                    input("Press That Enter button to Continue!!!!!!")


        else:
            continue
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
            if soup < 0 or soup_with_meat < 0:
                print("You dont have anything to sell, redirecting back in 3 sec")
                time.sleep(3)
                continue
            elif soup > 0 or soup_with_meat > 0:
                print("You can sell only food you made.")
                time.sleep(2)
                print("Prices on foods change after time(after updates), so be in right time to get much coins!")
                time.sleep(3)
                print("You can sell ", soup, " soup.")
                print("You can sell ", soup_with_meat, " soup with meatballs.")
                time.sleep(2)
                print("If you want to sell write: name of food you want to sell.")
                sell_command = input()
                if "soup" in sell_command:
                    print("One soup costs: 25 coins")
                    print("Want to sell 1 soup for current price? If not, you will be redirected back to main commands!")
                    sell_soup_answer = input("Write yes or no...")
                    if "yes" in sell_soup_answer:
                        print("Selling soup!")
                        soup -= 1
                        time.sleep(2)
                        print("You got 25 coins")
                        coins += 25
                elif "soup with meatballs" in sell_command:
                    print("One soup with meatballs costs: 30 coins")
                    print("Want to sell 1 soup with meatballs for current price?")
                    print("If not, you will be redirected back to main commands!")
                    sell_soup_answer = input("Write yes or no...")
                    if "yes" in sell_soup_answer:
                        print("Selling soup!")
                        soup_with_meat -= 1
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
                print("Water, 20 desiliters: 10 coins")
                print("Potato, 400 grams: 5 coins")
                print("Carrots, 6 sticks: 7 coins")
                if meat_achivement == True:
                    print("Meat, 4 packages: 5 coins")
                print("Lasagna, 1: 50 coins(being rich to buy this recommended)")
                time.sleep(3)
                print("Write in commands below what you want to buy:")
                print("Water")
                print("Potato")
                print("Carrot")
                print("Lasagna")
                if meat_achivement == True:
                    print("Meat")
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
                if meat_achivement == True:    
                    if "meat" in buy_commands:
                        print("Adding 4 meat packages, minus 5 coins")
                        meat_packages += 4
                        coins -= 5
                elif "lasagna" in buy_commands:
                    print("Adding 1 lasagna, minus 50 coins(JESUS!)")
                    lasagna += 1
                    coins -= 50

    elif "info" in command:
        print_pause()
        print("Cooking Game®")
        print("Made by Nikegamerjjjj(Nikita)")
        print("Copyright ©2021")
        print("This game is made completly by hand, and no turtorials have been used.")
        print("Game code can be changed, but without asking owner(nikegamerjjjj),")
        print("you are not following rules and may cause in problems.")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Contact me here:")
        print("Discord(Spamming me causes to block you from support): nikegamerjjjj#8874")
        print("Github: Nikegamerjjjj(Use issue report function in repo)")
        print("")



    elif "update" in command or "log" in command:
        print_pause()
        print("Update: Lasanga! ")
        print("")
        print("Version: v.0.6")
        print("")
        print("New:")
        print("")
        print("Added Lasagna!")
        print("You will find it as your worst nightmare, when you buy!")
        print("")
        print("")
        print("")


    else:
        continue 



#What is called Caveman's fart? Blast from past!
