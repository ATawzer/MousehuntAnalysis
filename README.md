# MousehuntAnalysis
Analyze runs from the online game Mousehunt. Provides wealth, point and special location analysis using useful statistical measures

The program is menu-based allowing for flexible and dynamic analysis that is user friendly for a any run or location added. This method means new analysis and insights can be looked at without updating any code.

# Project Files
Main.py - Contains the main menus and serves as backbone of desired analysis
analysisFunctions.py - This module actually performs all of the calculations
journalReading.py - Looks at all stored runs and turns them from a multi-line mess into a easy to use DataFrame
fileFunction.py - To make things simpler for some functions, this module deals with anything that writes or reads in a file. More useful in previous versions of the program, before Pandas was used
Marketplace Prices.xlsx - Contains values for every piece of loot, this file, when saved as a CSV, is how the program values locations and their loot wealth
marketPlace.csv - This file is made from the Excel document
Run Analysis.bat - Allows user to open a console and access all functionality without needing to write any code
runHunts.csv - Created by the program to store the data from the runs in. Will automatically be populated in program from previous data creation unless Create Data is selected in Main Menu
Runs Folder - Individual text documents containing journal entries from every hunt stored. Read the Data section to understand more in depth 

# Storing the Data
In the runs folder are individual documents with the hunt information stored inside. The hunts are copy and pasted directly off the Mousehunt website and are stored by text documents organized by the user. To create a new run simply create a new text document, use the format in a pre-existing text document. The name of this file is how you will reference that run inside the program

# Main Menu Analysis
Right now there are three main ways to analyze your hunts: Run, Location and Cheese. The Main Menu allows you to analyze these three main components and breaks them down based on useful parameters described below. Before using any of these functions make sure to run the Create Data option, which populates the CSV file containing all of the hunt information.
