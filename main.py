import discord
from discord.ext import commands
from random import randint
from config import *

bot = commands.Bot(command_prefix='!')

pet = {
    'health': 500,
    'strength': 500,
    'defense': 100,
}

resources = {
    'food': 50,
    'energy': 30,
    'coins': 50,
    'diamond': 0,
}

@bot.command('train')
async def train(ctx):
    if resources['energy'] >= 3:
        pet['strength'] += 2
        pet['health'] -= 10
        resources['energy'] -= 3
        await ctx.send('Ваш питомец прошел изнурительные тренировки')
        await ctx.send(str(pet))
    else:
        await ctx.send('У вас мало энергии')

@bot.command('feed')
async def feed(ctx):
    if resources['food'] >= 5:
        pet['health'] += 20
        resources['food'] -= 5
        await ctx.send('Ваш питомец хорошо покушал')
        await ctx.send(str(pet))
    else:
        await ctx.send('У вас мало еды.')

@bot.command('fight')
async def fight(ctx):
    enemy = {
        'health': randint(1, 10),
        'strength': randint(1, 10),
        'defense': randint(1, 10),
    }
    await ctx.send('Вы атакуете врага')
    while enemy['health'] >= 0 and pet['health'] >= 0:
        pet['health'] -= enemy['strength'] - pet['defense']
        enemy['health'] -= pet['strength'] - enemy['defense']
        await ctx.send('Ваш питомец:'+str(pet))
        await ctx.send('Враг :'+str(enemy))
    if enemy['health'] > pet['health']:
        await ctx.send('Вы проиграли')
        food = randint(10, 15)
        energy = randint(15, 20)
        coins = randint(10, 15)
        resources['food'] -= food
        resources['energy'] -= energy
        resources['coins'] -= coins
        await ctx.send(f'Вы потеряли ресурсы:\nЕда -{food}\nЭнергия -{energy}\nКоиниы -{coins}')
    else:
        food = randint(10, 15)
        energy = randint(15, 20)
        coins = randint(10, 15)
        await ctx.send('Вы победили')
        resources['food'] += food
        resources['energy'] += energy
        resources['coins'] += coins
        
        await ctx.send(f'вы добыли ресурсы: :\nЕда -{food}\nЭнергия -{energy}\nКоиниы -{coins}')
        print(f"food: {resources['food']}\nenergy: {resources['energy']}\ncoins: {resources['coins']}")

print(f"food: {resources['food']}\nenergy: {resources['energy']}\ncoins: {resources['coins']}")
bot.run(TOKEN)


