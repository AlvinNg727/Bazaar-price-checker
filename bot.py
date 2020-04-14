import discord
from discord.ext import commands
import getAverage

client = commands.Bot(command_prefix="!")

using = False

item = ""

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("ur mom"))
    print("Bot is ready")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments.")

@client.command()
async def ping(ctx):
    ms = round(client.latency * 1000)
    print(ms)
    await ctx.send(f"{ms}ms")

@client.command()
async def i(ctx, *, itemName):
    global using, item
    item = itemName
    print(item)
    if itemName == "a*":
        await ctx.send("A* is only average.")
        using = False
    else:
        using = True
        await ctx.send("What is the amount:")
    
@client.command()
async def a(ctx, amount):
    global using, item
    print(amount)
    if using == True:
        using = False
        final = getAverage.input(item, int(amount))
        try:
            await ctx.send(f"You can earn around {round(final, 1)} coins.")
            print(round(final, 1))
        except Exception:
            await ctx.send("That is not an item.")
    elif using == False:
        await ctx.send("You have not given an item first.")
    
client.run("NjM2ODgzNjM2OTAxMjQ5MDI3.XpWXjA._4chcwWjKQh5qz1RNSZyLHkRLac")