from fx.widgets import *

# a scene contains a list of all widgets along with their functions for
# the main program to interpret

class Scene(object):

    def __init__(self):

        self.widgets = []


    def addWidget(self, widget):

        self.widgets.append(widget)


    def insideBounds(self, x, y):

        for index in range(len(self.widgets)):

            if self.widgets[index].insideBounds(x, y):

                return index

        else:

            return -1

    
    def returnWidgets(self):

        return self.widgets