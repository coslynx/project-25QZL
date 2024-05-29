# message_filter.py (Python)

import discord
from discord.ext import commands

class MessageFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Add your message filtering logic here
        if "bad_word" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

def setup(bot):
    bot.add_cog(MessageFilter(bot))