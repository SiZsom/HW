

#This is the file for all graphics related functions except what's UI.

import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import QGraphicsScene


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