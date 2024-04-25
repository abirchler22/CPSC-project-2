class LocationNotFoundError(Exception):
    def __init__(self, location_name, message = "Location not found!"):
        self.location_name = location_name
        self.message = message
    
    def __str__(self):
        return f"{self.location_name} -> {self.message}"

class Clues:
    def __init__(self, number, decription):
        self.number = number
        self.object = description
    
    def get_discription(self):
        return f"{self.description}"

class Locations:
    def __init__(self, name, description, clues):
        self.name = name
        self.description = description
        self.clues = clues
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_clues(self):
        return self.clues

    def __str__(self):
        if len(self.clue) == 1:
            return f"{self.name}: {self.description} This location holds {len(self.clues)} clue."
        else:
            return f"{self.name}: {self.description} This location holds {len(self.clues)} clues."

class SetUp(self):
    def __init__(self):
        self.map = {}
        self.clues = {}
    
    def add_location(self, location):
        self.map[location.get_name()] = spot

    def add_clue(self, clue):
        self.clue[clue.get_name()] = clue

    def get_location(self, location_name):
        location_upper = location_name.title()
        if location_upper not in self.map:
            raise LocationNotFoundError(location_name, "Location not found!")
        else:
            return self.map[location_upper]
    
    def get_clue(self, clue_number):
        return self.clues[clue_number]


set_up = SetUp()

set_up.add_location(Location("The Liberty Bell", "One of Philadelphias most well known landmarks, the bell has become synonymous with the city itself.", ['Clue 1', 'Clue 4']))
set_up.add_location(Location("Boat House Row", "Boat House Row spans much of the Schuylkill river. It is most well known for its displays of christmas lights around the holidays.", []))
set_up.add_location(Location("Independence Hall", "Perhaps the most historic building in all of America. It is the building where America itself was formed.", ['Clue 3']))
set_up.add_location(Location("Citizens Bank Park", "Home of the Philadelphia Phillies, is known to be one of the loudest stadiums in all MLB.", ['Clue 2']))
set_up.add_location(Location("The Ben Franklin Bridge", "One of the most famous bridges in all of the north east. The spans from Philadelphia to the neighboring city of Camden New Jersey."['Clue 5', 'Clue 6', 'Clue 7']))

set_up.add_clue(Clue("Clue 1", "A Super Bowl ring."))
set_up.add_clue(Clue("Clue 2", "A dirty old football"))
set_up.add_clue(Clue("Clue 3", "The number 12 carved into the floor."))
set_up.add_clue(Clue("Clue 4", 'A note that reads "He has beaten me on the biggest stage in the sport, but never again".'))
set_up.add_clue(Clue("Clue 5", "A red, white, and blue towel."))
aet_up.add_clue(Clue("Clue 6", "An old and worn down cleat."))
set_up.add_clue(Clue("Clue 7", "A hat with a skull and crossbones on it."))

    
