# names: Aarsh, Ron, Misal, Georgie
# date: Mon Dec 12
# -*- python 3.8.12 -*-

import cmd
import textwrap
import sys
import os
import time
import random
from pprint import pprint
import datetime
import subprocess
from pytimedinput import timedInput, timedKey


# constants
answer = None
starttime = time.localtime()



# classes
class Player:
  """Player class represents a player and manipulates their status"""

  def __init__(self, name, date):
    self.name = name
    self.health = 100
    self.date = date
    self.food = 10
    self.happiness = 80

  def print_status(self):
    print(esc("34;1;4") + "Status" + esc(0))
    print("Health: {}/100".format(self.health))
    print("Date: {}".format(self.date.strftime("%m/%d/%y")))
    print("Food: {} lbs".format(self.food))
    print("Happiness: {}/100\n".format(self.happiness))

  def update_player(self):
    self.date += datetime.timedelta(days=1)
    self.food -= 3
    if self.food <= 0:
      self.food = 0
      self.health -= 15
    else:
      self.inc_health(4)
    if self.happiness <= 25:
      self.health -= 10
    self.random_events()

  def inc_health(self, num):
    if (num + self.health) < 100:
      self.health += num
    else:
      self.health = 100

  def hunt_minigame(self, animal, food, wind, pos, speed):
    for i in range(50):
      if wind == 0:
        menprint("The animal is running across the forest. When it aligns with your bow and arrow's line of sight, shoot it by pressing ENTER! The arrow at the bottom signifies the position of your bow and arrow.", 32)
      elif wind < 0:
        menprint("The animal is running across the forest. When it aligns with your bow and arrow's line of sight, shoot it by pressing ENTER! The arrow at the bottom signifies the position of your bow and arrow. Be aware of the light westward wind of " + str(abs(wind)), 32)
      else:
        menprint("The animal is running across the forest. When it aligns with your bow and arrow's line of sight, shoot it by pressing ENTER! The arrow at the bottom signifies the position of your bow and arrow. Be aware of the light eastward wind of " + str(abs(wind)), 32)
      print(" "*i+(animal))
      print(" "*(pos)+"^")
      userText, timedOut = timedKey("Press enter to shoot: ", timeout=speed)
      if(timedOut):
        os.system('clear')
        continue
      else:
        if i == (pos+wind):
          menprint("Good job! You got the animal!", 31)
          self.food += food
          return
        else:
          menprint("Unfortunately, you missed the animal :(")
          return

  def hunt(self):
    os.system('clear')
    menprint("You take pride in living off the land and hunting your own food. You wanted to prove to yourself that you could live on your own and without anyone’s help. However, hunting requires you to devote a large part of each day to stalking animals. You are only equipped with a bow and one arrow. Use it cautiously and wisely.\n\n Do you want to hunt a squirrel, rabbit, deer, or moose. Be aware that the larger the animal, the harder it is to shoot", 35)
    animal = input("Enter the animal you want to hunt: ")
    os.system('clear')
    if animal=="squirrel":
      self.hunt_minigame("🐿️", 3, 0, random.randint(3, 7), 1)
    elif animal=="rabbit":
      self.hunt_minigame("🐇", 5, random.randint(-2,2), random.randint(5,15), 0.8)
    elif animal=="deer":
      self.hunt_minigame("🦌", 10, random.randint(-5,5), random.randint(6, 17), 0.6)
    elif animal=="moose":
      self.hunt_minigame("🦌", 20, random.randint(-8,8), random.randint(10, 20), 0.5)
    input("\nPress the ENTER key to continue")
    

  def rest(self,snow=False):
    os.system('clear')
    woke_up=0
    menprint("There is a one in sixty chance that you get attacked by a bear and, if this occurs when you have less than 7 hours of sleep, you lose 10 health. You gain 20 health for a full 9 hours", 96)
    for i in range(540):
      hour=int(i/60)
      min=i%60
      bear=69
      if hour>=1:
        if i<420:
          bear=random.randint(0,1139)
        else:
          bear=random.randint(0,119)
      print("😴You have been asleep for: "+str(hour)+":"+str(min), end="\r", flush=True) 
      time.sleep(0.01)
      woke_up+=1
      if (bear==min):
        print("\n", flush=True)
        time.sleep(3)
        print("You got scared awake by a bear!!!")
        if (hour<7):
          print("You lose 10 health because you didn't get enough sleep")
          self.health-=10
        else:
          print("It is okay though, you got your 7 hours of sleep")
        break
    if woke_up==540:
      print("\n", flush=True)
      time.sleep(3)
      print("You made it through the night!! +20 health")
      self.inc_health(20)
    if snow==True:
      print("During the night, the snow melted. You are  now free to continue on your travels.")
    input("\nPress the ENTER key to continue")


  def read(self):
    os.system('clear')
    menprint("Works by Jack London, Henry David Thoreau, and Tolstoy compel you to keep exploring and spiritually to the wild around you. Ideas about socialism and solitude unlock your freedom of thought to understand that you dislike capitalism and conformity and instead subscribe to transcendentalist beliefs. 📕\n\nWhich book do you want to read:\n1. Walden\n2. Call of the Wild\n3. Terminal Man", 91)
    self.happiness += 10
    number=random.randint(1,3)
    pick = int(input("What is your choice: "))
    if pick == 1:
      print("The reading opened your eyes to a life of solitude")
      time.sleep(0.3)
      if number==pick:
        self.happiness+=3
    elif pick == 2:
      print ("After enjoying Call of the Wild you connect the life of a stranded dog to yours in American society")
      time.sleep(0.3)
      if number==pick:
        self.happiness+=3
    elif pick == 3:
      print ("You connected how the expirements on a sick man are equal to the expirements that happens in society")
      time.sleep(0.3)
      if number==pick:
        self.happiness+=3
    input("\nPress the ENTER key to continue")


  def diary(self):
    os.system('clear')
    menprint("You write about how the simple life of survival and living off the land.", 94)
    questions=["Which college did Chris attend?", "Were the McCandless a low, middle, or high income family?", "What state did Chris live as a child?", "What company did Chris's father work for that made them move?", "What psuedonym does Chris use when first introduced to the reader (full name)", "Who wanted to adopt Chris?", "What is Chris's half brother's first name?", "Where does Chris briefly work?", "What brand of car did Chris have?", "Roughly how far was Chris's bus ride from civilization (miles)?", "In one word what did Chris's belt represent to him? His___", "What was the name of the trail that Mccandless followed", "What type of vehicle was Chris's body found in?", "What did Wayne Westerberg know about Chris that helped police identify him?", "How many months does Chris spend in the wild?", "What vegetables does Krakauer think killed Chris", "What state does Chris travel to go into the wild?", "What is Carine McCandless's relationship to Chris?"]
    answers=["Emory university", "Middle", "Virginia", "Nasa", "Alexander supertramp", "Ronald franz", "Sam", "Mcdonalds", "Datsun", "16", "Future", "Stampede trail", "Bus", "Social security number", "4", "Potatoes", "Alaska", "Sister"]
    choice=random.randint(0,len(questions)-1)
    playerans=input("\nYou get 5 happiness for a right answer and lose 5 happiness for an incorrect answer\n\n" + questions[choice]+"\n")
    playerans=playerans.replace('\'','')
    playerans.strip(playerans)
    if (playerans.capitalize()==answers[choice]):
      print("You get 5 happiness!")
      self.happiness+=5
    else:
      print("The answer is " + answers[choice] + ". You put " + playerans.capitalize()+". You lose 5 happiness.")
      self.happiness-=5
    time.sleep(2)


  
  def farm(self):
    
    pass

  
  def random_events(self):
    os.system('clear')
    bad_luck=random.randint(1,30)
    
    if bad_luck==2:
      self.health-=10
      self.happiness-=10
      for i in range(20):
        os.system('clear')
        menprint("OH NO! In your journeys, you suddenly fell through ice! This is unexpected. Spam ENTER to swim out", 32)
        input()
        print("🌊"+" "*i+"🏃", end="\r", flush=True)
        time.sleep(0.3)
      menprint("Good job! You got through the ice!")
      time.sleep(3)
      input("\nPress the ENTER key to continue")
      
    if bad_luck>0:
      self.health-=10
      self.happiness-=10
      menprint("OH NO! Your bus has been snowed in. Looks like you are going to have to spend an uncomfortable night in the bus.", 30)
      input("\nPress the ENTER key to continue")
      self.rest(snow=True)
      
    if bad_luck==27:
      self.food-=2
      menprint("OH NO! Unfortunately, a part of your recently hunted game has gone bad. You just lost 2 lbs of good food. Take better care of it next time!",93)
      input("\nPress the ENTER key to continue")
      
  





    


