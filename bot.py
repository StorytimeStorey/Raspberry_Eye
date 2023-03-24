#bot to look at chosen channels
#look for uploads and connected messages
#look for .stl, .obj, and whatever else
#save to a folder
#compile an email with this info
#email a person the info



import discord
import info_parcer as info

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_read():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("hello!")

    if message.content.startswith('$status'):
        current_status = info.read_last_row('status_data.csv')
        await message.channel.send(f"{current_status}")

    if message.content.startswith("$graph"):
        info.make_graph()
        with open('temperature_and_humidity.png', 'rb') as file:
            image = discord.File(file)
        await message.channel.send(file=image)

client.run("MTA1ODg2NjI2MjY4OTcyMjUxMA.GDbe49.fr8TWeqw66o6LVQh_FCHPSkl5GtXy71yZO8YEc")