#!/usr/bin/env python
try:
    import sys
    from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QTimer, QObject)
    from PyQt5.QtGui import (QBrush, QColor, QPainter, QPixmap, QFont)
    from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem,
                                 QGraphicsTextItem,
                                 QGridLayout, QVBoxLayout, QHBoxLayout,
                                 QLabel, QLineEdit, QPushButton, QGraphicsPixmapItem)
    from collections import deque
    from random import randint
except Exception:
    print()
    print("Error while Importing required Packages")
    print("Make sure that you have installed package PyQt5 for your python version")
    print("Install all required packages for project using  : pip install -r requirements.txt")
    sys.exit(0)
# initialize the Qt application before doing anything
from qt_app.Window import Window

app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
