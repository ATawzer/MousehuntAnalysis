import fileFunction
import pandas as pd
import os

def isValidHunt(hunt):

    # Keywords found in every hunt, we check and see if we have them
    if ("went" in hunt):
        return True
    elif ("sounded" in hunt):
        return True
    elif ("checked" in hunt):
        return True
    elif ("check" in hunt):
        return True
    else:
        return False

def howMuchLoot(loot):
        lootList = loot.split()
        return int(lootList[0])

def convLootName(lootn):

    # Let's see if it has more than one
    if (howMuchLoot(lootn) > 1):

        # Let's first check for s's
        if (lootn[-1] == "s"):
            # The name start will change based on how many
            if (howMuchLoot(lootn) >= 1000):
                return (lootn[5:-1])
            elif (howMuchLoot(lootn) >= 100):
                return (lootn[4:-1])
            elif (howMuchLoot(lootn) >= 10):
                return (lootn[3:-1])
            elif (howMuchLoot(lootn) >= 1):
                return (lootn[2:-1])

        # Some special cases are multiple without s's, returned below
        else:
            if (howMuchLoot(lootn) >= 1000):
                return (lootn[5:])
            elif (howMuchLoot(lootn) >= 100):
                return (lootn[4:])
            elif (howMuchLoot(lootn) >= 10):
                return (lootn[3:])
            elif (howMuchLoot(lootn) >= 1):
                return (lootn[2:])
    else:
        return (lootn[2:])

def addRunInfo(lines):

    runArr = []
    for i in range(0, 6):
        temline = lines[i].split()
        tepline = ""
        for j in range(1, len(temline)):
            tepline = tepline + temline[j]
        runArr.append(tepline)

    return runArr

def addTime(huntLine):

    # When it's a vlid hunt, we just add the first two entries, time and pm/am
    return (huntLine[0] + huntLine[1])

def addLocation(huntList):

    # Let's find the indices of our location, in between '-' and 'I'
    dInd = huntList.index("-")
    iInd = huntList.index("I")

    # Let's append the location name
    return (" ".join(huntList[dInd + 1:iInd]))

def addHuntType(huntList):

    # First let's check if it was a horn or trap check
    if ("checked" in huntList[:10]):
        return ("Check")
    else:
        return ("Horn")

def addHunterType(huntList):

    # See if it was solo or not
    if ("went" in huntList):
        return ("Noso")
    else:
        return ("Solo")

def isFTA(huntLine):

    if ("failed to attract" in huntLine):
        return True
    else:
        return False

def isStale(huntLine):

    if ("I replaced" in huntLine):
        return True
    else:
        return False

def isCaught(huntLine):

    # Keywords for a catch
    if ("was successful" in huntLine or "I had caught a" in huntLine):
        return True
    else:
        return False

def addFTAInfo(huntLine):

    # Create a temp array we will store the rest of the entries in
    tempEntry = []

    # Putting in our information for FTA
    tempEntry.append("FTA")

    # Only other question is whether is was stale or fresh
    if isStale(huntLine):
        tempEntry.append("Stale")
    else:
        tempEntry.append("Fresh")

    # Since we don't have a mouse, the rest of the information is super easy, we will put it below
    tempEntry.append("FTA")
    tempEntry.append("FTA")
    tempEntry.append("0")
    tempEntry.append("0")
    tempEntry.append("0")
    tempEntry.append("None")
    tempEntry.append("0")
    tempEntry.append("0")
    tempEntry.append("0")

    return tempEntry

def addAttractionInfo():

    # Easy, Given paramters of a successful attraction
    return ["Attracted", "Eaten"]

def addCaughtMouseInfo(huntList):

    # The Array we will use to track our stuff
    tempEntry = ["Caught"]

    # Given of catching a mouse

    # These are important indices to track where the mouse name is in the caught situation
    spotm = huntList.index("worth")
    spotimd = huntList.index("oz.")

    if "weighing" in huntList:
        tempEntry.append('Stuck Snowball Mouse')
    else:
        tempEntry.append(getMouseName(huntList, spotm, spotimd))

    tempEntry.extend(getMouseInfo(huntList))

    # finding out the size
    tempEntry.append(addSizeInfo(huntList, spotimd))

    # Doing the necessary loot analysis
    tempEntry.append(addLootInfo(huntList))

    # Finishing our entry with the rest of the given info from a hunt, 0's for stuff like stolen goods
    tempEntry.extend(["0", "0", "0"])

    return tempEntry

