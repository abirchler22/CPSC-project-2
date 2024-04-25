"""
Author:         Andrew Birchler
Date:           4/25/2024
Assignment:     Final Project
Course:         CPSC1050
Lab Section:    002

CODE DESCRIPTION:
This game takes place in Phialdelphia Pennsylvania. in this game, the Manayunk police department discovers that Jason Kecle has been killed
and the user is tasked with finding the killer. The user must move through various landmarks in the city of Philadelphia and gather clues.
Once they feel that they have enough information the user travels to the crime scene and makes their final guess as to who the killer is.
IMPORTANT NOTES: inputs are meant to be enter as lowercase, if inputs are capitalized the code will not work properly. Additionally,
any location name that has "The" in it when the list of locations is given at the start of the game must be entered with "The" at the start
when enter by the user or the location will show as being invalid. Have fun playing!
https://github.com/abirchler22/CPSC-project-2/tree/main
"""

#import the intro file
from intro import Intro

#create a class for the location not found error
class LocationNotFoundError(Exception):
    def __init__(self, location_name, message = "Location not found!"):
        self.location_name = location_name
        self.message = message
    
    #function will output the error message
    def __str__(self):
        return f"{self.location_name} -> {self.message}"

#creates a class for the clues
class Clue:
    #initializes the clue class
    def __init__(self, description):
        self.description = description
    #pulls the descriptions of each clue
    def get_description(self):
        return f"{self.description}"
    #returns the clue descriptions
    def __str__(self):
        return self.get_description()

#creates a class for the various locations
class Location:
    #initializes the values in the class
    def __init__(self, name, description, clues):
        self.name = name
        self.description = description
        self.clues = clues
    #gets the name of the locations
    def get_name(self):
        return self.name
    #gets the descriptions of the locations
    def get_description(self):
        return self.description
    #gets the clues stored at each location
    def get_clues(self):
        return self.clues
    #prints the full description of the location with clue numbers
    def __str__(self):
        if len(self.clues) == 1:
            return f"{self.name}: {self.description} This location holds {len(self.clues)} clue."
        else:
            return f"{self.name}: {self.description} This location holds {len(self.clues)} clues."
    #removes clues after they have been found
    def remove_clue(self):
        return self.clues.pop(0)

#creates a class that sets up the game
class SetUp():
    #initializes an empty map and empty set of clues
    def __init__(self):
        self.map = {}
        self.clues = {}
    #adds the various locations to the map
    def add_location(self, location):
        self.map[location.get_name()] = location
    #adds the clues to the set of clues
    def add_clue(self, clue):
        self.clues[clue.get_description()] = clue
    #gets the locations and raises an error if the location doesnt match what is in the map
    def get_location(self, location_name: str):
        location_upper = location_name
        if location_upper not in self.map:
            raise LocationNotFoundError(location_name, "Location not found!")
        else:
            return self.map[location_upper]
    #gets the clues for a certain location
    def get_clue(self, clue_number):
        return self.clues[clue_number]

#creates a class for the inventory of clues already found
class Inventory(SetUp):
    #initializes an empty inventory
    def __init__(self):
        self.found_clues = []
    #adds clues to the inventory once found
    def add_found_clues(self, clue):
        self.found_clues.append(clue)
    #displays the most recently found clue
    def get_last_found_clues(self):
        return self.found_clues[-1]
    #displays the full inventory
    def get_found_clues(self):
        return self.found_clues
    

#assigns values to the various classes and prints the intro
inventory = Inventory()
set_up = SetUp()
print("Welcome to MURDER IN MANAYUNK. First things first lets get your name.\n")
name = input().strip()
print(f"Welcome Detective {name}, here is your case for today:")
intro = Intro()
intro.print_intro()
suspects = ("Travis Kelce", "Tom Brady", "Jalen Hurts", "Brock Purdy", "Spencer Strider")

#adds all locations and clues to the game
set_up.add_location(Location("The Liberty Bell", "One of Philadelphias most well known landmarks, the bell has become synonymous with the city itself.", ['A Super Bowl ring.', 'A note that reads "He has beaten me on the biggest stage in the sport, but never again".']))
set_up.add_location(Location("Boat House Row", "Boat House Row spans much of the Schuylkill river. It is most well known for its displays of christmas lights around the holidays.", []))
set_up.add_location(Location("Independence Hall", "Perhaps the most historic building in all of America. It is the building where America itself was formed.", ['The number 12 carved into the floor.']))
set_up.add_location(Location("Citizens Bank Park", "Home of the Philadelphia Phillies, is known to be one of the loudest stadiums in all MLB.", ['A dirty old football']))
set_up.add_location(Location("The Ben Franklin Bridge", "One of the most famous bridges in all of the north east. The bridge spans from Philadelphia to the neighboring city of Camden New Jersey.", ['A red, white, and blue towel.', 'An old and worn down cleat.', 'A hat with a skull and crossbones on it.']))

