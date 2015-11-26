
"""
Jamel Hamani
Patrick Burden
"""

import sys
import os
import time
from random import randint
import random
import string


#create function to go to a room




#create your player
class Character:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.inventory = []
        self.gold = 0
        self.job = ""


    def minus_health(self):
        self.health = self.health - 2
        if self.health <= 0:
            quit("You've lost!")
    def lookAtInventory(self):
        return self.inventory




#Enemy
class Enemy():
  def __init__(self):
    self.name = 'Burglar'
    self.health = 0
    self.inventory = []

class merchant(Enemy):
    def __init__(self):
        self.name = 'some monster'
        self.health = 100
        self.inventory = ["sword", "shield", "clothing"]

class guard(Enemy):
    def __init__(self):
        self.name = 'some monster'
        self.health = 200
        self.inventory = ["sword", "shield", "knife"]


enemy = Enemy()


#Global names
global character
character = Character("")



Items = {"shield":1, "sword":2, "medicine":3, "clothing":4, "staff":5, "knife":6}


a = {"look":1, "buy food":Items, "buy armor": 3, "show inventory":4}
b = {"look":2, "armor":3, "inventory":4}
c = {"sleep":3}
d = {"fight":4, "explore the cave":5, "look":6, "hunt for treasure":7, "lit fire":8}
e = {"look":5}
f = {"look":6}
g = {"look":7}
h = {"look":8}
i = {"look":9000}



gridSystem = {"store":a,
            "house":b,
            "c":c,
            "cave":d,
            "gate":e,
            "six": f,
            "seven":g,
            "eight":h,
            "nine":i}

def help():
  print "THIS AND THAT AND DO THIS AND THAT MENU SOMETHING"

#print rooms in gridsystem
def room_Gridsystem():
    rooms = ["House", "C", "Eight", "Gate", "Store", "Cave", "Nine", "Gate", "Six"]
    print  rooms



#view list of actions in a room
def view_Actions(dictionary):
    return list(gridSystem.get(dictionary))


def view_ActionsinActions(dictionary, dictionary2):
    return list(gridSystem.get(dictionary).get(dictionary2))




#exit game with timer
def exitGame():
    print 'That\'s a shame...'
    for i in range(5):
        time.sleep(1)
        print 'Exiting game in: ', i+1, ' seconds'
    sys.exit('Exiting Game')




#converts a list of actions to a string
def actiontoString(actions):
    action = []
    return ''.join(actions)



#creates a random action you might encounter in the House grid
def randomActionsHouse():
    digits = [ "burglar", "scripture", "treasure"]
    random_item = random.choice(digits)
    return random_item



#If user selects store
def store():
    for key in gridSystem.keys():
        if key  == "Store":
            while True:
                answer = raw_input("Welcome to our store. Would you like to read "
                                   "about the description? Type Yes or No ")
                if answer == "Yes" or answer == "yes":
                    print("This store does this and that")
                    break
                elif answer == "No" or answer == "no":
                    print("Ok")
                    break
                else:
                    print("Please enter Yes or No")



#If user selects house
def house():
    for key in gridSystem.keys():
        if key  == "House":
            while True:
                answer = raw_input("Welcome to your House. Would you like to read "
                                   "about the description? Type Yes or No ")
                if answer == "Yes":
                    print("This house does this and that")
                    break
                elif answer == "No":
                    print("Ok")
                    break
                else:
                    print("Please enter Yes or No")


#if user selects c-dictionary
def cdictionary():
    for key in gridSystem.keys():
        if key  == "House":
            while True:
                answer = raw_input("Welcome to your C. Would you like to read "
                                   "about the description? Type Yes or No ")
                if answer == "Yes" or answer == "yes":
                    print("This C does this and that")
                    break
                elif answer == "No" or answer == "no":
                    print("Ok")
                    break
                else:
                    print("Please enter Yes or No")



#if user selects c-dictionary
def cave():
    action = ""
    for key in gridSystem.keys():
        if key  == "Cave":
            while True:
                answer = raw_input("Welcome to the cave. Would you like to read "
                                   "about the description? Type Yes or No ")
                if answer == "Yes" or answer == "yes":
                    print("In this cave, you will fight this dude and stuff")
                    break
                elif answer == "No" or answer == "no":
                    print("Ok")
                    break
                else:
                    print("Please enter Yes or No")




