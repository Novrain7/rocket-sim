from cmu_112_graphics import *

from fileIO import *

from rocketry import *
from nodes import *
from fx import *
from fx.screen.scenes import testScene1
from fx.screen.scenes import testScene2

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

        currentIndex = lineList[0] - 1

        for index in range(1, len(lineList), 2):

            adjacentNode = lineList[index] - 1
            distance = lineList[index + 1]

            nodeList[currentIndex].addNode(nodeList[adjacentNode], distance)
            

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

def debug4(app):

    app.scenes = testScenes

def displayWidget(app, canvas, widget):

    if isinstance(widget, Widget):

        x0, y0, x1, y1 = widget.getBounds()

        if isinstance(widget, Button):

            if widget.isClicked: widget.changeColorState()

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

        elif isinstance(widget, Menu):

            if not widget.isCollapsed:

                for button in reversed(widget.items):

                    displayWidget(app, canvas, button)

            if widget.isClicked: widget.changeColorState()

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

        elif isinstance(widget, TextField):

            if widget.isClicked: 
                
                widget.changeColorState()

                widget.selected = True

            canvas.create_rectangle(
                x0, y0, x1, y1,
                fill = widget.fill,
                outline = widget.outline,
            )

            canvas.create_text(
                x0,
                y0,
                text = widget.text,
                fill = widget.textFill,
                anchor = 'nw'
            )




################################################################################
# scenes
################################################################################

def playScene(app, sceneNum):

    app.currentScene = sceneNum

################################################################################
# main graphical functions
################################################################################

def appStarted(app):
    
    app.nodeList = readNodes()

    readAdjacentNodes(app)

    app.timerDelay = 100

    app.scenes = testScenes

    app.currentScene = 0

    playScene(app, app.currentScene)

    #debug1(app)

    #debug2(app)

    #debug21()

    #debug22(app)

def redrawAll(app, canvas):

    '''canvas.create_text(
        0, 0,
        text = 'This is a placeholder',
        anchor = 'nw'
    )

    for widget in app.widgetList:

        displayWidget(app, canvas, widget)'''

    scene = app.scenes[app.currentScene]

    for widget in scene.widgets:

        displayWidget(app, canvas, widget)
    
def timerFired(app):

    pass

def keyPressed(app, event):

    scene = app.scenes[app.currentScene]

    key = event.key

    if key == 'Enter':

        for widget in scene.widgets:

            if isinstance(widget, TextField) and widget.selected:

                widget.text = ''

    if len(key) == 1 and key.isdigit():

        for widget in scene.widgets:

            if isinstance(widget, TextField) and widget.selected:

                widget.text += key

    

def mousePressed(app, event):

    scene = app.scenes[app.currentScene]

    x, y = event.x, event.y

    eventVal = scene.insideBounds(x, y)

    if not eventVal == -1:

        print('button pressed')

        widgetList = scene.widgets

        widgetList[eventVal].isClicked = True

        if eventVal == 0:

            if not app.currentScene + 1 >= len(app.scenes):

                app.currentScene += 1

def mouseReleased(app, event):

    scene = app.scenes[app.currentScene]

    for widget in scene.widgets:

        widget.isClicked = False

        widget.changeColorState()

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