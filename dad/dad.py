import discord
from redbot.core import commands
from redbot.core.config import Config
import os
import asyncio
import logging
import random
from random import choice
import re



class Noodledad(commands.Cog):
    """
    Dad?
    """
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=Noodledad
        )
    
    @commands.command(pass_context=True)
    async def venue(self, ctx):
    	"""Dad gives you a venue to grind"""
    	venues = ["Training Fields", "Woodland Path","Scorched Forest","Boneyard","Sandswept Delta","Silk-Strewn Wreckage","Blooming Grove", "Forgotten Cave", "Bamboo Falls", "Thunderhead Savanna", "Redrock Cove", "Waterway", "Arena", "Volcanic Vents", "Rainsong Jungle", "Boreal Wood", "Crystal Pools", "Harpy's Roost", "Ghostlight Ruins", "Mire", "Kelp Beds", "Golem Workshop", "Forbidden Portal"]
    	await ctx.send(random.choice(venues))

    @commands.command(pass_context=True)
    async def dadjoke(self, ctx):
        """Why didn't the find the Windsinger? Because he was FATHER away than she thought..."""
        dadjokes = ["What do you call a nocturne that is an acolyte or student? A noc-learn.", "What do you call a navigational float that does its job very well? A good buoy.", "What do you call a dragon that has anger management issues? A snapper!","What's a mummy's favorite kind of music? Wrap!","Have you been to the Dragonhome? I hear it's quite a-*stone*-ishing!", "Why'd the player stop grinding in the Mire? Because they got *swamped*.", "Why can't a ridgeback's nose be 12 inches long? Because then it would be a foot.", "Why do tundras have hairy coats? Fur protection", "I heard Windsinger took a job in Icewarden's library. It has its *prose* and *cons*.", "Did you hear the rumour about the butter caiman? No, wait, I shouldn't spread it.", "This hatchling refuses to take a nap. She is *resisting a rest*", "When the Arcanist cloned Windsinger, what were the clones called? Copypasta", "How did the vacationing out of flighter find Wind? They were *blown away*", "An acolight visited another flight on vacation... they were *de-lighted*", "What happens when Water crosses Fire territory? They will be mist", "Why couldn't the dragon get past the Training Fields? Because he *bumble*d", "Why'd everyone fall asleep at the veteran's dinner? Because it was *boran*", "Intern to Stormcatcher: Boss, boss, the interns are rebelling! \n Stormcatcher: Well, you're pretty re*volting* yourself.", "Why doesn't the Bone Fiend get mad? Because nothing gets under its skin", "Why does the Anomalous Skink win every trivia contest? Because *two heads are better than one*", "Did you about Nekomata Town? It's a *City of Two Tails*","Dragon to healer: I've broken my leg in several places. Healer to dragon: Well, don't go to those places!", "What do you call a group of spiney-whales playing instruments? An orca-stra!","Why did the croakers cross the road? They'd gone batty!", "How did the Octoflyer beat the Mammertee in a fight? Because it was *well-armed*", "Why couldn't the hatchling find the Sentinel? Because it was a mith.", "How did the psywurm know she'd reached Light territory? Because she was brilliant", "What do you get if you cross a leopard coralclimber with a steelhound? A terrified courier!", 'How did the hippy aardvark greet Gladekeeper? "Peace, vine"', "Why didn't the Silverbeast have any customers? Because he Overcharged.", "A Red and a Blue dragon mated at sea. The kids are marooned", "Did you hear about the ridgeback who went diving? He pulled a mussel", "What do you call a pile of floracats? A meowntain", "Why doesn't the moonbeam crayfish share? Because he's shellfish", "Somebody asks a tundra: Did you get a haircut? Tundra answer: No, I got them all cut", "Arcanite (post explosion): OMG ARCANIST ARE YOU ALL RIGHT \n Arcanist: NO I'M HALF LEFT", "What do you call a ridgeback with no body and no nose? Nobody knows!", "What do you call a dragon who's out of breath? A bad aim.", "Why did the blind ridgeback starve? Because he couldn't SEE FOOD!", "Why can't you hear a phthalo dragon go to the bathroom? Because the pee is silent.", "What do you call a really heavy tundra? A Tondra", "What do Snappers do when they're angry? They Snap a retort", "Why didn't the Dragon wear Marva's invisibility cloak to the ball? He couldn't see himself doing it.","What do you call a pebbly meatball? A snapper!", "Why do you never see mammertees hiding in trees? Because they're so good at it.", "The Abiding Boneyard is getting overcrowded - dragons must be dying to get in there.","What do you call a fake noodle? An impasta!", "What do you call a Spiral and a Skydancer in a hot tub? Chicken noodle soup!", "Why do Lightning Sprites look so angry? Because they're the Stormcatcher's entou-rage!", "What are Anomalous Nekomatas made of? Well, Arcane scientists say it's some kind of anomalous nekomatter.", "What is Swipp's favorite dessert? Swhipped cream!", "When Crim has a lot of clothes stacked up, Pinkerton sets up a Laundered Pile.", "The rewards Crim offers for some items are simply *crim*-inal, aren't they?", "They say Tundras are peaceful, but just get between two of them and it'll be really hairy.", "Be careful around dragons that drink blood. You don't want to invoke their vamp-*ire*", "What does the Gladekeeper say to support her children? She tells them to b-leaf!", "Kelp Beds? More like Welp Beds, am I right?", "The real joke are my parenting skills.", "How do you stop a Windie from doing something? You say: win*don't*!", "What do tired Windies do? Well, first of all, they take a *map!*", "Why don't Otherworldly Auras ever go trick-or-treating? Because they have no body to go with!", "Why does the Arcanist keep buying books even though he has thousands of them? He has no shelf control.", "The Arcanist got tired of watching the moon go around the planet for 24 hours so he decided to call it a day.", "Stormcatcher. What an attention hog, right? He hates when people steal his thunder.", "*Shockingly*, Stormcatcher's the only one ever aware of the state of *current* affairs."]
        await ctx.send(random.choice(dadjokes))

    @commands.command(pass_context=True)
    async def exalt(self, ctx, exaltee : str):
        """Off to the Cloudsong with ye!"""
        famther = ["dad", "Noodledad","@Noodledad#1251" "Windsinger", "Windpapa", "windad","windsinger","father","noodledad","Winddad","winddad","windpapa"]
        if exaltee in famther:
                await ctx.send("Hey, I thought you *wanted* me to be here! Kids nowadays...")
        elif exaltee not in famther:
            exline = ["*Plucks " + exaltee + " out of the air and puts back on the ground* Nope, go play around some more.", "Come on and slam, and welcome to MistJam!", "You must have gone through a lot of training, "+ exaltee + "! I really ad-*Mire* you for that.", "*tucks " + exaltee + " under a cloud* My child now", exaltee + " has joined the Noodle Search Party!", "Exalt Failure: Dad Not Found", "Wonderful! More kites in the sky!", "Ah, there you are! I just needed help with this jam jar."]
            await ctx.send(random.choice(exline))

    @commands.command()
    async def skya(self, ctx, name : str):
        """Skya needs her rest too! Dad is here to take care of us instead"""
        uvline = ["Remember to eat, sleep, stretch, drink some water and take your meds, " + name + "!", name + " :fork_and_knife::green_apple::zzz::muscle::pill::droplet::droplet::droplet:", "DRNKWTR, " + name + "!", "Have you taken care of yourself today, " + name + "?", name + " EAT SLEEP STRETCH MEDS HYDRATE"]
        await ctx.send(random.choice(uvline))

    @commands.command(pass_context=True)
    async def dad(self, ctx):
        """Dad says a thing if you poke him! ... Well, usually."""
        author = ctx.message.author
        dadsays = ["At least MY ears aren't tiny.", author.mention + ', my child!', 'Did someone call me?', '!? ' + author.mention + ", how did you find me!", '404 Dad Not Found', "TICK-TOCK ON THE CLOCK BUT THE PARTY DON'T STOP", "Isn't it bedtime for you yet?", "I can be a good dad too! Wait where did that egg go", "Voices on the wind...", "GET BACK TO PARTYING!", "Is that... Is that a corgnado?!", "Mom?", "Dad - more like rad!", "*pokes head down from the clouds* How are you kids doing? Oops, gotta run!", "Happy Mistral Jamboree! ... What do you mean, it's not March? It's always Mistjam!"]   
        await ctx.send(random.choice(dadsays))


async def setup(bot):
	await bot.add_cog(Noodledad(bot))
