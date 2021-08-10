from fx.widgets.widget import *

# textfield used for inputting values

class TextField(Widget):

    def __init__(self, x0, y0, x1, y1):

        super().__init__(x0, y0, x1, y1)

        self.selected = False
        self.fill = 'white'

        self.text = ''