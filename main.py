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

class UI:
  def __init__(self):
    pass
  def divider(self):
    print('▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂')
  def divideret(self):
    return '▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂'
  def midt(self,text):
    print(f'[{text}]')
  def midtr(self,text):
    return f'[{text}]'

class Shop:
  def __init__(self):
    self.stock = {}
    self.prices = {}
  def menu(self):
    string = ''
    for item in self.stock.keys():
      for price in self.prices.keys():
        string = string + (f'[{item[0].upper()+item[1:]}][Available:|{self.stock[item]}|Cost:|₪{self.prices[price]}|]\n\n')
        break
    return string
  def stockUpdate(self,value):
    for item in self.stock.key():
      self.stock[item] += value
  def newItem(self,name,avl,price):
    self.stock[name] = avl
    self.prices[name] = price
  def delItem(self, name):
    del self.stock[name]
    del self.prices[name]

newshop = Shop()
newshop.newItem('apple',7,5)
newshop.newItem('banana',7,5)
newshop.newItem('orange',7,5)
newshop.newItem('mango',7,5)
print(newshop.menu())