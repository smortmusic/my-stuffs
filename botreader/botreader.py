import discord
from redbot.core import commands

class BotReader(commands.Cog):
    """Bypasses core Red filters to process automated bot messages."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # 1. Ignore messages sent by this specific bot to prevent loops
        if message.author.id == self.bot.user.id:
            return

        # 2. Check if the message is coming from another bot application
        if message.author.bot:
            content = message.content.strip()

            # 3. Check for your custom trigger prefix (e.g., "t!")
            if content.startswith("t!"):
                # Strip the prefix out to read the actual instruction
                command_text = content[2:].strip().lower()

                # --- MANUAL REACTION LOGIC ---
                # Example: If another bot types "t!ping", Red responds with "Pong!"
                if command_text == "ping":
                    await message.channel.send("Pong! (Read from bot)")
                    return

                if command_text == "hello":
                    await message.channel.send(f"Hello, {message.author.name}!")
                    return

                # You can add more automated actions or text responses here
