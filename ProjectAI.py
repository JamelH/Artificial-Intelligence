import sys
import os

#starter

#create your player
class health:
    def __init__(self, name):
        self.health = 100
        self.name = name
    def minus_health(self):
        self.health = self.health - 2
        if self.health <= 0:
            quit("You've lost!")


#Global names
global character
character = health("")


a = {"Look":1, "Buy Food":2, "Buy Armor": 3}
b = {"Look":2, "Armor":3}
c = {"Sleep":3}
d = {"Fight":4, "Do other stuff":5}
e = {"Look":5}
f = {"Look":6}
g = {"Look":7}
h = {"Look":8}
i = {"Look":9}



gridSystem = {"Store":a,
			"House":b, 
			"C":c, 
			"Cave":d, 
			"Five":e, 
			"Six": f, 
			"Seven":g, 
			"Eight":h, 
			"Nine":i}



#Exit out of game
def exitGame():
    return sys.exit("Exit")


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
                if answer == "Yes":
                    print("This store does this and that")
                    break
                elif answer == "No":
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
                if answer == "Yes":
                    print("This C does this and that")
                    break
                elif answer == "No":
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
                if answer == "Yes":
                    print("In this cave, you will fight this dude and stuff")
                    break
                elif answer == "No":
                    print("Ok")
                    break
                else:
                    print("Please enter Yes or No")



#print rooms in gridsystem
def room_Gridsystem():
    for keys in gridSystem.keys():
        print keys,


#view list of actions in a room
def view_Actions():
    pass


#Play the game
def action():
    list = []
    character.name = raw_input("Create the name of your character ")
    while True:
        answer = raw_input("Hello " + character.name + ". Would you like to check your health before proceeding? " )
        if answer == "Yes" or answer == "yes":
            print character.health
        elif answer == "No" or answer == "no":
            print "Proceed"
        #else:
            #print "Please enter Yes or No"
        room_Gridsystem()
        print
        room = raw_input("Please select one of the rooms from the list above: ")
        if room in gridSystem.keys():
            if room == "Store":
                store()
                action = raw_input("What do you want to do? ")
                if action in gridSystem[room]:
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
                action = raw_input("What do you want to do? ")
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
                action = raw_input("What do you want to do? ")
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
                action = raw_input("What do you want to do? ")
                if action in gridSystem[room]:
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
                            elif quitGame == "No":
                                    print("Restart")
                                    break

                            else:
                                 print "Type Yes or No"
                                 x = 1
        else:
            raw_input("Not in the gridsystem. Press enter to try again")



action()