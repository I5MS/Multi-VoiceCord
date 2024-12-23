from discord import Client

client = Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await client.get_channel(1111111111111111111).connect()

client.run('Your_Token_Here', bot=False)
