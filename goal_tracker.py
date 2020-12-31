#!python3

#This program keeps track of the status of my projects to let me know where I stand with each one.

#I will continue to add to this program.
#TODO: Create user manual/ documentation
#TODO: create github repository
#TODO: create flowchart
#Additions:
#TODO: KPI - closure rates and length of projects
#TODO: GUI - Web based gui to access this program from anywhere and edit through webpage

#imports
import os
import csv
import json

#Add a new goal to the list
def newGoal(goal, status, difficulty):
    #with open(goalsFile, 'a') as f:

    return None

#Global Variables        
goalsFile = 'files/goals.csv'        
negative = ['n', 'no', 'nope']
positive = ['y', 'yes', 'yep', 'yup', 'yeah']
choices = ['New Goal', 'Edit Goal', 'Delete Goal', 'New Reward', 'Edit Reward', 'Delete Reward']
count = 1

with open(goalsFile, 'a') as f:
    try:
        goalsList = f.readlines()
    except:
        print('You have no goals')
    else:
        for goal in goalsList:
            print("Goal: {} Status: {}".format(goal, goalsList[goal]))
        


for choice in choices:
    print(f'{count}. {choice}')
    count += 1

while True:
    try:
        option = int(input('What would you like to do? (Choose a number): '))
    except:
        print('Please enter a valid option')
    else:
        #Option to add a new goal
        if option == 1:
            newGoal = input('Enter your new goal: ')
            newGoalStatus = int(input('Is this goal: 1: idea, 2: planned, 3: In Progress? '))
            if newGoalStatus == 1:
                newGoalStatus = 'idea'
            elif newGoalStatus == 2:
                newGoalStatus = 'planned'
            elif newGoalStatus == 3:
                newGoalStatus = 'in progress'
            else:
                print("Option not valid")
            difficulty = int(input('Choose a difficulty from 1 to 10: '))
            newGoal(newGoal, newGoalStatus, difficulty)
        
        #Option to edit an existing goal
        if option == 2:
            try:
                with open (goalsFile, 'r') as f:
                    goalData = json.load(f)
                    print(goalData)
            except:
                print()
            #TODO: add an else section that will print the goals and ask user to choose which goal to edit
                


        _quit = input("More to do? (Y/N): ")
        if _quit.lower() in (negative):
            break
        elif _quit.lower() in (positive):
            continue
#TODO: determine best way to handle multiple choice scenarios.            