from PySide6 import QtWidgets

from controllers.mainCtrl import mainWindowController

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # fusion風格
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    window = mainWindowController()
    window.show()
    sys.exit(app.exec())
