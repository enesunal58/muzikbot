import discord
from discord.ext import commands
import youtube_dl


class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def kanal(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Herhangi bir ses kanalında değilsiniz")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
             await ctx.voice_client.move_to(voice_channel)
             
    @commands.command()
    async def baglantiyi_kes(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def oynat(self, ctx, url):
        ctx.voice_client.stop()
        FFMEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info ['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def durdur(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Durduruldu ⏸️")

    @commands.command()
    async def devam(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Devam ettiriliyor ▶️")

    def setup(client):
        client.add_cog(music(client))