#start game by choosing the name and class of your character
def chooseYourCharacter():
    character.name = raw_input("Create the name of your character ").strip()
    print
    areYouSure()
    print "Pick a Class"
    print
    while True:
        action = raw_input("Thief, Fighter, Mage ").strip().lower()
        print
        if action == "thief":
            character.job = action
            character.inventory.append("knife")
            break
        if action == "fighter":
            character.job = action
            character.gold += 50
            character.inventory.append("sword")
            break
        if action == "mage":
            character.job = action
            character.gold += 150
            character.inventory.append("staff")
            break
        else:
            print "Not an Option"

#would you like to see the list of items in your inventory?
def showInventory():
    while True:
        show_Inventory = raw_input("Would you like to view your inventory? ")
        print
        if show_Inventory == "yes":
            print "Your current inventory is: " + str(character.inventory) + ". You can continue adding  to your inventory" \
            + " as your adventure continues"
            print
            break
        elif show_Inventory == "no":
            print "Very well. "
            break
        else:
            print "Please type yes or no"

#ready to begin adventure?
def procceedtoAdventure():
    myList = ["Show Inventory", "Choose a character", "Procceed"]
    while True:
        procceed = raw_input("Would you like to proceed? ").strip()
        print
        if procceed == "yes":
            break
        elif procceed == "no":
            while True:
                goBack= raw_input("Where would you like to go back? ").strip()
                if goBack == "Show Inventory":
                    showInventory()
                    break
                elif "Choose a character" == goBack:
                    chooseYourCharacter()
                    break
                elif "Procceed" == goBack:
                    break
                else:
                    print "Not in the menu. Please select an action from this list: " + str(myList)
            break
        else:
            print "Please type yes or no"


    print "Your adventure begins now" +" "+  character.name + " the " + character.job
    print





#proceed?
def areYouSure():
      while True:
        sure = raw_input("Your name is " + character.name + "." +" Are you sure? ").strip()
        print
        if sure == "Yes" or sure == "yes":
            break
        elif sure == "No" or sure == "no":
            chooseYourCharacter()
            break
        else:
            print "Please enter yes or no"
            print



#quit game
def quit():
    x = 1
    print "Not an action"
    while x:
        quitGame = raw_input("Do you want to quit? y/n ").strip()
        print
        if quitGame == "Yes":
                exitGame()
                x = 2
                sys.exit("EXITED")
        elif quitGame == "No":
            print("Restart")
            restart()
            break

        else:
            print "Type Yes or No"
            x = 1

#timer
def timerRestart():
    for i in range(5):
        time.sleep(1)
        print "Restarting game in", i+1, 'seconds'
    return 'Restarted'

#restart to a specific part of the game  --NOT FINISHED
def restart():
    restart_game = raw_input("From where would you like to restart your game from? ").lower().strip()
    if restart_game == "choose your character":
        print timerRestart()
        chooseYourCharacter()



#create functions
#get rid of capital letters


