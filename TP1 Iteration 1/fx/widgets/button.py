from fx.widgets.widget import *

# basic button class

class Button(Widget):

    defaultColors = ['light grey', 'grey']

    def __init__(self, x0, y0, x1, y1, fill = defaultColors[0], text = '', textFill = 'black', outline = 'black'):

        super().__init__(x0, y0, x1, y1)

        self.fill = fill
        self.outline = outline

        self.text = text
        self.textFill = textFill

    def changeColorState(self):

        if self.isClicked:

            self.fill = Button.defaultColors[1]

        else:

            self.fill = Button.defaultColors[0]

    

    

    