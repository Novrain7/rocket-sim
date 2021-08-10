from rocketry.stage import *
from rocketry.propellants import *

import math

# each instanc of the rocket class contains a list of stages (the first one 
# being the command module of said rocket) along with the functions needed
# for the rocket to travel to different locations

class Rocket(object):

    g = 9.80665 # gravitational constant

    def __init__(self):

        self.stages = []

    def addStage(self, stage):

        self.stages.append(stage)

    def calculateDeltaV(self):

        for index in range(len(self.stages)):

            # the payload of the rocket does not have a deltaV

            if isinstance(self.stages[index], Payload): continue

            grossMass = 0

            for otherIndex in range(index):

                grossMass += self.stages[otherIndex].wetMass

            stage = self.stages[index]

            stage.deltaV = Rocket.tsiolkovsky(stage, grossMass)

    def tsiolkovsky(stage, grossMass):

        # tsiolkovsky's rocket equation, which calculates change in velocity
        # using the rocket's dry mass and wet mass and the propellant's 
        # effective velocity

        specificImpulse = stage.propellant.specificImpulse

        effectiveV = specificImpulse * Rocket.g

        # the function also takes into account the combined weight of all the
        # other stages above the current stage into the deltaV calculation

        dryMass = stage.dryMass + grossMass
        wetMass = stage.wetMass + grossMass

        # the change in velocity is truncated into an integer value for better
        # readability; cutting off less than a m/s of velocity shouldn't effect
        # things too much for the rocket

        return int(effectiveV * math.log(wetMass / dryMass))