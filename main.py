from random import randint, choice
from os import system
import os
from time import sleep
import platform
import json

inDungeon = False


def wait(dur):
    sleep(dur)


def clearConsole():
    if platform.system() == 'win32':
        system('cls')
    else:
        system('clear')


def loading(msg, dur):
    for j in range(0, dur * 3):
        clearConsole()
        print(f"{msg}.")
        wait(1 / 3)
        clearConsole()
        print(f"{msg}..")
        wait(1 / 3)
        clearConsole()
        print(f"{msg}...")
        wait(1 / 3)
        clearConsole()


class PlayerStats:
    def __init__(self):
        self.stats = {
            'combat': 0,
            'defense': 0,
            'xplevel': 0
        }

    def getAttrib(self, attrib):
        try:
            return self.stats[attrib]
        except KeyError:
            pass

    def changeAttrib(self, attrib, num):
        if attrib in self.stats:
            self.stats[attrib] = num

    def changeDict(self, dictionary):
        self.stats = dictionary


class Inventory:
    def __init__(self):
        self.inv = {
            'healpot': 0,
            'strengthpot': 0,
            'dungeon_key': 0,
            'story_coins': 0
        }

    def getValue(self, food):
        try:
            return self.inv[food]
        except KeyError:
            pass

    def changeValue(self, item, num):
        if item in self.inv:
            self.inv[item] += num

    def menu(self):
        for item in self.inv.keys():
            text = item[0].upper() + item[1:]
            if item == 'mushroom stew':
                text = 'Mushroom Stew'
            print(f"[{text}]:[{self.getValue(item)}]")
            continue

    def changeDict(self, dictionary):
        self.inv = dictionary


inv = Inventory()


class Achievements:
    ach = {
        'enter_dungeon': False,
        'get_iron': False,
        'get_crystal': False,
        'get_dragonic': False
    }

    def __int__(self):
        pass

    def changeAch(self, attrib, tf):
        if tf is None:
            if self.ach[attrib]:
                self.ach[attrib] = False
            else:
                self.ach[attrib] = True
        else:
            self.ach[attrib] = tf

    def changeDict(self, dictionary):
        self.ach = dictionary

    def retDict(self):
        return self.ach


class Health:
    def __init__(self):
        self.health = 20

    def getHeath(self):
        return self.health

    def verify(self):
        if self.health > 20:
            self.health = 20
        elif self.health < 0:
            self.health = 0

    def changeHealth(self, val):
        self.health += val
        self.verify()


health = Health()


class Hunger:
    def __init__(self):
        self.hunger = 20

    def getHunger(self):
        return self.hunger

    def verify(self):
        if self.hunger > 20:
            self.hunger = 20
        elif self.hunger < 0:
            self.hunger = 0
        if self.hunger == 0:
            health.changeHealth(-4)
            print("You lost some health because your hunger is low. This can kill you.")

    def changeHunger(self, val):
        self.hunger += val
        self.verify()


class UI:
    def __init__(self):
        pass

    @staticmethod
    def divider():
        print('══✿══╡°˖✧✿✧˖°╞══✿══')

    @staticmethod
    def dividerReturn():
        return '══✿══╡°˖✧✿✧˖°╞══✿══'

    @staticmethod
    def midPrint(text):
        print(f'[{text}]')

    @staticmethod
    def midReturn(text):
        return f'[{text}]'


class Shop:
    def __init__(self):
        self.stock = {}
        self.prices = {}

    def menu(self):
        string = ''
        for item in self.stock.keys():
            for price in self.prices.keys():
                string = string + (
                    f'[{item[0].upper() + item[1:]}][Available:|{self.stock[item]}|Cost:|₪{self.prices[price]}|]\n\n')
                break
        return string

    def update(self, value):
        for item in self.stock.keys():
            self.stock[item] += value

    def newItem(self, itemname, avl, price):
        self.stock[itemname] = avl
        self.prices[itemname] = price

    def delItem(self, delname):
        del self.stock[delname]
        del self.prices[delname]

    @staticmethod
    def calcPrice(self, item, quan):
        try:
            return self.prices[item] * quan
        except KeyError:
            return False

    @staticmethod
    def checkOutPossible(price):
        if price > inv.getValue('money'):
            return False
        else:
            return True


# To be changed as per game

save_template = {
    "inventory": {
        "apple": 0,
        "mushroomstew": 0
    },
    "achievements": {
        "finish_tutorial": False,
        "find_traders": False,
        "get_iron_gear": False
    },
    "attributes": {
        "combat": 0,
        "defense": 0,
        "xplevel": 0
    }
}

# Object Creation

# Health is created as "health"

ui = UI()
hunger = Hunger()
shop = Shop()
achievements = Achievements()

print("Note: Caps DON'T Matter.")
wait(2)
clearConsole()

pathToFile = input("Please enter your system path to this folder. If it is already saved press enter: ")

if pathToFile != '':
    with open('path.txt', 'w') as f:
        f.write(pathToFile)

else:
    pass

running = True
setup = True

# So if you want to end the game do: running = False
while setup:
    clearConsole()
    ui.divider()
    print("SETUP: \nNew Save - N\nLoad Save - L\nDelete Save - D\n")
    command = input("[N/L/D]>>> ").lower()
    if command == 'n':
        clearConsole()
        name = input("[Save Name]>>> ")
        with open('path.txt', 'r') as f:
            ptf = f.read()
        with open(f'{ptf}/saves/{name}.json', 'w') as f:
            json.dump(save_template, f)
            setup = False
    elif command == 'd':
        clearConsole()
        name = input("[Save Name]>>> ")
        with open('path.txt', 'r') as f:
            ptf = f.read()
        try:
            conf = input("Confirmation[Y/N]>>> ").lower()
            if conf == 'y':
                os.remove(f"{ptf}/saves/{name}.json")
                print('Deleted File.')
                wait(1)
            else:
                print("Save not Deleted.")
                wait(1)
                continue
        except FileNotFoundError:
            print("That Save Doesn't Exist")
    elif command == 'l':
        clearConsole()
        name = input("[Save Name]>>> ")
        with open('path.txt', 'r') as f:
            ptf = f.read()
            with open(f'{ptf}/saves/{name}.json', 'r') as i:
                curSave = i.read()
                setup = False

while running:
    clearConsole()
    ui.divider()
    print("Commands:\nA - Achievements\nI - Inventory\nS - Shop\nD - Dungeon\nS - Story\nSQ - Save and Quit\n")
    command = input("[Command]>>> ").lower()
    if command == 'a':
        ui.divider()
        clearConsole()
        for key in achievements.retDict().keys():
            val = ''
            if key == 'enter_dungeon':
                val = 'Dungeon Dweller'

            elif key == 'get_iron':
                val = 'Suited'

            elif key == 'get_crystal':
                val = 'Bright Shine'

            elif key == 'get_dragonic':
                val = 'Fly and Fry'

            print(f'{ui.midReturn(val)}: {ui.midReturn(achievements.retDict()[key])}')
        conf = input("Enter to Continue: ")
quit()
