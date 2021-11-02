import json
import discord
import random
from discord.ext import commands, tasks
import pandas as pd
import youtube_dl
import os


with open('config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefixo = infos['prefix']
    ownerID = infos['owner_id']

client = commands.Bot(command_prefix=prefixo,intents=discord.Intents.all())
emojisCool =['','','','','','','']
@client.event
async def on_ready():
    print(f'Bot Online!\nID: {client.user.id}\nNome: {client.user.name}')

#moeda    
@client.command(aliases=['Cara ou Coroa','caraoucoroa','cara ou coroa'])
async def moeda(ctx):
    num = random.randint(1, 2)
    if num==1:#cara
        msg = await ctx.send('Você tirou cara!') #:grinning:
        await msg.add_reaction('😀')
    elif num==2:#coroa
        msg = await ctx.send('Você tirou coroa!')#:crown:
        await msg.add_reaction('👑')

#say it
@client.command(aliases=['falar','diga','fale'])
async def say(ctx,*,mensagem):
    await ctx.send(mensagem)

#teste
@client.command()
async def teste(ctx):
    if ctx.author.id == ownerID:
        
        await ctx.send(f'{ctx.author}, você é o desenvolvedor desse bot!')

#dm
@client.command()
async def dm(ctx,*,mensagem):
    user = client.get_user(mensagem)
    await user.send("oi")

@client.command()
async def p(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Espere a música acabar!")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Geral')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
    


    ydl_opts = {'format':'bestaudio/best',
    'postprocessorrs':[{
        'key':'FFmpegExtractAudio',
        'preferredcodec':'mp3',
        'preferredquality':'192',
        }],
        }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def l(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Bot não está conectado em um canal!")
    
@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Nenhuma música está tocando no momento")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("A música não está pausada")


@client.command()
async def stop():
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


player1 = ""
player2 = ""
turn = ""
gameOver = True
board = []
winningConnditions = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]
@client.command(aliases=['Jogo da velha'])
async def velha(ctx, p1: discord.Member, p2: discord.Member):
    global player1
    global player2
    global turn
    global gameOver
    global count

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        #Printar o quadro
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        
        #determinar quem vai primeiro
        num = random.randint(1, 2)
        if num == 1:
            turn = player1 
            await ctx.send("É a vez de <@"+str(player1.id)+"> jogar.")
        elif num == 2:
            turn = player2
            await ctx.send("É a vez de <@"+str(player2.id)+"> jogar.")
    else:
        await ctx.send("Um jogo já está em progresso! Termine ele primeiro antes de começar outro!")


@client.command()
async def pos(ctx, pos: int):
    global player1
    global player2
    global turn
    global board
    global count
    
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                #Printar o quadro
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConnditions, mark)
                if gameOver:
                    await ctx.send(mark + " venceu!")
                elif count>=9:
                    gameOver = True
                    await ctx.send("Deu velha!")

                #troca turno
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1

            else:
                await ctx.send("Escolha um número inteiro entre 1 e 9")
        else:
            await ctx.send("Não é a sua vez!")
    else:
        await ctx.send("Não tem nenhum jogo acontecendo seu bobo(a)!")  


def checkWinner(winningConnditions,mark):
    global gameOver
    for condition in winningConnditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@velha.error
async def velha_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Por favor, mencione dois jogadores!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Por favor tem certeza de mencionar/pingar jogadores. Exemplo: <@130131497121349632>")

@pos.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Por favor, mencione dois jogadores!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Por favor tem certeza de colocar um inteiro")
client.run(TOKEN)