from .botreader import BotReader

async def setup(bot):
    await bot.add_cog(BotReader(bot))
