from fx.screen.scene import Scene
from fx.widgets import *

testScenes = []
mainScenes = []

testScene1 = Scene()
testScene2 = Scene()

nextButton = Button(
    50, 50, 100, 70,
    text = 'next'
)


testScene1.addWidget(nextButton)

finalButton = Button(
    40, 40, 90, 60,
    text = 'you did it'
)

testScene2.addWidget(finalButton)

textBox = TextField(
    40, 80, 190, 100
)

testScene2.addWidget(textBox)

testScenes = [testScene1, testScene2]
