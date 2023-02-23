# Jegliche Videos/Bilder sind auf meinen discord server gespeichert (Alles aus cdn.discordapp.com). 
# Das verhindert Traffic und macht vieles einfacher, wenn der Kanal auf dem die Videos drauf sind nicht mehr existiert heißt dass das alle Funktionen mit Videos/Bilder auch nicht mehr existieren


import discord
import os 
import random
from dotenv import load_dotenv

load_dotenv() 
bot = discord.Bot()

technick = ["https://cdn.discordapp.com/attachments/1078032962706231316/1078040293884043294/4hHXi9z.mp4","https://cdn.discordapp.com/attachments/1078032962706231316/1078040311860826183/iEwMepU.mp4"]
abgenickt = ["Abgenickt", "Angepisst"]
speechbubble = ["https://media.discordapp.net/attachments/1078032962706231316/1078239280813592687/watermark.png?width=916&height=610", "https://media.discordapp.net/attachments/1078032962706231316/1078239378826088499/watermark.png?width=960&height=543", "https://media.discordapp.net/attachments/1078032962706231316/1078239432622219285/watermark.png?width=960&height=480", "https://media.discordapp.net/attachments/1078032962706231316/1078239499064188990/watermark.png?width=960&height=540", "https://media.discordapp.net/attachments/1078032962706231316/1078239562557554689/watermark.png", "https://media.discordapp.net/attachments/1078032962706231316/1078239602457989210/watermark.png?width=960&height=540", "https://media.discordapp.net/attachments/1078032962706231316/1078239730002571334/watermark.png?width=960&height=480", "https://media.discordapp.net/attachments/1078032962706231316/1078239815562182736/watermark.png"]
# die sprechblase ist etwas was ich noch einbauen will, momentan bin ich mir aber unsicher wie genau es umgesetzt werden soll

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="FIFA")) # Zeigt dass der Bot "FIFA" spielt.
    print(f"{bot.user} ist online")

@bot.slash_command(name = "technick", description = "Bei Technik fragen Tech-Nick fragen!") #/technick befehlt. Schickt ein zufälliges Element aus der technick liste.
async def werbespot(ctx):
    await ctx.respond(random.choice(technick))

@bot.slash_command(name = "entscheidung", description = "Ist diese Nachricht abgenickt oder angepisst von technik 🤔") # /entscheidung befehlt. Schickt ein zufälliges Element aus der technick liste.
async def auswahl(ctx):
    await ctx.respond(random.choice(abgenickt) + " von Technik!")

@bot.slash_command(name = "techfakt", description = "Tech Nick erzählt euch einen zufälligen Tech Fakt!") # /techfakt befehlt. Schickt eine zufällige Zeile aus der Datei fakt.txt
async def fakt(ctx):
    await ctx.respond(random.choice(open("fakt.txt").readlines())) 




bot.run(os.getenv('TOKEN')) 