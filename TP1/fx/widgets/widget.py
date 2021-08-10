# generic widget class with bounds and isVisible parameter. the other more
# complex widgets all inherit these basic properties

class Widget(object):

    def __init__(self, x0, y0, x1, y1):

        self.x0 = x0
        self.y0 = y0

        self.x1 = x1
        self.y1 = y1

        self.isVisible = False

    def setBounds(self, x0, y0, x1, y1):

        self.x0 = x0
        self.y0 = y0

        self.x1 = x1
        self.y1 = y1

    def getBounds(self):

        return self.x0, self.y0, self.x1, self.y1

    def insideBounds(self, x, y):

        x0, y0, x1, y1 = self.getBounds()

        if x0 < x <x1 and y0 < y < y1:
            
            return True

        elif x1 < x < x0 and y1 < y < y0:

            return True

        return False

    def setIsVisible(self, bool):

        self.isVisible = bool
