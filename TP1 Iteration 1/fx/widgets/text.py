from fx.widgets import Widget

class Text(Widget):

    def __init__(self, x, y, nil = 0, text = '', anchor = '', fill = 'black'):

        super().__init__(x, y, nil, nil)

        self.text = text
        self.fill = fill

        self.achnor = anchor


    def getBounds(self):

        return self.x, self.y


    def insideBounds(self):

        return False
