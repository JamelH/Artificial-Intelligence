
import sys
import os
import time
from random import randint





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
    self.name = 'some monster'
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





#Global names
global character
character = Character("")



Items = {"shield":1, "sword":2, "medicine":3, "clothing":4, "staff":5, "knife":6}


a = {"look":1, "buy food":Items, "buy armor": 3, "inventory":4}
b = {"look":2, "armor":3, "inventory":4}
c = {"sleep":3}
d = {"fight":4, "Do other stuff":5}
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

def helper():
  print "THIS AND THAT AND DO THIS AND THAT MENU SOMETHING"

#print rooms in gridsystem
def room_Gridsystem():
    for keys in gridSystem.keys():
        print keys,


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

#restart
def restart():
    for i in range(0):
        time.sleep(1)
    print 'Restarting'




#converts a list of actions to a string
def actiontoString(actions):
    action = []
    return ''.join(actions)





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


print view_ActionsinActions("store", "buy food")


def chooseYourCharacter():
    character.name = raw_input("Create the name of your character ")
    areYouSure()
    print "Pick a Class"
    print "Thief, Fighter, Mage"
    while True:
        action = raw_input("Choose an option from above ")
        if action == "Thief":
            character.job = action
            character.inventory.append("knife")
            break
        if action == "Fighter":
            character.job = action
            character.gold += 50
            character.inventory.append("sword")
            break
        if action == "Mage":
            character.job = action
            character.gold += 150
            character.inventory.append("staff")
            break
        else:
            print "Not an Option"
    print "Your adventure begins now" +" "+  character.name + " the " + character.job



print character.health
print character.gold


def areYouSure():
      while True:
        sure = raw_input("Are you sure ?")
        if sure == "Yes" or sure == "yes":
            break
        elif sure == "No" or sure == "no":
            chooseYourCharacter()
            break
        else:
            print "Please enter yes or no"




#Play the game
def playGame():
    chooseYourCharacter()
    x = True
    while x:
        room_Gridsystem()
        print
        room = raw_input("Please select one of the rooms from the list above: ").lower()
        if room in gridSystem.keys():
            #if room == "gate":

            if room == "store":
                store()
                while True:
                    print("Here is a list of actions you may select in " + room)
                    print view_Actions("store")
                    action = raw_input("Select an action from the list above ").lower()
                    while True:
                        if "inventory" == action:
                            print "Here is " +character.name + "'s Inventory " + str(character.lookAtInventory()) \
                                  + " You have this much gold: " + str(character.gold )
                            break

                        if "buy food" == action:
                            print view_ActionsinActions("store", "buy food")
                            select = raw_input( "Select something from the list above to buy: ")

                            if select == "sword":
                                 print "You have selected to buy a sword"
                            elif select == "medicine":
                                print "you have selected to buy medicine"
                                character.inventory.append("medicine")
                                character.lookAtInventory()



                            else:
                                print ("You have selected to " + actiontoString([action]))
                                print gridSystem[room][action]
                                break

                    else:
                        print "Not an action"
                        quitGame = raw_input("Do you want to quit? y/n ")
                        if quitGame == "Yes" or quitGame == "yes":
                                exitGame()
                        elif quitGame == "No" or quitGame == "no":
                                print("Restart")
                        else:
                            print "Type Yes or No"
            elif room == "House":
                house()
                print("Here is a list of actions you may select in " + room)
                print view_Actions("House")
                action = raw_input("Select an action from the list above ")
                if action in gridSystem[room]:
                    print ("You have selected to " + actiontoString([action]))
                    print gridSystem[room][action]
                    break
                else:
                    print "Not an action"
                    quitGame = raw_input("Do you want to quit? y/n ")
                    if quitGame == "Yes":
                            exitGame()
                    elif quitGame == "No":
                            print("Restart")
                    else:
                        print "Type Yes or No"
            elif room == "C":
                cdictionary()
                print("Here is a list of actions you may select in " + room)
                print view_Actions("C")
                action = raw_input("Select an action from the list above ")
                if action in gridSystem[room]:
                    print ("You have selected to " + actiontoString([action]))
                    print gridSystem[room][action]
                    break

                else:
                    print "Not an action"
                    quitGame = raw_input("Do you want to quit? y/n ")
                    if quitGame == "Yes":
                            exitGame()
                    elif quitGame == "No":
                            print("Restart")
                    else:
                        print "Type Yes or No"

            elif room == "Cave":
                cave()
                print("Here is a list of actions you may select in " + room)
                print view_Actions("Cave")
                action = raw_input("Select an action from the list above ")
                if action in gridSystem[room]:
                    if "Fight" in view_Actions("Cave"):
                        print "There is no one to fight.....yet"
                    else:
                        print ("You have selected to " + actiontoString([action]))
                        print gridSystem[room][action]
                        break


                else:
                    x = 1
                    print "Not an action"
                    while x:
                            quitGame = raw_input("Do you want to quit? y/n ")
                            if quitGame == "Yes":
                                exitGame()
                                x = 2
                                sys.exit("EXITED")
                            elif quitGame == "No":

                                    print("Restart")
                                    break

                            else:
                                 print "Type Yes or No"
                                 x = 1
        else:
            raw_input("Not in the gridsystem. Press enter to try again")


