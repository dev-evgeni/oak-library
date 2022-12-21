import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    apply_stylesheet(app, theme='dark_teal.xml')

    window.show()

    sys.exit(app.exec_())
