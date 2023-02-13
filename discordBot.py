import discord
import responses

#Very generic way of talking to discord's API

async def send_message(message, text, user_message):
    try:
        response = responses.handle_response(text, user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    #Get your bot token and add it here
    token = "<Your bot token here>"
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} on {channel}')

        if(user_message != ""):
            user_message = user_message.partition(' ')[2]
            print("said something: " + user_message)
            await send_message(message, user_message, username)

    client.run(token)


