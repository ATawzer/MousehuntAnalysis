import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def buildRunCalcDF(df):

    columns = ['RunName', 'Location', 'Cheese', 'totalHunts', 'totalAttractions', 'totalCatches', 'totalGold', 'totalPoints', 'totalSG', 'totalSB', 'totalSP',
               'mouseGold', 'lootGold', 'Profit', 'netPoints', 'profitPerHunt', 'mouseGoldPerHunt', 'lootGoldPerHunt', 'pointsPerHunt',
               'totalCost', 'mouseProfit']
    runs = df['RunName'].unique()
    locs = df['Location'].unique()
    cheeses = df['Cheese'].unique()
    runsdf = pd.DataFrame(index=[x for x in range(0, len(runs)+len(locs)+len(cheeses))], columns=columns)



    # General stuff
    for index, row in runsdf.iterrows():

        # First type, rundata
        if index < len(runs):
            rundf = df[df.RunName == runs[index]]

            row['RunName'] = runs[index]
            row['Location'] = 'Mixed'
            row['Cheese'] = 'Mixed'
            row['totalHunts'] = np.sum(rundf.isHunt)
            row['totalAttractions'] = len(rundf[rundf.isFTA != 1])
            row['totalCatches'] = len(rundf[rundf.isCaught == 1])
            row['totalGold'] = np.sum([rundf.Gold, rundf.LootGold])
            row['totalPoints'] = np.sum(rundf.Points)
            row['totalSG'] = np.sum(rundf.SG)
            row['totalSB'] = np.sum(rundf.SB)
            row['totalSP'] = np.sum(rundf.SP)
            row['totalCost'] = np.sum(rundf.Cost) - (np.sum(rundf.keptCheese)*np.min(rundf.Cost)) + row.totalSG + (row.totalSB*np.min(rundf.Cost))
            row['mouseGold'] = np.sum(rundf.Gold)
            row['lootGold'] = np.sum(rundf.LootGold)
            row['Profit'] = row['totalGold'] - row.totalCost
            row['mouseProfit'] = row['mouseGold'] - row.totalCost
            row['netPoints'] = row['totalPoints'] - row['totalSP']
            row['profitPerHunt'] = round(row['Profit']/row['totalHunts'], 2)
            row['pointsPerHunt'] = round(row['netPoints'] / row['totalHunts'], 2)
            row['mouseGoldPerHunt'] = round(row['mouseGold'] / row['totalHunts'], 2)
            row['lootGoldPerHunt'] = round(row['lootGold'] / row['totalHunts'], 2)

        # Second type, Location Data
        elif index >= len(runs) and index < len(runs)+len(locs):
            newindex = index-len(runs)
            rundf = df[df.Location == locs[newindex]]

            row['RunName'] = 'Mixed'
            row['Location'] = locs[newindex]
            row['Cheese'] = 'Mixed'
            row['totalHunts'] = len(rundf)
            row['totalAttractions'] = len(rundf[rundf.isFTA != 1])
            row['totalCatches'] = len(rundf[rundf.isCaught == 1])
            row['totalGold'] = np.sum([rundf.Gold, rundf.LootGold])
            row['totalPoints'] = np.sum(rundf.Points)
            row['totalSG'] = np.sum(rundf.SG)
            row['totalSB'] = np.sum(rundf.SB)
            row['totalSP'] = np.sum(rundf.SP)
            row['totalCost'] = np.sum(rundf.Cost) - (np.sum(rundf.keptCheese) * np.min(rundf.Cost)) + row.totalSG + (
                row.totalSB * np.min(rundf.Cost))
            row['mouseGold'] = np.sum(rundf.Gold)
            row['lootGold'] = np.sum(rundf.LootGold)
            row['Profit'] = row['totalGold'] - row.totalCost
            row['mouseProfit'] = row['mouseGold'] - row.totalCost
            row['netPoints'] = row['totalPoints'] - row['totalSP']
            row['profitPerHunt'] = round(row['Profit'] / row['totalHunts'], 2)
            row['pointsPerHunt'] = round(row['netPoints'] / row['totalHunts'], 2)
            row['mouseGoldPerHunt'] = round(row['mouseGold'] / row['totalHunts'], 2)
            row['lootGoldPerHunt'] = round(row['lootGold'] / row['totalHunts'], 2)

        elif index >= len(runs)+len(locs) and index < len(runs)+len(locs)+len(cheeses):
            newindex = index-len(runs)-len(locs)
            rundf = df[df.Cheese == cheeses[newindex]]

            row['RunName'] = 'Mixed'
            row['Location'] = 'Mixed'
            row['Cheese'] = cheeses[newindex]
            row['totalHunts'] = len(rundf)
            row['totalAttractions'] = len(rundf[rundf.isFTA != 1])
            row['totalCatches'] = len(rundf[rundf.isCaught == 1])
            row['totalGold'] = np.sum([rundf.Gold, rundf.LootGold])
            row['totalPoints'] = np.sum(rundf.Points)
            row['totalSG'] = np.sum(rundf.SG)
            row['totalSB'] = np.sum(rundf.SB)
            row['totalSP'] = np.sum(rundf.SP)
            row['totalCost'] = np.sum(rundf.Cost) - (np.sum(rundf.keptCheese) * np.min(rundf.Cost)) + row.totalSG + (
                row.totalSB * np.min(rundf.Cost))
            row['mouseGold'] = np.sum(rundf.Gold)
            row['lootGold'] = np.sum(rundf.LootGold)
            row['Profit'] = row['totalGold'] - row.totalCost
            row['mouseProfit'] = row['mouseGold'] - row.totalCost
            row['netPoints'] = row['totalPoints'] - row['totalSP']
            row['profitPerHunt'] = round(row['Profit'] / row['totalHunts'], 2)
            row['pointsPerHunt'] = round(row['netPoints'] / row['totalHunts'], 2)
            row['mouseGoldPerHunt'] = round(row['mouseGold'] / row['totalHunts'], 2)
            row['lootGoldPerHunt'] = round(row['lootGold'] / row['totalHunts'], 2)


    return runsdf

