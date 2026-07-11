import discord
from redbot.core import commands

class BotReader(commands.Cog):
    """Allows Red to listen to messages sent by other bots."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.id == self.bot.user.id:
            return

        if message.author.bot:
            ctx = await self.bot.get_context(message)
            if ctx.valid:
                await self.bot.invoke(ctx)
                return

# --- THIS IS THE CRITICAL MISSING BLOCK RED NEEDS ---
async def setup(bot):
    await bot.add_cog(BotReader(bot))
