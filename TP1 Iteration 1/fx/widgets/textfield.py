from fx.widgets.widget import *

# textfield used for inputting values

class TextField(Widget):

    defaultColors = ['white', 'light blue']

    def __init__(self, x0, y0, x1, y1):

        super().__init__(x0, y0, x1, y1)

        self.selected = False
        self.fill = TextField.defaultColors[0]
        self.outline = 'black'

        self.text = ''
        self.textFill = 'black'

        self.selected = False

    def changeColorState(self):

        if self.isClicked or self.selected:

            self.fill = TextField.defaultColors[1]

        else:

            self.fill = TextField.defaultColors[0]

    def setText(self, text):

        self.text = text