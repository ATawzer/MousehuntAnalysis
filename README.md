# MousehuntAnalysis

This console-based program will analyze runs from the online game Mousehunt and provide wealth, point and special location insight using useful statistical measures. The program is menu-based allowing for flexible and dynamic analysis that is user friendly for any run or location added.

# Main Menu
1. Create Run Data – will read in all stored runs and update their values in the runHunts.csv file allowing the program to update its analysis from any newly stored hunts
2. Single Parameter Analysis – breaks down analysis by either a run-name, a location name or a cheese name. Each option allows the user to type help to see all of the available analysis combination options
3. Collective Analysis – prints out the entire DataFrame for really basic run stats comparison for everything logged in the Runs folder. Later version will contain a better comparison menu
4. Special Analysis Menu – contains special analysis for specific things in the game, currently just does Winter Hunt 2017 Golems. Will eventually include things like Daily Reward, King’s Rewards and potentially marketplace updating from logged transactions


# Putting in Journal Data

Mousehunt information is not obtainable via any scraping method as a result of the page being forbidden from being read outside of a browser, meaning the user must compile what they would like analyzed. In the runs folder are individual documents with the hunt information stored inside. The hunts are copy and pasted directly off the Mousehunt journal and are stored by text documents organized by the user. To create a new run simply create a new text document, use the format in the sample run file. The name of this file will be how you reference these hunts later in the program.


# Project Files

Run Analysis.bat – Allows user to open the console and access the Main Menu

Main.py - Contains the main menus code and serves as backbone for program

analysisFunctions.py - This module actually performs all of the calculations and displays them to the user

journalReading.py - Looks at all stored runs and turns them into an easy to use DataFrame

fileFunction.py - To make things simpler for some functions, this module deals with anything that writes or reads in a file. More useful in previous versions of the program, before Pandas was used

Marketplace Prices.xlsx - Contains values for valuable pieces of loot. This file, when saved as a CSV, is how the program values locations and their loot wealth

marketPlace.csv - This file is made from the Excel document

runHunts.csv - Created by the program to store the data from the runs in. Will automatically be populated in program from previous data creation unless Create Data is selected in Main Menu

Runs Folder - Individual text documents containing journal entries from every hunt stored. Read the Data section to understand more in depth 


# Dependencies
- Python 3
- Pandas
- NumPy
- Excel (If desire to update marketplace values)

**This app is not intended to provide any in-game advantage and is simply made by fans and for fans to compare different locations, mice and loot drops across the kingdom in an easy to use format. Using this app to gain advantage over other players in the game would be a violation of the game’s terms of service. Additionally, using this information to expose the mechanics of the game would not only ruin the fun but violate the rules. Please, use this tool like an extended progress report and nothing more.

