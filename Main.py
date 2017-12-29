import journalReading
import analysisFunctions
import pandas as pd

def mainMenu():

    print("===Main Menu===")
    print("1. Create Run Data")
    print("2. Single Run Analysis")
    print("3. Run Collective Run Stats")
    print("4. Run Location-based Analysis")
    print("5. Access Special Analysis Menu")
    print("6. Quit")
    return input("What would you like to do?\n")

def miscSubMenu():

    print("===Specialized Analysis Menu===")
    print("1. GWH17 Golem Analysis")
    print("2. King's Reward Analysis")
    print("3. Go Back")
    return input('What would you like to do?\n')

def Main():

    user = 0
    allEntryDF = pd.read_csv("D:\Python Projects\Mousehunt Analytics\\runHunts.csv")
    allRunDF = allEntryDF[allEntryDF.isHunt == 1]
    miscEntryDF = allEntryDF[allEntryDF.isHunt == 0]

    while user != "6":

        runsDF = analysisFunctions.buildRunCalcDF(allRunDF)
        user = mainMenu()

        if user == "1":
            # Make new data and then update its value
            journalReading.createData()
            allEntryDF = pd.read_csv("D:\Python Projects\Mousehunt Analytics\\runHunts.csv")
            allRunDF = allEntryDF[allEntryDF.isHunt == 1]
            miscEntryDF = allEntryDF[allEntryDF.isHunt == 0]
        elif user == "2":

            user = input("What is the name you'd like to look at? (help for options)\n")
            if user == "help":
                print(allRunDF.RunName.unique())
                user = input("What is the name you'd like to look at?\n")
                analysisFunctions.runSingleAnalysis(user, runsDF, allRunDF)
            else:
                analysisFunctions.runSingleAnalysis(user, runsDF, allRunDF)
        elif user == "3":
            print('DataFrame containing all run stats info: \n')
            analysisFunctions.allRunStats(runsDF)
        elif user =='4':
            user = input("What is the location you'd like to look at? \n")
            if user == 'help':
                print(allRunDF.Location.unique())
                user = input("What is the location you'd like to look at? \n")
                analysisFunctions.runLocationAnalysis(user, runsDF, allRunDF)
            else:
                analysisFunctions.runLocationAnalysis(user, runsDF, allRunDF)

        elif user == '5':
            user = miscSubMenu()
            if user == '1':
                analysisFunctions.runGolemAnalysis(miscEntryDF)
                user = miscSubMenu()
            elif user == '2':
                print("Coming Soon. . .")
                user = miscSubMenu()
            elif user == '3':
                user = mainMenu()
            else:
                print("Invalid Entry. . .")

        else:
            print("Invalid Entry . . .")


Main()


