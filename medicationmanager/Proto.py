# Title     : TODO
# Objective : TODO
# Created by: dean.wright
# Created on: 17/10/2017

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Proto(QTWidget):
    def __init__(self):
        super().__init__()

        self.initUI()



    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())