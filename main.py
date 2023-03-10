# Jegliche Videos/Bilder sind auf meinen discord server gespeichert (Alles aus cdn.discordapp.com). 
# Das verhindert Traffic und macht vieles einfacher, wenn der Kanal auf dem die Videos drauf sind nicht mehr existiert heißt dass das alle Funktionen mit Videos/Bilder auch nicht mehr existieren


import discord
import os 
import random
from dotenv import load_dotenv
from time import ctime


load_dotenv() 
bot = discord.Bot(intents=discord.Intents.all())

speechbubble = ["https://media.discordapp.net/attachments/1083494559994105967/1083716039247925338/watermark.png?width=960&height=540", "https://media.discordapp.net/attachments/1083494559994105967/1083716055962238996/watermark.png?width=928&height=618", "https://media.discordapp.net/attachments/1083494559994105967/1083715898285772870/watermark.png?width=825&height=618", "https://media.discordapp.net/attachments/1083494559994105967/1083715850797846568/watermark.png", "https://media.discordapp.net/attachments/1083494559994105967/1083715820091342888/watermark.png", "https://media.discordapp.net/attachments/1083494559994105967/1083715777535942656/watermark.png", "https://media.discordapp.net/attachments/1083494559994105967/1083715751153762304/watermark.png", "https://media.discordapp.net/attachments/1083494559994105967/1083715707960828024/watermark.png", "https://media.discordapp.net/attachments/1083494559994105967/1083715587080982568/watermark.png?width=463&height=618", "https://media.discordapp.net/attachments/1083494559994105967/1083715541442777098/watermark.png", "https://media.discordapp.net/attachments/1083494559994105967/1083715501810778152/watermark.png?width=879&height=618", "https://media.discordapp.net/attachments/1083494559994105967/1083715465546825728/watermark.png?width=960&height=540", "https://media.discordapp.net/attachments/1083494559994105967/1083715411431936041/watermark.png?width=618&height=618", "https://media.discordapp.net/attachments/1083494559994105967/1083715345707176067/watermark.png?width=960&height=461", "https://media.discordapp.net/attachments/1083494559994105967/1083715284025753710/watermark.png?width=960&height=540", "https://media.discordapp.net/attachments/1083494559994105967/1083715236441374800/watermark.png?width=928&height=618", "https://media.discordapp.net/attachments/1083494559994105967/1083715188043305020/watermark.png?width=960&height=480"]
abgenickt = ["Abgenickt", "Angepisst"]
technick = ["https://cdn.discordapp.com/attachments/1083466887117152293/1083724257726582844/KkbhurR.mp4", "https://cdn.discordapp.com/attachments/1083466887117152293/1083724423699382272/WcCidNe.webm", "https://cdn.discordapp.com/attachments/1083466887117152293/1083724601915355236/BaAmIRW.mp4", "https://cdn.discordapp.com/attachments/1083466887117152293/1083724664687300648/yZCnrMe.webm", "https://cdn.discordapp.com/attachments/1083466887117152293/1083724746786615317/NcUn3Tz.webm", "https://cdn.discordapp.com/attachments/1083466887117152293/1083724811823489054/Z9kAxrM.webm", "https://cdn.discordapp.com/attachments/1083466887117152293/1083724915213078568/5aA2pvl.webm", "https://cdn.discordapp.com/attachments/1083466887117152293/1083724987090870282/MlOpYLy.webm", "https://cdn.discordapp.com/attachments/1083466887117152293/1083725046050213909/KOw1rZB.webm", "https://cdn.discordapp.com/attachments/1083466887117152293/1083725101599576094/Z1oQDpU.mp4", "https://cdn.discordapp.com/attachments/1083466887117152293/1083725191563186236/qlYXsWX.mp4"]


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="FIFA")) # Zeigt dass der Bot "FIFA" spielt.
    print(ctime() + ": " f"{bot.user} ist online") 

@bot.event
async def on_message(message: discord.message): # wenn der bot markiert wird schickt er ein element aus der speechbubble liste und löscht die ursprüngliche nachricht
    if str(bot.user.id) in message.content:
        await message.delete()
        await message.channel.send(random.choice(speechbubble))
        print(ctime() + ": " " speechbubble wurde benutzt")
        
@bot.slash_command(name = "technick", description = "Bei Technik fragen Tech-Nick fragen!") #/technick befehl. Schickt ein zufälliges Element aus der technick liste.
async def werbespot(ctx):
    await ctx.respond(random.choice(technick))
    print(ctime() + ": " "/technick wurde benutzt")

@bot.slash_command(name = "entscheidung", description = "Ist diese Nachricht abgenickt oder angepisst von technik 🤔") # /entscheidung befehl. Schickt ein zufälliges Element aus der technick liste.
async def auswahl(ctx):
    await ctx.respond(random.choice(abgenickt) + " von Technik!")
    print(ctime() + ": " "/entscheidung wurde benutzt")

@bot.slash_command(name = "techfakt", description = "Tech Nick erzählt euch einen zufälligen Tech Fakt!") # /techfakt befehl. Schickt eine zufällige Zeile aus der Datei fakt.txt
async def fakt(ctx):
    await ctx.respond(random.choice(open("fakt.txt").readlines())) 
    print(ctime() + ": " "/fakt wurde benutzt")

@bot.slash_command(name = "geld", description = "Gratis Geld Download") # /geld befehl. gratis geld download
async def geld(ctx):
    await ctx.respond("https://cdn.shopify.com/s/files/1/0550/1383/4888/files/Gratis_Geld.jpg?v=1656120813&width=550")
    await ctx.send("Gratis Geld Download!")
    print(ctime() + ": " "/geld wurde benutzt")

bot.run(os.getenv('TOKEN')) 