def getMouseName(tempHuntList, ind2, ind1):

    # Our mouse name is trapped in those indices, we have our mouse name
    mouseName = " ".join(tempHuntList[ind1+1:ind2])
    return mouseName

def getMouseInfo(tempHuntList):

    # Find the info
    goldspot = int(tempHuntList.index("gold."))-1
    pointspot = int(tempHuntList.index("points"))-1

    # Return those indexed locations
    return [tempHuntList[goldspot], tempHuntList[pointspot]]

def addSizeInfo(tempHuntList, ind):

    if ("lb." in tempHuntList):
        return str((int(tempHuntList[ind - 3]) * 16) + int(tempHuntList[ind - 1])) + " oz."
    else:
        return str(tempHuntList[ind - 1]) + " oz."

def addStolenInfo(tempHuntList, tempHuntLine):

    tempTempEntry = []
    if ("Additionally," in tempHuntLine):
        if ("fiend pillaged" in tempHuntLine):
            index = tempHuntList.index("pillaged")
            tempTempEntry.append(str(tempHuntList[index + 1]))
            tempTempEntry.append("0")
            tempTempEntry.append("0")
        elif ("crippled my courage" in tempHuntLine):
            index = tempHuntList.index("courage,")
            tempTempEntry.append("0")
            tempTempEntry.append(str(tempHuntList[index + 4]))
            tempTempEntry.append("0")

        # eventually will be for bait loss, don't know wording
        elif ("the crafty mouse managed" in tempHuntLine):
            index = tempHuntList.index("additional")
            tempTempEntry.append("0")
            tempTempEntry.append("0")
            tempTempEntry.append(str(tempHuntList[index + 1]))
    else:
        tempTempEntry.append("0")
        tempTempEntry.append("0")
        tempTempEntry.append("0")

    return tempTempEntry

def getEndLoot(huntList):

    # We need to determine where the loot information stops
    # Not many locations do this, but some actively update your hunt, one of which is Zokor

    # If we're in Zokor
    if ("Zokor" in huntList):

        # One of two things will follow
        if ("With" in huntList):
            return (huntList.index("With"))
        elif ("lost" in huntList):
            return huntList.index("lost")-1
        else:
            return len(huntList)
    elif 'Labyrinth' in huntList:
        if 'Dead' in huntList:
            return huntList.index('Dead')-1
        elif 'Compass' in huntList:
            return huntList.index('Compass')-2
    else:
        return len(huntList)

def addLootInfo(tempHuntList):


    # Let's say we have some loot
    if ("loot:" in tempHuntList):

        # This is the last part of our entry, everything after this is going to be loot
        startLI = int(tempHuntList.index("loot:"))

        # Let's first store our loot as an array of all of the loot dropped
        newLoot = tempHuntList[startLI + 1:getEndLoot(tempHuntList)]

        # Keeping track of our loot entries
        theLoot = []

        # Let's check and see if we have more than one
        if ("and" in newLoot):
            # We've got atleast two entries, let's split it into everything before and after 'and'
            andLI = int(newLoot.index("and"))
            afAnd = newLoot[andLI + 1:]

            # Let's do everything before and, cycling through each value we will check for commas and add loot
            # to our list. Counter tracks how many pieces of loot we have
            counter = 0
            for kk in range(0, andLI):
                # We have a comma, that is the end of one piece of loot
                if ("," in newLoot[kk]):
                    lootEntry = " ".join(newLoot[counter:kk + 1])
                    theLoot.append(lootEntry[:-1])

                    # move our index of last loot entry finishing point
                    counter = kk + 1
                if (kk == andLI - 1):
                    # This is our last entry of loot, let's stop cycling
                    lootEntry = " ".join(newLoot[counter:kk + 1])
                    theLoot.append(lootEntry)

                else:
                    continue

            # Alright, everything after and is easy
            theLoot.append(" ".join(afAnd))

        # Or we only have one
        else:
            theLoot.append(" ".join(newLoot))

        # Finally, let's add the loot, with a delimiter, into our tline
        return ("**".join(theLoot))

    # If not, no issue here, let's say we don't
    return "None"

