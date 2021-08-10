# the node class contains information regarding the different places the rocket
# can travel. Each individual instance of node contains an expandable dict of 
# adjacent nodes, each with a seperate distance.

class Node(object):

    def __init__(self, name, description):

        self.name = name
        self.description = description

        self.nodes = dict()

    # addNode() is a recursive function that assigns two given nodes as adjacent
    # to one another with a given distance. The recursive nature of the function
    # ensures that both nodes have each other added

    def addNode(self, otherNode, distance):

        if not self in otherNode.nodes.keys():

            otherNode.nodes[self] = distance

            otherNode.addNode(self, distance)

    def __repr__(self):

        return f'{self.name}: {self.description}'

    def debug(self):

        print(self.name)

        for key in self.nodes.keys():

            print(f'\t{key.name} {self.nodes[key]}')

        print()
