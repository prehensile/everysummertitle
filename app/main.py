#!/usr/bin/env python

from botkit import botkit
import generator

# instantiate botkit
bot = botkit.BotKit( "astonished" )

# instantiate asciibot
astonished = generator.PerpetualAstonishment()

# go!
bot.run( astonished )
