#!/usr/bin/env python
# -*- coding: utf-8 -*-

# itunes.py
# irssi now playing script for iTunes
# v 0.1, 19.08.2013
#

import commands
import string

def progressBar(percent):
    progBar = "[]"
    min = 0
    max = 10
    width = 20
    amount = 0
    percent = int(percent)

    allFull = width - 2
    numHashes = (percent / 100.0) * allFull
    numHashes = int(round(numHashes))
    progBar = "[" + '='*numHashes + ' '*(allFull-numHashes) + "]"
    percentPlace = (len(progBar) / 2) - len(str(percent)) 
    percentString = str(percent) + "%"
    progBar = progBar[0:percentPlace] + percentString + progBar[percentPlace+len(percentString):]
    return str(progBar)

def mpcnp():
    result = commands.getoutput("osascript -e 'tell app \"itunes\" to {artist, name, album, duration} of current track & {player position}'").split(",")

    if len(result) == 1:
        np = 'Is iTunes running?'
    else:
        artist = result[0].lstrip()
        track = result[1].lstrip()
        album = result[2].lstrip()
        time = result[3]
        current_time = result[4]

        percent = (float(current_time)/float(time))*100

        np = 'np: '+artist+' - '+track+' ~ ('+album+') @ '+progressBar(percent)


    print(np)




try:
    mpcnp()
except:
    print("Is iTunes running?")

