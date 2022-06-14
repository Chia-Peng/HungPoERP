from PySide6 import QtWidgets
from controllers.mainCtrl import mainWindowController
from controllers.materialCalculationCtrl import materialCalculationController


class main():
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx

    def showMaterialCalculation(self):
        print('showMaterialCalculation')
        self.window = materialCalculationController()
        self.window.show()

    def showMainWindow(self):
        print('showMainWindow')
        self.window = mainWindowController()
        self.window.show()
        app.exec()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # fusion風格
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    main().showMainWindow()
    sys.exit()
