from discord.ext import commands
import discord

client = commands.Bot(command_prefix=',')
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():


    print('Bot is ready.')


@client.event
async def on_message(ctx):
    guild = ctx.guild
    men_roles = ctx.role_mentions
    t = 0
    men_person = ctx.mentions
    c = ctx.content
    if ctx.channel.id == 792059735830036500:
        message_people = []
        for i in men_roles:


            real_role = guild.get_role(i.id)
            a = real_role.members
            if len(men_person) > 0:

                for o in men_person:
                    c = c.replace(f'<@&{real_role.id}>','').replace(f'@everyone','').replace(f'<@!{o.id}>','')

            else:
                c = c.replace(f'<@&{real_role.id}>','').replace(f'@everyone','')
        for k in men_roles:
            real_role = guild.get_role(k.id)
            s = real_role.members
            for m in s:
                message_people.append(m)
                t = t+1
        for y in men_person:
            message_people.append(y)
        for all in set(message_people):
            try:
                await all.send(c)
            except:
                print(f"Couldn't send message to {all.name}#{all.discriminator}.")
                t -=1
                if t == -1:
                    t = 0
        print(f'Message({c}) sent to {t} person ({len(set((message_people)))} expected) in {len(men_roles)} roles')



client.run("ODMyNjQyNDA2MjY0NDcxNTY0.YHmwqw.TUIcu5aGHfk5aHS5_HV6QtSc9A8")








