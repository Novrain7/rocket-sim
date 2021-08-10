from rocketry.propellants import *

# the stage object represents an individual stage of the rocket, containing its
# own propellant, weight, and fuel

class Stage(object):

    def __init__(self, dryMass, wetMass, propellant):

        self.dryMass = dryMass
        self.wetMass = wetMass

        self.propellant = propellant

        self.deltaV = None

# a subclass of Stage that's just the command module of the rocket

class Payload(Stage):

    def __init__(self, name, wetMass, type):

        self.name = name
        self.type = type

        self.wetMass = wetMass