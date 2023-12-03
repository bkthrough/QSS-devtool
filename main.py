# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from qtpy.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton
from src.main import DevTool


def create_test_widget():
    widget = QWidget()
    layout = QHBoxLayout(widget)
    layout.addWidget(QLabel("main window"))
    layout.addWidget(QPushButton("button"))
    width = 400
    height = 400
    widget.setGeometry(500, 300, width, height)
    return widget


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = create_test_widget()
    devtool = DevTool(widget)
    widget.show()
    devtool.show()
    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
