import numpy as np
import sys
from PyQt6.QtCore import Qt, QTimer, QElapsedTimer
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView


import config
import graphics

app = QApplication(sys.argv)
scene = QGraphicsScene(-400, -225, 800, 450)

line_pen = QPen(QColor("#CCE035"), 3)
#circle_pen = QPen(QColor("#469FCF"), 1)
circle_brush = QBrush(QColor("#2D0057"))



view = QGraphicsView(scene)
view.setWindowTitle("FFT visualiser")
view.resize(800, 450)
view.setRenderHint(QPainter.RenderHint.Antialiasing)
view.show()

A = np.array([60,120,50,60])
om = np.array([0.31, -0.42, 0.811, -2.332])
phi = np.zeros(4)

arms = [] #A forgó karok megjelenítése
joints = [] #A karok közti "csapágyak" megjelenítése

arms, joints = graphics.createLineSequences(A, phi, line_pen, circle_brush, scene)




clock = QElapsedTimer()
clock.start()

game_timer = QTimer()
game_timer.setTimerType(Qt.TimerType.PreciseTimer)


def gameLoop():
    global A, om, phi, arms, joints

    dt = clock.restart() / 1000.0
    if dt > 0.1: dt = 0.1

    phi += om*dt #Update positions
    graphics.updateLineSequences(A, phi, arms, joints)



game_timer.timeout.connect(gameLoop)
game_timer.start(16)

sys.exit(app.exec())




if __name__ == "__main__":
    main()