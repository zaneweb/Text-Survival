from sys import exit

from time import sleep


"""define variables"""
has_wood_pick = False
Name = input("Enter your name: ")
print ("Hello, " + Name)

class Player:
    """The Player. Packaged with the game."""
    def __init__(self):
        self.name = Name
        self.health = 20
        self.armor = ["no helmet", "no chestplate", "no leggings", "no boots"]
        self.inv = ["none", "none", "none", "none", "none", "none", "none", "none", "none"]
        self.input = "nil"
    def game(self, playerName):
        print ("Armor: ",self.armor)
        print ("Inventory: ",self.inv)
        print ("Health: ",self.health)
        print ("\nYou awake in a strange place you have never seen before. \n What do you do?")
        self.inputOP()
    def inputOP(self):
        self.input = input(">Enter Action>")
        if (self.input == "punch wood"):
            print (self.name + " punches wood.")
            self.get("wood")
            print (self.inv)
            self.inputOP()
        elif (self.input == "make planks"):
            self.testForItem("wood", "wood_planks")
        elif (self.input == "make sticks"):
            self.testForItem("wood_planks", "sticks")
        elif (self.input == "make wood pick"):
            self.tools("wood_planks", "sticks", "wooden_pick")
            self.has_wood_pick = True
        elif (self.input == "quit"):
            print ("goodbye")
            exit()
        elif (self.input == "pause"):
            Pause = input("Press enter to resume")
            self.inputOP()
        else:
            print ("Command not found. Please try again.")
            self.inputOP()
    def testForItem(self, item, result):
        if (self.inv[0] == item):
            if (self.inv[0] == "none"):
                    print ("made " + result)
                    self.inv[0] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[1] == "none"):
                    print ("made " + result)
                    self.inv[1] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[2] == "none"):
                    print ("made " + result)
                    self.inv[2] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[3] == "none"):
                    print ("made " + result)
                    self.inv[3] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[4] == "none"):
                    print ("made " + result)
                    self.inv[4] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[5] == "none"):
                    print ("made " + result)
                    self.inv[5] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[6] == "none"):
                    print ("made " + result)
                    self.inv[6] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[7] == "none"):
                    print ("made " + result)
                    self.inv[7] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[8] == "none"):
                    print ("made " + result)
                    self.inv[8] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
        elif (self.inv[1] == item):
            if (self.inv[0] == "none"):
                    print ("made " + result)
                    self.inv[0] = result
                    self.inv[1] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[1] == "none"):
                    print ("made " + result)
                    self.inv[1] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[2] == "none"):
                    print ("made " + result)
                    self.inv[2] = result
                    self.inv[1] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[3] == "none"):
                    print ("made " + result)
                    self.inv[3] = result
                    self.inv[1] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[4] == "none"):
                    print ("made " + result)
                    self.inv[4] = result
                    self.inv[1] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[5] == "none"):
                    print ("made " + result)
                    self.inv[5] = result
                    self.inv[1] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[6] == "none"):
                    print ("made " + result)
                    self.inv[6] = result
                    self.inv[1] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[7] == "none"):
                    print ("made " + result)
                    self.inv[7] = result
                    self.inv[1] = "none"
                    print (self.inv)
                    self.inputOP()
            elif (self.inv[8] == "none"):
                    print ("made " + result)
                    self.inv[8] = result
                    self.inv[1] = "none"
                    print (self.inv)
            self.inputOP()
            print ("made " + result)
        elif (self.inv[2] == item):
            print ("made " + result)
        elif (self.inv[3] == item):
           print ("made " + result)
        elif (self.inv[4] == item):
            print ("made " + result)
        elif (self.inv[5] == item):
            print ("made " + result)
        elif (self.inv[6] == item):
            print ("made " + result)
        elif (self.inv[7] == item):
            print ("made " + result)
        elif (self.inv[8] == item):
            print ("made " + result)
        else:
            print ("you don't have " + item)
            self.inputOP()

    def get(self, result):
        if (self.inv[0] == "none"):
            self.inv[0] = result
            print (self.inv)
            self.inputOP()
        elif (self.inv[1] == "none"):
            print ("made " + result)
            self.inv[1] = result
            print (self.inv)
            self.inputOP()
        elif (self.inv[2] == "none"):
            print ("made " + result)
            self.inv[2] = result
            print (self.inv)
            self.inputOP()
        elif (self.inv[3] == "none"):
            print ("made " + result)
            self.inv[3] = result
            print (self.inv)
            self.inputOP()
        elif (self.inv[4] == "none"):
            print ("made " + result)
            self.inv[4] = result
            print (self.inv)
            self.inputOP()
        elif (self.inv[5] == "none"):
            print ("made " + result)
            self.inv[5] = result
            self.inv[0] = "none"
            print (self.inv)
            self.inputOP()
        elif (self.inv[6] == "none"):
            print ("made " + result)
            self.inv[6] = result
            self.inv[0] = "none"
            print (self.inv)
            self.inputOP()
        elif (self.inv[7] == "none"):
            print ("made " + result)
            self.inv[7] = result
            self.inv[0] = "none"
            print (self.inv)
            self.inputOP()
        elif (self.inv[8] == "none"):
                    print ("made " + result)
                    self.inv[8] = result
                    self.inv[0] = "none"
                    print (self.inv)
                    self.inputOP()
        else:
            print ("you don't have " + item)
            self.inputOP()
    def tools (self, item1, item2, result):
        if (self.inv[0] == item1 and self.inv[1] == item2):
            if (self.inv[2] == "none"):
                self.inv[2] = result
                self.inv[0] = "none"
                self.inv[1] = "none"
                print ("made " + result)
                print (self.inv)
            self.inputOP()
        elif (self.inv[3] == "none"):
            self.inv[3] = result
            self.inv[0] = "none"
            self.inv[1] = "none"
            print ("made " + result)
            print (self.inv)
            self.inputOP()
        elif (self.inv[4] == "none"):
            self.inv[4] = result
            self.inv[0] = "none"
            self.inv[1] = "none"
            print ("made " + result)
            print (self.inv)
            self.inputOP()
        elif (self.inv[5] == "none"):
            self.inv[5] = result
            self.inv[0] = "none"
            self.inv[1] = "none"
            print ("made " + result)
            print (self.inv)
            self.inputOP()
        elif (self.inv[6] == "none"):
            self.inv[6] = result
            self.inv[0] = "none"
            self.inv[1] = "none"
            print ("made " + result)
            print (self.inv)
            self.inputOP()
        elif (self.inv[7] == "none"):
            self.inv[7] = result
            self.inv[0] = "none"
            self.inv[1] = "none"
            print ("made " + result)
            print (self.inv)
            self.inputOP()
        elif (self.inv[8] == "none"):
            self.inv[8] = result
            self.inv[0] = "none"
            self.inv[1] = "none"
            print ("made " + result)
            print (self.inv)
            self.inputOP()
        elif (self.inv[1] == item1 and self.inv[0] == item2):
            if (self.inv[2] == "none"):
                self.inv[2] = result
                self.inv[0] = "none"
                self.inv[1] = "none"
                print ("made " + result)
                print (self.inv)
                self.inputOP()
            elif (self.inv[3] == "none"):
                self.inv[3] = result
                self.inv[0] = "none"
                self.inv[1] = "none"
                print ("made " + result)
                print (self.inv)
                self.inputOP()
            elif (self.inv[4] == "none"):
                self.inv[4] = result
                self.inv[0] = "none"
                self.inv[1] = "none"
                print ("made " + result)
                print (self.inv)
                self.inputOP()
            elif (self.inv[5] == "none"):
                self.inv[5] = result
                self.inv[0] = "none"
                self.inv[1] = "none"
                print ("made " + result)
                print (self.inv)
                self.inputOP()
            elif (self.inv[6] == "none"):
                self.inv[6] = result
                self.inv[0] = "none"
                self.inv[1] = "none"
                print ("made " + result)
                print (self.inv)
                self.inputOP()
            elif (self.inv[7] == "none"):
                self.inv[7] = result
                self.inv[0] = "none"
                self.inv[1] = "none"
                print ("made " + result)
                print (self.inv)
                self.inputOP()
            elif (self.inv[8] == "none"):
                self.inv[8] = result
                self.inv[0] = "none"
                self.inv[1] = "none"
                print ("made " + result)
                print (self.inv)
                self.inputOP()






player = Player()
player.game(player.name)

