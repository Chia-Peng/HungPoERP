from PySide6 import QtGui, QtCore
from enum import Enum

# 材料類型


class materialType(Enum):
    # 圓棒、圓管、六角棒、鈑材
    roundRod = 0
    roundPipe = 1
    hexRod = 2
    metalSheet = 3


class materialCalculation():
    def __init__(self):
        pass

    def volumeCalculation(item_1, item_2, item_3, type):
        pi = 3.14
        if(type == materialType.roundRod.value):
            radius = item_1/2
            length = item_3
            total = radius*radius*pi*length
        elif(type == materialType.roundPipe.value):
            radius1 = item_1/2
            radius2 = item_2/2
            circleArea1 = radius1*radius1*pi
            circleArea2 = radius2*radius2*pi
            length = item_3
            total = circleArea1-circleArea2*length
        elif(type == materialType.hexRod.value):
            total = 0
            pass
        elif(type == materialType.metalSheet.value):
            length = item_1
            width = item_2
            thickness = item_3
            total = length*width*thickness
        return total

    def weightCalculation(item_1, item_2, item_3):
        total = float(item_1)*float(item_2)*float(item_3)
        return total

    def getComboBoxList(Type):
        if(Type == "MaterialList"):
            return ['SS400', 'S150C', 'S45C', 'SCM415(SCM21)', 'SCM440(SCM4)']
        elif(Type == "styleList"):
            return ['圓棒', '圓管', '六角棒', '鈑材']
        elif(Type == "styleSize"):
            return ['10', '20', '30', '40']

    def getstyleImage(Style):
        pixmap = QtGui.QPixmap('resources\\img\\styleImage.png')
        pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        return pixmap
