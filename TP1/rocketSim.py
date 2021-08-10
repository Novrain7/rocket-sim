from cmu_112_graphics import *

from fileIO import *

from rocketry import *
from nodes import *
from fx import *

################################################################################
# file I/O 
################################################################################

def readNodes(pathname = 'assets\IOFiles\EarthMars\EarthMarsNames.txt'):

    fileString = readFile(pathname)

    nodeList = []

    stringList = fileString.splitlines()

    for string in stringList:

        nodeInfo = string.split(',')

        name = nodeInfo[0].strip()
        description = nodeInfo[1].strip()

        nodeList.append(Node(name, description))

    return nodeList


def readAdjacentNodes(app, pathname = 'assets\IOFiles\EarthMars\EarthMarsNodes.txt'):

    fileString = readFile(pathname)

    nodeList = app.nodeList

    stringList = fileString.splitlines()

    for line in stringList:

        lineList = line.split(',')

        for index in range(len(lineList)):

            lineList[index] = int(lineList[index].strip())

        currentIndex = lineList[0]

        for index in range(1, len(lineList), 2):

            nodeList[currentIndex].addNode(nodeList[index], nodeList[index + 1])

    

################################################################################
# additional graphical functions
################################################################################

def debug1(app): # testing out all the widgets

    app.widgetList = []

    b1 = Button(
        10, 10, 80, 40, 
        fill = 'grey',
        text = 'click me', 
        textFill = 'black',
        outline = 'black'
    )

    m1 = Menu(
        200, 10, 280, 30,
        fill = 'light grey',
        text = 'menu',
        textFill = 'black',
        outline = 'black'
    )

    m1.addItem('item 1')
    m1.addItem('item 2')
    m1.addItem('item 3')

    m1.isCollapsed = False

    app.widgetList.append(b1)
    app.widgetList.append(m1)

def debug2(app): # tests out node network

    for node in app.nodeList:

        node.debug()

def debug21():

    node1 = Node('node a', 'test a')
    node2 = Node('node b', 'test b')

    node1.debug()
    node2.debug()

    node1.addNode(node2, 500)

    node1.debug()
    node2.debug()

def debug22(app):

    app.nodeList[0].debug()

    print(app.nodeList[0].name)

def debug3(): # tests out rocket class

    pass


def displayWidget(app, canvas, widget):

    if isinstance(widget, Widget):

        x0, y0, x1, y1 = widget.getBounds()

        if isinstance(widget, Button) or isinstance(widget, Menu):

            canvas.create_rectangle(
                x0, y0, x1, y1,
                fill = widget.fill,
                outline = widget.outline,
            )

            canvas.create_text(
                (x0 + x1) // 2,
                (y0 + y1) // 2,
                text = widget.text,
                fill = widget.textFill
            )

            if isinstance(widget, Menu):

                if not widget.isCollapsed:

                    for button in widget.items:

                        displayWidget(app, canvas, button)
            


################################################################################
# scenes
################################################################################

def playScene(sceneNum):

    pass

################################################################################
# main graphical functions
################################################################################

def appStarted(app):
    
    app.nodeList = readNodes()

    readAdjacentNodes(app)

    app.timerDelay = 100

    app.widgetList = []

    debug1(app)

    debug2(app)

    #debug21()

    debug22(app)

def redrawAll(app, canvas):

    canvas.create_text(
        0, 0,
        text = 'This is a placeholder',
        anchor = 'nw'
    )

    for widget in app.widgetList:

        displayWidget(app, canvas, widget)
    
def timerFired(app):

    pass

def keyPressed(app, event):

    pass

def mousePressed(app, event):

    x, y = event.x, event.y

    for widget in app.widgetList:

        if widget.insideBounds(x, y):

            print('button pressed')

def mouseMoved(app, event):

    pass

def sizeChanged(app):

    pass

################################################################################
# main
################################################################################

def main():

    a = Rocket()

    runApp(width = 400, height = 400)

if __name__ == '__main__':

    main()