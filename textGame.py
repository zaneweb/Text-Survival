from sys import exit

from time import sleep

Name = raw_input("Enter your name: ")
print "Hello, " + Name

class Player:
    """The Player. Packaged with the game."""
    def __init__(self):
        self.name = Name
        self.health = 20
        self.armor = ["none", "none", "none", "none"]
        self.inv = ["none", "none", "none", "none", "none", "none", "none", "none", "none"]
        self.input = "nil"
    def game(self, playerName):
        print "You awake in a strange place you have never seen before. \n What do you do?"
        self.inputOP()
    def inputOP(self):
        self.input = raw_input(">Enter Action>")
        if (self.input == "punch wood"):
                print self.name + " punches wood."
                self.inv[0] = "wood"
                print self.inv
                self.inputOP()
        elif (self.input == "make planks"):
                self.testForItem("wood", "wood_planks")
        elif (self.input == "quit"):
                print "goodbye"
                exit()
        else:
                self.inputOP()
    def testForItem(self, item, result):
        if (self.inv[0] == item):
                if (self.inv[0] == "none"):
                        print "made " + result
                        self.inv[0] = result
                        self.inv[0] = "none"
                        print self.inv
                elif (self.inv[1] == "none"):
                        print "made " + result
                        self.inv[1] = result
                        self.inv[0] = "none"
                        print self.inv
                elif (self.inv[2] == "none"):
                        print "made " + result
                        self.inv[2] = result
                        self.inv[0] = "none"
                        print self.inv
                elif (self.inv[3] == "none"):
                        print "made " + result
                        self.inv[3] = result
                        self.inv[0] = "none"
                        print self.inv
                elif (self.inv[4] == "none"):
                        print "made " + result
                        self.inv[4] = result
                        self.inv[0] = "none"
                        print self.inv
                elif (self.inv[5] == "none"):
                        print "made " + result
                        self.inv[5] = result
                        self.inv[0] = "none"
                        print self.inv
                elif (self.inv[6] == "none"):
                        print "made " + result
                        self.inv[6] = result
                        self.inv[0] = "none"
                        print self.inv
                elif (self.inv[7] == "none"):
                        print "made " + result
                        self.inv[7] = result
                        self.inv[0] = "none"
                        print self.inv
                elif (self.inv[8] == "none"):
                        print "made " + result
                        self.inv[8] = result
                        self.inv[0] = "none"
                        print self.inv
        elif (self.inv[1] == item):
                print "made " + result
        elif (self.inv[2] == item):
                print "made " + result
        elif (self.inv[3] == item):
                print "made " + result
        elif (self.inv[4] == item):
                print "made " + result
        elif (self.inv[5] == item):
                print "made " + result
        elif (self.inv[6] == item):
                print "made " + result
        elif (self.inv[7] == item):
                print "made " + result
        elif (self.inv[8] == item):
                print "made " + result
        else:
            self.inputOP()

player = Player()
player.game(player.name)