set_up.add_clue(Clue('A Super Bowl ring.'))
set_up.add_clue(Clue('A dirty old football'))
set_up.add_clue(Clue('The number 12 carved into the floor.'))
set_up.add_clue(Clue('A note that reads "He has beaten me on the biggest stage in the sport, but never again".'))
set_up.add_clue(Clue('A red, white, and blue towel.'))
set_up.add_clue(Clue('An old and worn down cleat.'))
set_up.add_clue(Clue('A hat with a skull and crossbones on it.'))

#starts the user at The Liberty Bell
print("We will begin your adventure at The Liberty Bell")
current_location: Location = set_up.get_location("The Liberty Bell")

#initializes location_valid to true
location_valid = True

#plays the game
while True:
    try:
        #if the location is valid print the current location with its description and number of clues
        if location_valid:
            print(current_location)
            #set valid_location to false
            location_valid = False
            #if there are any clues at the location execute this loop
            if len(current_location.get_clues()) > 0:
                #print the number of clues and ask if they want to look at the first clue
                print("Would you like to look at the first clue.")
                exit_location = input().lower().strip()
                #create a variable called looking at set it to true
                looking = True
                #validate the users input
                while exit_location not in ["yes", "no"]:
                    print("Invalid input: please enter yes or no")
                    exit_location = input().lower().strip()
                #if they wish to look at the clue then execute this loop
                if exit_location == "yes":
                    #add the clue to the inventory and then print out what clue they just found
                    inventory.add_found_clues(set_up.get_location(current_location.get_name()).remove_clue())
                    print(inventory.get_last_found_clues())
                    #while the user is looking for clues
                    while looking:
                        #check if there are any clues left and if there are not then set looking to false
                        if len(current_location.get_clues()) == 0:
                            print("There are no clues left to look at. Exiting the location.")
                            looking = False
                        #if there are clues left then ask if they want to look at the next clue
                        else:
                            print(f"This location has {len(current_location.get_clues())} clues left.")
                            print("Would you like to look at the next clue?")
                            exit_location = input().lower().strip()
                            #validate the users input
                            while exit_location not in ["yes", "no"]:
                                print("Invalid input: please enter yes or no")
                                exit_location = input().lower().strip()
                            #if they dont want to look at any more clues then set looking to false to exit the location
                            if exit_location == "no":
                                looking = False
                            #if they do want to look at other clues then add the clues to the inventory and print out the last clue that was found
                            else:
                                inventory.add_found_clues(set_up.get_location(current_location.get_name()).remove_clue())
                                print(inventory.get_last_found_clues())
        #ask the user what location they would like to visit next
        print("Please enter the next location you would like to visit.")
        user_input = input().strip()
        #if the next location they want to visit is the crime scene then tske them to the crime scene and enter the end of the game
        if user_input.title() == "Crime Scene":
            #ask for their final guess as to who the culprit is
            print("Please enter your final guess as to who committed this crime.")
            guess = input().title()
            #if they dont guess one of the suspects then have them enter again
            while guess not in  suspects:
                print("Please enter a valid suspect")
                guess = input().title()
            #if they guess correctly then congratulate them on winning the game
            if guess == "Tom Brady":
                print("Great work you have captured the killer.")
            #if they guess incorrectly then tell them they have lost
            else:
                print(f"{guess} is innocent. The killer has escaped capture.")
            #end the game
            break
        #if they dont enter crime scene then validate their selection for the next location
        elif user_input.title() not in set_up.map:
            #if they enter an invalid location then raise the LocationNotFoundError
            raise LocationNotFoundError(user_input, "Location not found!")
        #if they enter a valid location then set location_valid to true and change the current location to the user input
        else:
            #ask the user if they would like to view all of the clues they have found before they go to the next location
            print("Before you leave would you like to view your inventory of found clues?")
            inventory_choice = input().lower().strip()
            #validate the users input
            while inventory_choice not in ["yes", "no"]:              
                print("Invalid input: please enter yes or no")
                inventory_choice = input().lower().strip()
            #if they want to see their inventory then print out the inventory
            if inventory_choice == "yes":
                print(inventory.get_found_clues())
            location_valid = True
            current_location = set_up.get_location(user_input.title())
    #execute the error if it was raised
    except LocationNotFoundError as e:
       print(e)




