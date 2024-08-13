from discord import Client, Intents

client = Client(intents=Intents.default())


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    voice_channel = client.get_channel(1111111111111111111)
    await voice_channel.connect()


client.run("Your_Token_Here", bot=False)
