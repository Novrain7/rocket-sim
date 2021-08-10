from fx.widgets.widget import *

# basic button class

class Button(Widget):

    def __init__(self, x0, y0, x1, y1, fill = 'white', text = '', textFill = 'black', outline = 'black'):

        super().__init__(x0, y0, x1, y1)

        self.fill = fill
        self.outline = outline

        self.text = text
        self.textFill = textFill
        
        self.isVisible = False

    

    

    

    