# helpers
def menprint(msg, ansi=0):
  tput = subprocess.Popen(['tput', 'cols'], stdout=subprocess.PIPE)
  max = int(tput.communicate()[0].strip())
  print((lambda: "="*len(msg), lambda: "="*max)[len(msg) > max]())
  print(esc(ansi) + msg + esc(0))
  print((lambda: "="*len(msg), lambda: "="*max)[len(msg) > max]())

def esc(code):
  return f'\033[{code}m'

def progress(percent=0, width=30):
  left = width * percent // 100
  right = width - left
  print('\r[', '#' * left, ' ' * right, ']', f' {percent:.0f}%', sep='', end='', flush=True)

  
# main
def main():
  os.system('clear')
  menprint("Welcome to the Into the Wild Trail Game!".title(), '31;1;4')
  name = input("Let's get started with your name: ")
  player = Player(name, datetime.date(1992, 4, 1))
  print("\n\nloading game ")
  #for i in range(101):
  #  progress(i)
  #  time.sleep(0.1)

  os.system('clear')
  menprint(
    "Welcome {}. It is April 1, 1992. You are living in the Alaskan wilderness. You are only equipped with a 10-lb bag of rice, a guide to the region's edible plants, a .22 caliber rifle and ammunition, and a camera. Every day, you are presented with a range of options that affect your status. Your goal is to survive and live a pure transcendentalist life. If your health reaches 0, you die. Good Luck Explorer! You now walk into the wild."
    .format(name.capitalize()), 33)
  input("Press the ENTER key to continue")

  while (player.health > 0):
    os.system('clear')
    player.print_status()
    
    menprint(
      "1. Hunt\n2. Rest\n3. Read\n4. Write in your diary\n", '35')

    valid = False
    while not valid:
      choice = input("\nWhat is your choice: ")
      if choice == '1':
        valid = True
        player.hunt()
      elif choice == '2':
        valid = True
        player.rest()
      elif choice == '3':
        valid = True
        player.read()
      elif choice == '4':
        valid = True
        player.diary()
      else:
        valid = False
    
    player.update_player()
    time.sleep(1)

if __name__ == '__main__':
  main()
