import discord
from discord.ext import commands, tasks

import ClientConfig
client = ClientConfig.client

import os
from dotenv import load_dotenv
import B

import random
from random import choice
import time
from time import sleep

@client.event
async def on_ready():
  print('Logged in as:')
  print("Username:", client.user.name)
  print("Client ID:", client.user.id)
  print('-----------------------------')
  await client.change_presence(status=discord.Status.idle)

@client.command()
async def rr(ctx, name):
  if name = None:
    await ctx.send("You haven't put in a name!")
   else:
    await ctx.send(f"Nice! Your name is {name}")
    players = ["John" , "Ryan" , "Nelson" , "Sam" , you]
    fires = ["Yes" , "No" , "No" , "No" , "No" , "No"]
    n =5
    
    while n > -1:
      await ctx.send("Spinning the revolver...\n")
      time.sleep(2)
      playerturn = random.choice(players)
      fireturn = random.choice(fires)
      
      await ctx.send(f"The revolver has landed on {playerturn}!\nWill it discharge?\n")
      time.sleep(2)
      
      if fireturn == "No":
        await ctx.send(f"{playerturn} got lucky. There are {n} turns of the chamber left.\n")
        fires.remove(fireturn)
        
      else:
        await ctx.send(f"{playerturn} has been eliminated. There are {n} turns of the chamber left.\n")
        fires.remove(fireturn)
        players.remove(playerturn)
      
      n = n - 1
      time.sleep(2)
      
      for x in players:
        print(f"{x} has won!")
  
B.b()
client.run(os.getenv('TOKENA'))
