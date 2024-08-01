from discord import Client, Intents

client = Client(intents=Intents.default())


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    voice_channel = client.get_channel(1111111111111111111)
    await voice_channel.connect()
    print('Connected to voice channel: {}'.format(voice_channel))


client.run("Your_Token_Here")
