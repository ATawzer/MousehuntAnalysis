import journalReading
import analysisFunctions
import pandas as pd

def mainMenu():

    print("===Main Menu===")
    print("1. Create Run Data")
    print("2. Single Parameter Analysis")
    print("3. Collective Stats DataFrame")
    print("4. Special Analysis Menu")
    print("5. Quit")
    return input("What would you like to do?\n")

def miscSubMenu():

    print("===Specialized Analysis Menu===")
    print("1. GWH17 Golem Analysis")
    print("2. King's Reward Analysis")
    print("3. Go back")
    return input('What would you like to do?\n')

def singleAnalysisMenu():

    print("===Single Parameter Analysis Menu===")
    print("1. Run-Based")
    print("2. Location-based")
    print("3. Cheese-based")
    print("4. Go back")
    return input("What would you like to do?\n")

def Main():

    user = 0
    allEntryDF = pd.read_csv("D:\Python Projects\Mousehunt Analytics\\runHunts.csv")
    allRunDF = allEntryDF[allEntryDF.isHunt == 1]
    miscEntryDF = allEntryDF[allEntryDF.isHunt == 0]

    while user != "5":

        # Reading in the data
        runsDF = analysisFunctions.buildRunCalcDF(allRunDF)
        user = mainMenu()

        # Build a new dataframe with updated run data
        if user == "1":
            # Make new data and then update its value
            journalReading.createData()
            allEntryDF = pd.read_csv("D:\Python Projects\Mousehunt Analytics\\runHunts.csv")
            allRunDF = allEntryDF[allEntryDF.isHunt == 1]
            miscEntryDF = allEntryDF[allEntryDF.isHunt == 0]

        # Single Parameter analysis
        elif user == "2":

            while user != "4":

                # Run-based
                user = singleAnalysisMenu()
                if user == "1":
                    user = input("What is the name you'd like to look at?\n")
                    if user =="help":
                        print(allRunDF.RunName.unique())
                        user = input("What is the name you'd like to look at?\n")
                    analysisFunctions.runSingleAnalysis(user, runsDF, allRunDF)

                # Location-based
                elif user == "2":
                    user = input("What is the location you'd like to look at?\n")
                    if user =="help":
                        print(allRunDF.Location.unique())
                        user = input("What is the name you'd like to look at?\n")
                    analysisFunctions.runLocationAnalysis(user, runsDF, allRunDF)

                # Cheese
                elif user == "3":
                    user = input("What is the cheese you'd like to look at?\n")
                    if user == "help":
                        print(allRunDF.Cheese.unique())
                        user = input("What is the name you'd like to look at?\n")
                    analysisFunctions.runCheeseAnalysis(user, runsDF, allRunDF)

                elif user == "4":
                    print("Returning to Main Menu . . .\n")

                else:
                    print('Invalid Entry . . .')

        # Collective Run Stats
        elif user =='3':
            analysisFunctions.allRunStats(runsDF)

        # Special Analysis Menu
        elif user == '4':

            user = miscSubMenu()
            while user != "2":
                if user == '1':
                    analysisFunctions.runGolemAnalysis(miscEntryDF)
                    user = miscSubMenu()
                elif user == "2":
                    print("Returning to Main Menu . . .")
                else:
                    print("Invalid Entry. . .")

        elif user == '5':
            print("Shutting down . . .")

        else:
            print("Invalid Entry . . .")


Main()


