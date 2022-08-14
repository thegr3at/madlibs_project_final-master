"""
Author: Ahmed Fath Allah
Date: 8/10/22
This program will let user create Madlibs story.
File madlibs.py

"""

def showMenu():
      fileName = input("Please enter a file name: ")
      fileName = "files/" + fileName
      schoolMadlib = open(fileName, "r")
      reader = schoolMadlib.readlines()
      makeMadlib(reader)

def playGame():
    while True:
        print(f"Welcome to my Madlibs Console Game!")
        userChoice = input(f"\nPlease make a choice from the menu below."
        f"\n1: Make a madlib"                                            
        f"\n2: Exit\n")
        if userChoice == "2":
              break
        else:
             showMenu()


def makeMadlib(reader):
  missingValues = []
  replacmentValues = []
  for line in reader:
        words = line.split()
        [missingValues.append(word) for word in words if "<" and ">" in word]


  for value in missingValues:
        replacment = input(f"Enter one {value}: ")
        replacmentValues.append(replacment)


def printMadlib(lines):
    print("print the madlib here...")

playGame()


