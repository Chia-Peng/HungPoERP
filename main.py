from PySide6 import QtWidgets
from controllers.mainCtrl import mainWindowController
from controllers.materialCalculationCtrl import materialCalculationController


class main():
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx

    def entryChanged(self, objectName='default'):
        print('entryChanged:' + objectName)
        if(objectName == 'default'):
            self.window = mainWindowController()
            self.window.show()
            app.exec()
        elif(objectName == 'BtnMaterialCalculation'):
            self.window = materialCalculationController()
            self.window.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # fusion風格
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    main().entryChanged()
    sys.exit()
