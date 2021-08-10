from fx.widgets.button import *

# dropdown menu class

class Menu(Widget):

    def __init__(self, x0, y0, x1, y1, fill = 'white', text = '', textFill = 'black', outline = 'black'):

        super().__init__(x0, y0, x1, y1)

        self.height = abs(y0 - y1)

        self.fill = fill
        
        self.text = text
        self.textFill = textFill

        self.outline = outline

        self.isCollapsed = True

        # creates an empty list of buttons that will be used as part of the 
        # dropdown menu
        
        self.items = []

        self.currentSelected = -1

    def setBounds(self, x0, y0, x1, y1):

        super().setBounds(x0, y0, x1, y1)

        self.height = abs(y0 - y1)

    

    def addItem(self, item):

        x0, y0, x1, y1 = self.getBounds()

        y0 += ((len(self.items) + 1) * self.height)
        y1 += ((len(self.items) + 1) * self.height)
        
        itemButton = Button(
            x0, y0, x1, y1,
            fill = 'white',
            text = item,
            textFill = 'black',
            outline = ''
        )

        self.items.append(itemButton)


