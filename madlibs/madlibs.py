"""
Author: Ahmed Fath Allah
Date: 8/10/22
This program will let user create Madlibs story.
File madlibs.py

"""

def showMenu():
    while True:

        userChoice = input(f"\nPlease make a choice from the menu below."
        f"\n1: Make a madlib"                                            
        f"\n2: Exit\n")
        if userChoice == "2":
              break
        else:
             makeMadlib()


def playGame():
    print(f"Welcome to my Madlibs Console Game!")
    showMenu()


def makeMadlib():
    print(f"Files you can open:"
          f"\njungle.madlib"
          f"\nschool.madlib"
          f"\nzoo.madlib")
    fileName = input("\nPlease select one of the files above: ")
    fileName = "files/" + fileName
    fileOpen = open(fileName, "r")
    reader = fileOpen.readlines()
    lines = []

    for line in reader:
        if "<noun>" in line:
            line = line.replace("<noun>", input("Enter one noun: "))
        if "<verb>" in line:
            line = line.replace("<verb>", input("Enter one verb: "))
        if "<adjective>" in line:
            line = line.replace("<adjective>", input("Enter one adjective: "))
        lines.append(line)

    printMadlib(lines)

def printMadlib(lines):
    for line in lines:
        print(line)

playGame()


