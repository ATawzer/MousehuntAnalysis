import pandas as pd

def readFile(filename):

    #based on run information we will grab the hunts
    fname = f"Runs/{filename}"
    f = open(fname, "r")
    flines = []

    #creating and array with all of the lines in it to send back to Main
    for line in f:
        flines.append(line)

    #we're done here
    f.close()
    return flines

def writeRunHuntsFile(dirname, huntsArr):

    runDict = {'#': [], 'isHunt':[], 'Description':[], 'Time': [], 'Location': [], 'isHorn': [], 'isSolo': [], 'Trap': [], 'Base': [], 'Cheese': [],
               'Charm': [], 'LGS': [], 'Cost': [], 'isFTA': [], 'keptCheese':[], 'isCaught': [], 'Mouse': [], 'Gold': [], 'Points': [], 'Size': [],
               'Loot': [], 'SG': [], 'SP': [], 'SB': []}

    rundf = pd.DataFrame(index=[x for x in range(0, len(huntsArr))], columns=runDict.keys())
    for i in range (0, len(huntsArr)):
        rundf.loc[i] = huntsArr[i]


    # Small little cleaning process
    print("Converting to DataFrame. . .")
    for index, row in rundf.iterrows():
        row['Gold'] = int(row['Gold'].replace(",", ""))
        row['Points'] = int(row['Points'].replace(",", ""))
        row['SG'] = int(row['SG'].replace(",", ""))
        row['SP'] = int(row['SP'].replace(",", ""))
        row['SB'] = int(row['SB'].replace(",", ""))
        row['Size'] = int(row['Size'].replace(" oz.", ""))


        row['isHunt'] = 1 if row['isHunt'] == 'Hunt' else 0
        row['isSolo'] = 1 if row['isSolo'] == "Solo" else 0
        row['isFTA'] = 0 if row['isFTA'] == "Attracted" else 1
        row['isHorn'] = 1 if row['isHorn'] == "Horn" else 0
        row['isCaught'] = 1 if row['isCaught'] == "Caught" else 0
        row['LGS'] = 1 if row['LGS'] == "GoldenShield:True" else 0
        row['keptCheese'] = 1 if row['keptCheese'] == 'Fresh' else 0

    rundf['RunName'] = dirname[:-4]
    return rundf