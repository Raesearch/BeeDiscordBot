import discord
import responses


async def send_message(message, user_message, is_private):
    if "https://x.com" in user_message or "https://twitter.com" in user_message:
        try:
            response = responses.embedfix(user_message)
            await message.author.send(response) if is_private and response else await message.channel.send(response)

        except Exception as ex:
            print(ex)


def run_discord_bot():
    TOKEN = "MTE2NDIyNDk1Mjc0OTI2OTA4Mw.GY5bKL.S7i9EsenSgVk0uTFvDasi3Z-9gHvCWISP0mTJ8"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} running..')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
