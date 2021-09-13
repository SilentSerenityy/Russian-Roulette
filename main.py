#Programmer Name : Shadi
#Programming Date : February 5th, 2021. 05:50 UTC - 5
#Program Purpose : Simulates a Russian Roulette game with 6 players and the proper chances of the gun firing.

import random
from random import choice
#this will randomly pick the player and if the gun fires

import time
from time import sleep
#this will make the output not so "in your face"

import markdown
from colorama import init
from termcolor import colored
#this to format the messages if the gun fired
#red for fired, green for not fired

print("Let's play Russian Roulette!")
you = input("Your name: ")
print()

players = ["John" , "Ryan" , "Nelson" , "Sam" , you] #a list of the players and if the bullet fires.
fires = ["Yes" , "No" , "No" , "No" , "No" , "No"] #being that there is only one bullet only one "yes" has to exist


n = 5 #even though there is 6 chambers/spins/turns, Python considers "0" as a "1", and therefore putting "6" would incorrectly simulate 7 bullets

while n > -1: #while the amount bullets is more than 0

  print("Spinning the revolver...\n")
  time.sleep(2)

  playerturn = random.choice(players)
  fireturn = random.choice(fires)
  #this randomly picks the player and if the gun fires or not

  print(f"The revolver has landed on {playerturn}!\nWill it discharge?\n")
  time.sleep(2)

  if fireturn == "No":
    print(colored(f"{playerturn} got lucky. There are {n} turns of the chamber left.\n","green"))
    #the colored part is coming from the package, it colors the text green as told by ,"green", in this case to indicate the player has been lucky. The below line will remove that chance of the gun firing from the list
    fires.remove(fireturn)

  else:
    print(colored(f"{playerturn} has been eliminated. There are {n} turns of the chamber left.\n","red"))
    #same aspect as the above, now the text is red, and not only will the chance of firing be removed, but the player as well, as they are "unlucky"
    fires.remove(fireturn)
    players.remove(playerturn)
    #removes the chance from the list, and the player from the list as well.
    #this will be able to narrow down the chances and make it more realistic.

  n = n - 1 #this is the looping of the chamber spins

time.sleep(2) #less in your face, otherwise the entire script would've been completed in literally a second

for x in players:
  print(f"{x} has won!") #this is the looping of the players that won, or haven't been "unlucky"

  #one day I'll add a play again?
