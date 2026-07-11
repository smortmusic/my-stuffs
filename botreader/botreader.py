import discord
from redbot.core import commands

class BotReader(commands.Cog):
    """Allows Red to listen to messages sent by other bots."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Ignore messages sent by this specific bot instance
        if message.author.id == self.bot.user.id:
            return

        # Check if the message is from another bot
        if message.author.bot:
            # OPTIONAL: Check if the message starts with your prefix to manually trigger commands
            ctx = await self.bot.get_context(message)
            if ctx.valid:
                await self.bot.invoke(ctx)
                return
            
            # --- YOUR CUSTOM LOGIC HERE ---
            # You can handle embeds, trigger actions, or log text from other bots.
            # Example: print(f"Bot {message.author} said: {message.content}")