def addMissedMouseInfo(huntList, huntLine):

    tempEntry = ["Missed"]

    # Grab our valuable indices
    if ("appeared" in huntList):
        spotimd = huntList.index("appeared") + 1
    else:
        spotimd = huntList.index("fruitless.") + 1

    if ("ate" in huntList):
        spotm = huntList.index("ate")
    else:
        spotm = huntList.index("had")

    # Put in our info about the mouse, we will say it is worth nothing since we did not catch it
    tempEntry.append(getMouseName(huntList, spotm, spotimd))
    tempEntry.extend(["0", "0"])


    # Givens of a miss, no size or loot
    tempEntry.extend(["0", "None"])

    # Finding if something was stolen
    tempEntry.extend(addStolenInfo(huntList, huntLine))

    return tempEntry

def processJournalEntries(hunts, tra, bas, cha, che, lg, hid, filename):

    # Opening up our text to write on
    print("Currently Processing: " + filename)

    # These are variables to keep track of our hunts and info
    huntCount = 0
    journalEntries = []

    '''runDict = {'#': [], 'Time': [], 'Location': [], 'Type': [], 'isSolo': [], 'Trap': [], 'Base': [], 'Cheese': [],
               'Charm': [], 'Cost': [], 'isFTA': [], 'isCaught': [], 'Mouse': [], 'Gold': [], 'Points': [], 'Size': [],
               'Loot': [], 'SG': [], 'SP': [], 'SB': []}'''


    # We are going to cycle through our new hunts/entries in the condensed lines
    # All we are really doing here is taking our condensed line hunts and making it a more easily
    # able to process document where we know the entry number for each piece of information we want
    for i in range (0, len(hunts)):

        entryLine =[]
        entry = hunts[i].split()

        # Call a simple function that's make sure we actually have a valid hunt
        if (isValidHunt(entry)):

            huntCount += 1
            # Self-Explanatory from here, adding information common to all hunts
            entryLine.append(str(huntCount))
            entryLine.append("Hunt")
            entryLine.append(hunts[i])
            entryLine.append(addTime(entry))
            entryLine.append(addLocation(entry))
            entryLine.append(addHuntType(entry))
            entryLine.append(addHunterType(entry))
            entryLine.append(tra)
            entryLine.append(bas)
            entryLine.append(cha)
            entryLine.append(che)
            entryLine.append(str(lg))
            entryLine.append(hid)

            '''runDict['#'].append(str(huntCount))
            runDict['Time'].append(addTime(entry))
            runDict['Location'].append(addLocation(entry))
            runDict['Type'].append(addHuntType(entry))
            runDict['isSolo'].append(addHunterType(entry))
            runDict['Trap'].append(tra)
            runDict['Base'].append(bas)
            runDict['Charm'].append(cha)
            runDict['Cheese'].append(che)
            runDict['Cost'].append(hid)'''


            # Now we have conditional information
            # First Question, did we even attract a mouse?
            # Let's start by asking if we failed to attract one, that's the easier case
            if (isFTA(hunts[i])):
                entryLine.extend(addFTAInfo(hunts[i]))

            # We didn't fail to attract, therefore we did indeed attract a mouse. Let's move forward accordingly
            else:

                # Simply just adds attraction info, nothing special at the moment
                entryLine.extend(addAttractionInfo())

                # Let's see if we actually got a mouse, though
                if (isCaught(hunts[i])):

                    # Sweet and simple, just call this function, it'll take care of the mess it is to extract mouse info
                    if "Stuck Snowball Mouse" in hunts[i]:
                        entry[entry.index('oz.!')] = 'oz.'
                        entryLine.extend(addCaughtMouseInfo(entry))
                    else:
                        entryLine.extend(addCaughtMouseInfo(entry))

                # We didn't get a mouse, let's fill in the necessary information for that
                else:
                    entryLine.extend(addMissedMouseInfo(entry, hunts[i]))





        else:

            entryLine.append('0')
            entryLine.append('noHunt')
            entryLine.append(hunts[i])
            entryLine.extend(['0' for x in range(0, 21)])

        journalEntries.append(entryLine)

    # Real quick, let's just reverse the order of our numberings
    for i in range (0, len(journalEntries)):
        journalEntries[i][0] = huntCount - int(journalEntries[i][0])
        journalEntries[i][0] = str(journalEntries[i][0])

    return journalEntries

