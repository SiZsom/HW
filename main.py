import numpy as np
import sys
from PyQt6.QtCore import Qt, QTimer, QElapsedTimer
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView


def createLineSequences(A, phi, Lpen: QPen, Cbrush:QBrush, scene: QGraphicsScene, origin = (0,0)):
    dx = A*np.cos(phi)
    dy = A*np.sin(phi)

    x, y = origin

    arms = [] #A forgó karok
    joints = [] #A karok közti "csapágyak"
    
    for i in range(len(A)):
            arms.append(scene.addLine(x, y, x+dx[i], y+dy[i], Lpen))
            joints.append(scene.addEllipse(-5, -5, 10, 10, QPen(Qt.PenStyle.NoPen), Cbrush))
            x += dx[i]
            y += dy[i]
            
    return arms, joints

def updateLineSequences(A, phi, arms, joints, origin = (0,0)):
    dx = A*np.cos(phi)
    dy = A*np.sin(phi)

    x, y = origin

    for i in range(len(A)):
        arms[i].setLine(x, y, x+dx[i], y+dy[i])
        joints[i].setPos(x,y)

        x += dx[i]
        y += dy[i]



app = QApplication(sys.argv)
scene = QGraphicsScene(-400, -225, 800, 450)

line_pen = QPen(QColor("#469FCF"), 3)
#circle_pen = QPen(QColor("#469FCF"), 1)
circle_brush = QBrush(QColor("#841F1F"))



view = QGraphicsView(scene)
view.setWindowTitle("GUI demo")
view.resize(800, 450)
view.setRenderHint(QPainter.RenderHint.Antialiasing)
view.show()

A = np.array([60,140,30,40])
om = np.array([0.2, 0.4, 0.8, 1.6])
phi = np.zeros(4)
arms = [] #A forgó karok
joints = [] #A karok közti "csapágyak"

arms, joints = createLineSequences(A, phi, line_pen, circle_brush, scene)




clock = QElapsedTimer()
clock.start()

game_timer = QTimer()
game_timer.setTimerType(Qt.TimerType.PreciseTimer)


def gameLoop():
    global A, om, phi, arms, joints

    dt = clock.restart() / 1000.0
    if dt > 0.1: dt = 0.1

    phi += om*dt #Update positions
    updateLineSequences(A, phi, arms, joints)



game_timer.timeout.connect(gameLoop)
game_timer.start(16)

sys.exit(app.exec())




        