import discord
import ollama

f = open(".env")
discord_token = f.readline().split('=', 1)[1]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')


@client.event
async def on_message(message):
    print(f'Messages from {message.author}: {message.content}')
    if message.author == client.user:
        return

    channel = message.channel
    if channel.name == "do-not-post":
        member = message.author
        await member.ban(delete_message_days=1, reason= "SPAM!")

# VIBE CODED
#     if message.content.startswith('!join'):
#         if message.author.voice:
#             channel = message.author.voice.channel
#
#             # Bot join ke channel
#             voice_client = await channel.connect()
#             await message.channel.send(f"Berhasil join ke: **{channel.name}**")
#
#             try:
#                 # Menggunakan FFmpeg untuk menangkap input audio default PC (Mikrofon)
#                 # 'audio=Microphone (...)' bisa diganti dengan nama device audio kamu
#                 FFMPEG_OPTIONS = {
#                     'executable': 'ffmpeg',  # Pastikan ffmpeg sudah di PATH
#                     'before_options': '-f dshow',
#                     'options': '-ac 2 -ar 48000'
#                 }
#
#                 device_input = 'audio=CABLE Output (VB-Audio Virtual Cable)'
#
#                 # Mulai streaming suara PC ke Discord
#                 source = discord.FFmpegPCMAudio(device_input, **FFMPEG_OPTIONS)
#                 voice_client.play(source)
#                 await message.channel.send("Sekarang menyalurkan suara dari PC ke Voice Channel...")
#
#             except Exception as e:
#                 await message.channel.send(f"Gagal memutar audio: {e}")
#         else:
#             await message.channel.send("Kamu harus masuk ke voice channel dulu!")
#
#     elif message.content.startswith('!leave'):
#         voice_client = message.guild.voice_client
#         if voice_client:
#             if voice_client.is_playing():
#                 voice_client.stop()  # Hentikan audio sebelum disconnect
#             await voice_client.disconnect()
#             await message.channel.send("Bot telah keluar dari voice channel.")
#         else:
#             await message.channel.send("Bot sedang tidak ada di voice channel mana pun.")


client.run(discord_token)