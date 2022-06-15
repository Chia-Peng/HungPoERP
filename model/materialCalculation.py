from PySide6 import QtGui, QtCore


class materialCalculation():
    def __init__(self):
        pass

    def calculate(D, d, L):
        return D*d*L

    def getComboBoxList(Type):
        if(Type == "MaterialList"):
            return ['SS400', 'S150C', 'S45C', 'SCM415(SCM21)', 'SCM440(SCM4)']
        elif(Type == "styleList"):
            return ['圓柱', '方管', '鋁擠型', '中空圓管']
        elif(Type == "styleList_D"):
            return ['10', '20', '30', '40']
        elif(Type == "styleList_d"):
            return ['5', '10', '15', '20']

    def getstyleImage(Style):
        pixmap = QtGui.QPixmap('resources\\img\\styleImage.png')
        pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        return pixmap
