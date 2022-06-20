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
            return ['圓棒', '圓管', '六角棒', '鈑材']
        elif(Type == "styleSize"):
            return ['10', '20', '30', '40']

    def getstyleImage(Style):
        pixmap = QtGui.QPixmap('resources\\img\\styleImage.png')
        pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        return pixmap
