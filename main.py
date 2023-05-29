import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from Teacher_ui import Ui_MainWindow
from Teacher_result import creat_result
from leader_result import creat_leader_result
from fudaoyuan_result import fudaoyuan_result


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.pushButton_6.clicked.connect(lambda: self.select_file())
        self.pushButton.clicked.connect(lambda: self.creat_result())
        self.pushButton_3.clicked.connect(lambda: self.creat_fudaoyuan_result())
        self.pushButton_2.clicked.connect(lambda: self.creat_leader_result())

    def creat_result(self):
        # print(self.lineEdit.text())
        creat_result(self.lineEdit.text())

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "./", "*.xlsx")
        self.lineEdit.setText(file_name)
        return file_name

    def creat_leader_result(self):
        creat_leader_result(self.lineEdit.text())

    def creat_fudaoyuan_result(self):
        fudaoyuan_result()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

