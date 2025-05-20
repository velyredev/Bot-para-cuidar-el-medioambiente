import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def Como_evitar_contaminar(ctx): 
    await ctx.send("No tirar basura a las calles, mar, inodoro, o contenedores equivocados.")


@bot.command()
async def Recomendaciones(ctx):
    await ctx.send("1: Reciclar cada cosa en su contenedor correspondiente")
    await ctx.send("2: Informate bien sobre cuales son los contenedores correspondientes en tu ciudad o pueblo")
   

@bot.command()
async def Medidas_para_descontaminar(ctx):
    await ctx.send("Recoger la basura de las calles y tirarla a su lugar correspondiente(con las medidas adecuadas de higiene)")

    
# Reemplaza por tu token real
bot.run("INTRODUCE TU TOKEN AQUÍ")
