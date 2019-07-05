import discord
from discord.ext import commands
import asyncio
import os
from .clib import crimsotools as c
from .clib import imagetools as imagetools

# lists for games in progress
eface_channels = []

# path to root
root_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

class Image:
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='Boop the snoot! Must mention someone to boop.')
    async def boop(self, ctx, mention):
        booper = str(ctx.message.author.nick)
        if booper == 'None':
            booper = str(ctx.message.author.name)
        if mention.startswith('<@') == True:
            mention = str(ctx.message.mentions[0].nick)
            if mention == 'None':
                mention = str(ctx.message.mentions[0].name)
            imagetools.boop(booper,mention)
            await self.bot.send_file(ctx.message.channel,
                                        root_dir+'\\img\\booped.jpg')

    @commands.command(pass_context=True,
                      brief='Convert image to emojis!',
                      description='WARNING: Best on desktop. You will get a '+
                          'LOT of PMs. SVGs are no. '+
                          '\nWorks best with images with good contrast and '
                          'larger features. A one-pixel-wide line is likely '
                          'not going to show up in the final product.\n' +
                          'Try >eimg2 if you want to preserve more detail.')
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def eimg(self, ctx, image=None):
        await self.bot.send_message(ctx.message.author, 'Please wait...')
        imagetools.emojiImage2(ctx, image)
        c.checkin('eimg', ctx.message.server, ctx.message.author, \
                  eface_channels)
        asyncio.sleep(10)
        # read in lines of emojis
        line_list = open(root_dir+'\\img\\emoji.txt',
                         encoding='utf8',
                         errors='ignore').readlines()
        # strip newlines
        line_list = [line.replace('\n','') for line in line_list]
        # send line-by-line as DM
        for line in line_list:
            await self.bot.send_message(ctx.message.author,line)
            await asyncio.sleep(1)
        c.checkout('eimg', ctx.message.server, ctx.message.author, \
                   eface_channels)

    @commands.command(pass_context=True,
                      brief='Convert image to emojis with a bit more detail!',
                      description='WARNING: Best on desktop. You will get a '+
                          'LOT of PMs. SVGs are no. '+
                          '\nWorks best with images with good contrast and '
                          'larger features. A one-pixel-wide line is likely '
                          'not going to show up in the final product.')
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def eimg2(self, ctx, image=None):
        await self.bot.send_message(ctx.message.author, 'Please wait...')

        imagetools.emojiImage2(ctx, image)
        c.checkin('eimg', ctx.message.server, ctx.message.author, \
                  eface_channels)
        asyncio.sleep(10)
        # read in lines of emojis
        line_list = open(root_dir+'\\img\\emoji.txt',
                         encoding='utf8',
                         errors='ignore').readlines()
        # strip newlines
        line_list = [line.replace('\n','') for line in line_list]
        # send line-by-line as DM
        for line in line_list:
            await self.bot.send_message(ctx.message.author,line)
            await asyncio.sleep(1)
        c.checkout('eimg', ctx.message.server, ctx.message.author, \
                   eface_channels)

    @commands.command(pass_context=True, hidden=True)
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def bless(self, ctx):
        """bless bless"""
        # read in lines of emojis
        line_list = open(root_dir+'\\img\\bless.txt',
                         encoding='utf8',
                         errors='ignore').readlines()
        # strip newlines
        line_list = [line.replace('\n','') for line in line_list]
        # send line-by-line as DM
        c.botlog('{} is being blessed...'.format(ctx.message.author))
        for line in line_list:
            await self.bot.send_message(ctx.message.author,line)
            await asyncio.sleep(1)
        c.botlog('{} is blessed!'.format(ctx.message.author))

    @commands.command(pass_context=True, hidden=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def gimme_last(self, ctx):
        await self.bot.send_message(ctx.message.author,'Last eimg:')
        # read in lines of emojis
        line_list = open(root_dir+'\\img\\emoji.txt',
                         encoding='utf8',
                         errors='ignore').readlines()
        # strip newlines
        line_list = [line.replace('\n','') for line in line_list]
        # send line-by-line as DM
        c.botlog('{} is using gimme_last...'.format(ctx.message.author))
        for line in line_list:
            await self.bot.send_message(ctx.message.author,line)
            await asyncio.sleep(1)
        c.botlog('{}\'s gimme_last is done!'.format(ctx.message.author))

    @commands.command(pass_context=True, hidden=True)
    async def eface_pm(self, ctx, userid, *, arg):
        """crimsoBOT avatar as emojis!"""
        if ctx.message.author.id =='310618614497804289':
            # get user object
            user = await self.bot.get_user_info(userid)
            # read in lines of emojis
            line_list = open(root_dir+'\\ref\\emojiface.txt',
                             encoding='utf8',
                             errors='ignore').readlines()
            # strip newlines
            line_list = [line.replace('\n','') for line in line_list]
            line_list = line_list[0:-1]
            # send line-by-line as DM
            for line in line_list:
                await self.bot.send_message(user,line)
                await asyncio.sleep(1)
            await self.bot.send_message(user,arg)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 8*60*60, commands.BucketType.user)
    async def eface(self, ctx):
        """crimsoBOT avatar as emojis!"""
        # read in lines of emojis
        c.checkin('eface', ctx.message.server, ctx.message.author, \
                  eface_channels)
        line_list = open(root_dir+'\\ref\\emojiface.txt',
                         encoding='utf8',
                         errors='ignore').readlines()
        # strip newlines
        line_list = [line.replace('\n','') for line in line_list]
        for line in line_list:
            await self.bot.send_message(ctx.message.author, line)
            await asyncio.sleep(1)
        c.checkout('eface', ctx.message.server, ctx.message.author, \
                   eface_channels)

    @commands.command(pass_context=True)
    async def acidify(self, ctx, number_of_hits, image=None):
        """1-3 hits only. Can use image link, attachment, mention, or emoji."""
        try:
            if not 1 <= int(number_of_hits) <= 3:
                raise ValueError
        except ValueError:
            return commands.CommandInvokeError('Wrong number of hits')
        c.botlog('acidify running on {}/{}...'.format(ctx.message.server,
                                                      ctx.message.channel))
        imagetools.acid(ctx, int(number_of_hits), image)
        ess = 's'
        if int(number_of_hits) == 1:
            ess = ''
        await self.bot.send_file(ctx.message.channel,
                                 root_dir+'\\img\\acid_.png',
                                 content='**'+number_of_hits+' hit'+ess+':**')
        c.botlog('acidify COMPLETE on {}/{}!'.format(ctx.message.server,
                                                     ctx.message.channel))

    @commands.command(pass_context=True, hidden=True)
    async def inspect(self, ctx, id=None):
        if ctx.message.author.id != '310618614497804289':
            return
        # read in lines of emojis
        line_list = open(root_dir+'\\games\\emojilist.txt',
                         encoding='utf8',
                         errors='ignore').readlines()
        # strip newlines
        line_list = [line.replace('\n','') for line in line_list]
        # send line-by-line as DM
        if id is not None:
            user = await self.bot.get_user_info(id)
        else:
            user = ctx.message.author
        c.botlog('{} is using inspect...'.format(user))
        for line in line_list:
            await self.bot.send_message(user, line)
            await asyncio.sleep(1)
        c.botlog('{}\'s inspection is done!'.format(user))

    @commands.command(pass_context=True)
    async def needping(self, ctx, image=None):
        """SOMEONE needs ping. Pls to give! User mention, attachment, link, or emoji."""
        imagetools.fishe(ctx, image)
        await self.bot.send_file(ctx.message.channel, root_dir+'\\img\\needping.png')
    
    @commands.command(pass_context=True,
                      aliases=['pingbadge'])
    async def verpingt(self, ctx, image=None):
        """SOMEONE needs ping. Pls to give! User mention, attachment, link, or emoji."""
        if image is None:
            try:
                ctx.message.attachments[0]['url']
            except IndexError:
                raise commands.MissingRequiredArgument('no')
        thumb = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/185/input-symbol-for-numbers_1f522.png'
        embed = c.crimbed('Choose a corner:', '1. Top left\n2. Top right\n3. Bottom left\n4. Bottom right', thumb)
        prompt = await self.bot.send_message(ctx.message.channel, embed=embed)
        # define check for position vote
        def check(msg):
            try:
                return ((0 < int(msg.content) <= 4) and msg.channel == ctx.message.channel and msg.author == ctx.message.author)
            except ValueError:
                return False
        # define default position, listen for user to specify different one
        position = '4'
        msg = await self.bot.wait_for_message(timeout=15, check=check)
        if msg is None:
            position = '4'
        else:
            position = msg.content
        # send to pingbadge
        imagetools.pingbadge(ctx, image, position)
        # delete prompt and vote, send image
        if msg is not None:
            await self.bot.delete_message(msg)
        await self.bot.delete_message(prompt)
        await self.bot.send_file(ctx.message.channel, root_dir+'\\img\\pingbadge.png')

def setup(bot):
    bot.add_cog(Image(bot))