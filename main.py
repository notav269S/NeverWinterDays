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
