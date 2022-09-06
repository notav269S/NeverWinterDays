from random import randint,choice
from os import system
from time import sleep

def wait(dur):
  sleep(dur)
  
def clearConsole():
  system('clear')
  system('cls')
  
def loading(msg, dur):
  for i in range(0, dur*3):
    clearConsole()
    print(f"{msg}.")
    wait(1/3)
    clearConsole()
    print(f"{msg}..")
    wait(1/3)
    clearConsole()
    print(f"{msg}...")
    wait(1/3)
    clearConsole()
    
class Inventory:
  def __init__(self):
    self.inv = {
      '':0,
      '':0,
      '':0,
      '':0,
      '':0,
      '':0,
      '':0,
      '':0,
      '':0,
      '':0,
      '':0,
      '':0,
      '':0
    }

  def getValue(self,food):
    return self.inv[food]

  def changeValue(self,item,num):
    self.inv[item] += num
    
class Health:
  def __init__(self):
    self.health = 20
  def getHeath(self):
    return self.health
  def verify(self):
    if self.health > 20:
      self.health = 20:
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
      self.hunger = 20:
    elif self.hunger < 0:
      self.hunger = 0
    if self.hunger == 0:
      health.changeHealth(-4)
      print("You lost some health because your hunger is low. This can kill you.")
  def changeHunger(self, val):
    self.hunger += val
    self.verify()