def runSingleAnalysis(name, df, dfall):

    # "$" + str("{:,}"

    df = df[df.RunName == name]
    GeneralAnalysis(df)
    singleMouseAnalysis(dfall[dfall.RunName == name])
    singleLootAnalysis(dfall[dfall.RunName == name])

def runLocationAnalysis(loc, df, dfall):

    df = df[df.Location == loc]
    dfall = dfall[dfall.Location == loc]
    GeneralAnalysis(df)
    singleMouseAnalysis(dfall)
    singleLootAnalysis(dfall)

def runCheeseAnalysis(che, df, dfall):

    df = df[df.Cheese == che]
    dfall = dfall[dfall.Cheese == che]
    GeneralAnalysis(df)
    singleMouseAnalysis(dfall)
    singleLootAnalysis(dfall)

def GeneralAnalysis(df):

    print("=====Run Stats=====\n")
    print("===General Information===")
    print("Total Hunts: " + "{:,.2f}".format(np.sum(df.totalHunts)) +
          " | Total Attractions: " + "{:,.2f}".format(np.sum(df.totalAttractions)) +
          " | Total Catches: " + "{:,.2f}".format(np.sum(df.totalCatches)))
    print("Total Stolen Bait: " + "{:,.2f}".format(np.sum(df.totalSB)) +
          " | Total Stolen Gold: $" + "{:,.2f}".format(np.sum(df.totalSG)) +
          " | Total Stolen Points: " + "{:,.2f}".format(np.sum(df.totalSP)))
    print('Global Catch Rate: ' + "{:,.2f}".format(round(np.sum(df.totalCatches)/np.sum(df.totalAttractions)*100, 2)) +
          "% | Global Attraction Rate: " + "{:,.2f}".format(round(np.sum(df.totalAttractions)/np.sum(df.totalHunts)*100, 2)) + '%\n')

    print("===Wealth Information===")
    print("Total Gold: $" + "{:,.2f}".format(np.sum(df.totalGold)) +
          " | Total Profit: $" + "{:,.2f}".format(np.sum(df.Profit)) +
          " | Total Cost: $" + "{:,.2f}".format(np.sum(df.totalCost)))
    print("Mouse Gold: $" + "{:,.2f}".format(np.sum(df.mouseGold)) +
          " | Mouse Profit: $" + "{:,.2f}".format(np.sum(df.mouseProfit)) +
          " | Loot Gold: $" + "{:,.2f}".format(np.sum(df.lootGold)))
    print("Profit per Hunt: $" + "{:,.2f}".format(np.mean(df.profitPerHunt)) +
          " | Mouse Gold per Hunt: $" + "{:,.2f}".format(np.mean(df.mouseGoldPerHunt)) +
          " | Loot Gold per Hunt: $" + "{:,.2f}".format(np.mean(df.lootGoldPerHunt)) + '\n')

    print("===Point Information===")
    print("Total Points: " + "{:,.2f}".format(np.mean(df.totalPoints)) +
          " | Net Points: " + "{:,.2f}".format(np.mean(df.netPoints)) +
          " | Points per Hunt: " + "{:,.2f}".format(np.mean(df.pointsPerHunt)))



    input('\n')

