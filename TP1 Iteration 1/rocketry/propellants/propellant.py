# the propellant class contains the name, specific impulse, and a bit of flavor
# text explaining the type of propellant used

class Propellant(object):

    def __init__(self, name, specificImpulse, description):

        self.name = name
        self.description = description

        self.specificImpulse = specificImpulse