def makeEntryList(lines):

   # Important stuff that allows us to break apart each lines and hunt
    newStarts = []
    newEntries = []

    # Now we look at all of the rest of the lines
    for i in range (6, len(lines)):
        line = lines[i].split()

        #create array for days of week
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Eliminate all of the dud lines
        if (len(lines[i]) > 1):
            # We find the beginning of a hunt using the time stamp at the first entry for a time
            # First we check and see if it is a time or a day
            if (line[0] in days):
                colon = line[1]
            else:
                colon = line[0]
            # Now we know its the beginning of an entry and we add it to the start
            if (len(colon) > 2):
                if (colon[1] == ":" or colon[2] == ":"):

                    #We are keeping track of which lines have new starts on them
                    newStarts.append(i)

    #log total hunts
    newStarts.append(len(lines))

   #Now we go through our starts
    for j in range (0, len(newStarts)-1):
        # Setup variable
        newline = ""

        #Now we are going to look in between each line we logged as being a new start
        for k in range (newStarts[j], newStarts[j+1]):

            #Condense the lines, get rid of new line character
            lines[k].replace('\n', '')
            newline = newline + lines[k]
        #Now we have on big line that will serve as our hunt rather than a confusing multi-line thing
        newEntries.append(newline)

    # Now we are ready to run some analysis using this array of useful lines
    return newEntries

def doJournalProcessing(file):

    # Grab our information from the logs
    entries = fileFunction.readFile(file)
    runBaseInfo = addRunInfo(entries)

    # print("Thank you! We will now process the entries with the information provided. . . \n")

    # We're going to do two sets of 'cleaning' we will call it. First we clean up our multi-line mess into a single line mess
    entries = makeEntryList(entries)

    # Then we take our new single line mess and  extract all of our hunts into an array of usable hunt arrays
    entries = processJournalEntries(entries, runBaseInfo[0], runBaseInfo[1], runBaseInfo[3],
                                                   runBaseInfo[2], runBaseInfo[4], runBaseInfo[5], file)

    # And now, we write it to our file, runHunts.txt, as an easy to understand, uniquely separated, set of hunt information
    return (fileFunction.writeRunHuntsFile(file, entries))

def createData():

    runNames = []
    dfArray = []

    runNames.extend(os.listdir("Runs/"))

    for i in range(0, len(runNames)):
        dfArray.append(doJournalProcessing(runNames[i]))

    # Create our master dataFrame to print out

    NewDf = pd.DataFrame(index=[], columns=list(dfArray[0].columns.values))
    for df in dfArray:
        NewDf = pd.concat([NewDf, df], axis=0)

    print("All entries have been processed!")

    NewDf.reset_index(inplace=True)
    NewDf = cleanLoot(NewDf)

    print("New Data has been succesfully created and stored.")
    NewDf.to_csv("runHunts.csv")

def cleanLoot(df):


    print("Converting Loot Information. . .")
    loot = df['Loot']
    lootNames = []

    for i in range(0, len(loot)):
        if loot[i] != 'None':
            info = loot[i].split("**")
            for j in range (0, len(info)):

                # Grabbing loot
                indLoot = info[j].split()
                name = " ".join(indLoot[1:])

                # remove s
                if name[-1:] == 's':
                    name = name[:-1]

                # See if it has been logged
                if name not in lootNames:
                    lootNames.append(name)
                else:
                    continue
        else:
            continue
    lootNames.append('LootGold')

    # So now we need to create a new dataframe where we will stick on the loot info
    lootdf = pd.DataFrame(0, index=[x for x in range(0, len(loot))], columns=lootNames)
    marketdf = pd.read_csv('marketPlace.csv')

    for index, row in lootdf.iterrows():

        if loot[index] == 'None':
            row[lootNames] = 0
        else:
            info = loot[index].split("**")
            for j in range(0, len(info)):

                # Grabbing loot
                indLoot = info[j].split()
                name = " ".join(indLoot[1:])

                # remove s
                if name[-1:] == 's':
                    name = name[:-1]
                elif name[-3:] == 'ves':
                    name = name[:-3] + 'f'

                row[name] = indLoot[0] if len(indLoot) > 0 else 'Unknown'



    # Now we update value of this
    print("Updating Loot Value. . .")
    for index, row in marketdf.iterrows():
        if row['ItemName'] in lootNames:
            lootdf['LootGold'] =  lootdf['LootGold'] + lootdf[row['ItemName']]*row['Price']



    return pd.concat([df, lootdf], axis=1)