def singleMouseAnalysis(huntsdf):

    print("=====Mouse Information=====")
    print('')
    mice = huntsdf.Mouse.unique(); mice = np.sort(mice);
    loot = huntsdf.columns; loot = loot[27:-1]; loot = np.sort(loot)

    for mouse in mice:
        if mouse != 'FTA':
            subdf = huntsdf[huntsdf.Mouse == mouse]
            print("===" + mouse + "===")
            print('Attractions: ' + str(len(subdf) - np.sum(subdf.isFTA)) + " | Catches: " + str(np.sum(subdf.isCaught)))
            print('Population Estimation: ' + str(round(100*(len(subdf) - np.sum(subdf.isFTA))/len(huntsdf), 2)) +
            '% | Catch Rate: ' + str(round(100*np.sum(subdf.isCaught)/(len(subdf) - np.sum(subdf.isFTA)), 2)) + '%')

            print("\nMouse Loot: ")
            for item in loot:
                subdf = subdf[subdf.isCaught == 1]
                if np.sum(subdf[item]) > 0:
                    print(item + ': ' + str(np.sum(subdf[item])) + " | Drop Rate: " +
                          str(round(np.sum(subdf[item])/np.sum(subdf.isCaught), 2)) +' per Catch' +
                          " | Drop Range: " + str(np.min(subdf[item])) + " to " + str(np.max(subdf[item])))

            print('')



    input('\n')

def singleLootAnalysis(huntsdf):

    print("=====Global Loot Information=====")
    loot = huntsdf.columns; loot = loot[27:-1]; loot = np.sort(loot)
    for item in loot:
        if np.sum(huntsdf[item]) > 0:
            print(item + ": " + str(np.sum(huntsdf[item])) +
                  " | Global Drop Rate: " + str(round(np.sum(huntsdf[item])/len(huntsdf), 2)) + " per Hunt")

    print("")
    print("Total Loot Value: $" + str("{:,}".format(np.sum(huntsdf['LootGold']))))

    input('\n')

def allRunStats(df):

    cols = df.columns
    print(df)

    for index, row in df.iterrows():
        for col in cols:
            if col != "RunName" and col != "Location" and col != "Cheese":
                row[col] = "{:,.2f}".format(row[col])

    print(df)