#Play the game
def playGame():
    chooseYourCharacter()
    showInventory()
    procceedtoAdventure()
    print
    x = True
    while x:
        room_Gridsystem()
        room = raw_input("Please select one of the rooms from the list above: ").lower().strip()
        print
        if room in gridSystem.keys():
            #if room == "gate":

            if room == "store":
                store()
                while True:
                    print("Here is a list of actions you may select in " + room)
                    print
                    print view_Actions("store")
                    print
                    action = raw_input("Select an action from the list above ").lower().strip()
                    print
                    while True:
                        if "show inventory" == action:
                            print "Here is " +character.name + "'s. Inventory " + str(character.lookAtInventory()) \
                                  + " You have this much gold: " + str(character.gold )
                            print
                            break

                        if "buy food" == action:
                            print view_ActionsinActions("store", "buy food")
                            select = raw_input( "Select something from the list above to buy: ").strip()
                            print

                            if select == "sword":
                                 print "You have selected to buy a sword"
                            elif select == "medicine":
                                print "you have selected to buy medicine"
                                character.inventory.append("medicine")
                                character.lookAtInventory()


                            """
                            else:
                                print ("You have selected to " + actiontoString([action]))
                                print gridSystem[room][action]
                                break
                                """
                        else:
                            quit()


            elif room == "house":
                house()
                while True:
                    print("Here is a list of actions you may select in " + room)
                    print
                    print view_Actions("house")
                    print
                    action = raw_input("Select an action from the list above ").strip()
                    while True:
                        if action == "look":
                            print str(character.name) + " is looking around the " + str(room)
                            print
                            if randomActionsHouse() == "burglar":
                                print "A burglar has borken into your house!"
                                print
                                print "Take action?, Run Away?"
                                while True:
                                    take_action = raw_input("What are you going to do? ").strip()
                                    if take_action == "Run Away":
                                        print "You got away safely"
                                        break
                                    elif take_action == "Take action":
                                        print character.name + " attatcked " + str(enemy.name) + "." + str(enemy.name) \
                                              + " s health is now " + str(enemy.health)
                                        break
                                    else:
                                        print "Please select to Take action or to Run Away"
                            elif randomActionsHouse() == "treasure":
                                print "Weird. There is a treasure box on the floor"
                                print
                                print str(character.name) + " opens the treasure box"
                                print character.gold
                                character.gold += randint(0,1000)
                                print character.gold
                                if character.gold > 0:
                                    print "Wow you currently have " + str(character.gold) + \
                                    " coins!"
                                else:
                                    print "0? POINTLESS! "
                                break
                            elif randomActionsHouse() == "scripture":
                                print "There is a weird scripture drawn on the wall of your house"
                                print
                                print "The scripture reads: You must enter the cave to meat the omega"
                                print
                                break
                            else:
                                print("Looks like nothing caught the attention of ") + str(character.name)

                            break

                        elif action == "inventory":
                            check_inventory = raw_input("Would you like to check your current inventory? ")
                            if check_inventory == "yes":
                                print "Here is the list of your current inventory: " + str(character.inventory)
                                break
                            elif check_inventory == "no":
                                print "Very well"
                                break
                            else:
                                print "Please type yes or no"

                        else:
                            quit()
            elif room == "C":
                cdictionary()
                print("Here is a list of actions you may select in " + room)
                print view_Actions("C")
                action = raw_input("Select an action from the list above ").strip()
                print
                if action in gridSystem[room]:
                    print ("You have selected to " + actiontoString([action]))
                    print gridSystem[room][action]
                    break

                else:
                    quit()
            elif room == "cave":
                cave()
                print "You enter the dark cave out of curioisty"
                print
                while True:
                    print("Here is a list of actions you may select in " + room)
                    print
                    print view_Actions("cave")
                    print
                    action = raw_input("Select an action from the list above ").strip()
                    if action in gridSystem[room]:
                        if "fight" == action:
                            print "There is no one to fight.....yet"
                            break

                        elif "look" == action:
                            print str(character.name) + " is looking around the cave. It is dark and " \
                                                        "you can only make out a small stick on the floor."
                            print
                            while True:
                                pickStick = raw_input("Pick up the stick and add to inventory? Might be useful to "
                                                      "light up a fire! ").lower().strip()
                                if pickStick == "yes":
                                    character.inventory.append("stick")
                                    print str(character.name) + " added a stick to his inventory"
                                    print
                                    print str(character.name) + "'s current inventory " + str(character.lookAtInventory())
                                    break
                                elif pickStick == "no":
                                    print str(character.name) + " did not pick up the stick"
                                    break
                                else:
                                    print "Type yes or no"



                        elif "lit fire" == action:
                            if not "stick" in character.inventory:
                                print "You cant lit up a fire without a stick. Try finding a stick around the cave" \
                                      ". There must be one!!"

                            else:
                                print str(character.name) + " is feeling warm in this dark, cold cave"
                                character.health += 100
                                print
                                print str(character.name) + " health is now " + str(character.health)

                        elif "explore the cave" == action:
                            while True:
                                print "There seems to be someone near the lake"
                                print
                                walkTowards = raw_input("Walk towards the figure? ")
                                if walkTowards == "yes":
                                    print
                                    print str(character.name) + " is walking towards the dark figure"
                                    print
                                    print "Its an enemy!"
                                    #create list of attatcs here
                                elif walkTowards == "no":
                                    print
                                    print str(character.name) + " decides its not worth the risk and walks away"
                                    break






                    else:
                        quit()



                else:
                   quit()
        else:
            raw_input("Not in the gridsystem. Press enter to try again").strip()
            print

playGame()