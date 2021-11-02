import discord
import asyncio
import random 
import time

intents= discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    mention = message.author.mention
    jogos = ['jogo do chute','jogo da velha']
    #Primeira validação: verficar se o autor da mensagem não é o próprio bot
    if author == 'Bot de Teste':
        return
    if content == 'jogos':
        for i in jogos:
            await channel.send(i)

    if content =='jogo do chute':
        await channel.send('De 1 até quanto você quer que eu escolha?')
        limite = message.content
        time.sleep(3)
        print(limite)                            
        await channel.send(limite)
    
    if content == 'boa noite' and author =='guigs':
        await channel.send(f'Boa noite {mention}, o mais gato desse servidor!')
        await message.add_reaction('♥')
    elif content=='boa noite' and author=='mano well':
        await channel.send(f'Boa noite {mention},o mais tiltado do servidor, vava?')
    elif content =='boa noite':
        await channel.send(f'Boa noite {mention},sua beleza não se compara ao @guigs !')
    
        
        # chute = int(await channel.send('Qual seu chute?'))



    if content == 'bom dia' and channel.name == 'geral' :
       await channel.send('Bom dia! ' + mention)
       await message.add_reaction("♥")
    
    


client.run('ODU5MTYwMDc3NTc5NzE0NTcw.YNopLA.fq3R8FMVXRKqPBcwP2bu3MhNgeQ')

#client.run('ODU5MTYwMDc3NTc5NzE0NTcw.YNopLA.fq3R8FMVXRKqPBcwP2bu3MhNgeQ')


#ODU5MTYwMDc3NTc5NzE0NTcw.YNopLA.fq3R8FMVXRKqPBcwP2bu3MhNgeQ