def createGolemDF(df):

    print("Collecting Golem entry information. . .")
    golemDict = {'Level': [], 'Location': [], 'LootDes': []}

    # First, we want just the Festive Comet Entries
    for index, row in df.iterrows():
        entry = row['Description']
        if 'My golem returned' in entry:

            # First up
            entry = entry.split()
            i1 = entry.index('returned')
            i2 = entry.index('with')
            loc = " ".join(entry[i1 + 3:i2])
            if loc == '':
                loc = 'Zokor'

            golemDict['Location'].append(loc)
            golemDict['Level'].append(entry[i2+1])
            golemDict['LootDes'].append(" ".join(entry[i2+1:]))

    gdf = pd.DataFrame(golemDict)
    lootNames = []

    for index, row in gdf.iterrows():
        lootlist = row.LootDes.split(',')
        for item in lootlist:

            loot = item.split()
            quant = loot[0]
            name = " ".join(loot[1:])
            if name[-1] == 's':
                name = name[:-1]

            if name not in lootNames:
                lootNames.append(name)

    lootNames.append('LootGold')
    lootNames.append('eGold')

    lootdf = pd.DataFrame(index=[x for x in range(0, len(gdf))], columns=lootNames)
    for item in lootNames:
        lootdf[item] = [0 for x in range(0, len(lootdf))]


    for index, row in lootdf.iterrows():
        lootlist = np.array(gdf.LootDes)[index].split(',')
        for item in lootlist:

            loot = item.split()
            quant = loot[0]
            name = " ".join(loot[1:])
            if name[-1:] == 's':
                name = name[:-1]

            row[name] = quant

    marketdf = pd.read_csv('marketPlace.csv')
    for index, row in marketdf.iterrows():
        if row['ItemName'] in lootNames:
            lootdf['LootGold'] = lootdf['LootGold'] + lootdf[row['ItemName']]*row['Price']
            lootdf['eGold'] = lootdf['eGold'] + lootdf[row['ItemName']] * row['eValue']

    return pd.concat([gdf, lootdf], axis=1)

def runGolemAnalysis(entrydf):

    golemdf = createGolemDF(entrydf)
    print("=====Golem Analysis=====\n")

    # Now let's break it down
    locs = golemdf.Location.unique()

    for loc in locs:

        print("===" + loc +"===\n")
        gdf = golemdf[golemdf.Location == loc]
        levels = gdf.Level.unique()
        levels = np.sort(levels)
        for level in levels:
            newdf = gdf[gdf.Level == level]
            print("Golem Level: " + str(level) + " | Number of Golems: " + str(len(newdf)))
            print("Tangible Value: $" + "{:,.2f}".format(np.sum(newdf.LootGold)) +
                  " | Value per Golem: $" +"{:,.2f}".format(round(np.sum(newdf.LootGold)/len(newdf), 2)))
            print("Effective Value: $" + "{:,.2f}".format(np.sum(newdf.eGold)) +
                  " | Value per Golem: $" + "{:,.2f}".format(round(np.sum(newdf.eGold) / len(newdf), 2)))
            print("")

            print("Loot Breakdown: ")
            loot = newdf.columns; loot = loot[3:-2]; loot = np.sort(loot)
            for item in loot:
                if np.sum(newdf[item]) > 0:
                    print(item + ": " + str(np.sum(newdf[item])) + " | Per Golem: " +
                          str(round(np.sum(newdf[item])/len(newdf), 2)))


            # print("")

            input("\n")

    print("===Global Stats===")
    print("Number of Golems: " + str(len(golemdf)))
    print("Tangible Value: $" + "{:,.2f}".format(np.sum(golemdf.LootGold)) +
          " | Value per Golem: $" + "{:,.2f}".format(round(np.sum(golemdf.LootGold) / len(golemdf), 2)))
    print("Effective Value: $" + "{:,.2f}".format(np.sum(golemdf.eGold)) +
          " | Value per Golem: $" + "{:,.2f}".format(round(np.sum(golemdf.eGold) / len(golemdf), 2)))
    print("")







