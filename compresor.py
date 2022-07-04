import sys 
import os
from PyQt5.QtWidgets import QApplication,QAction,QFileDialog,QMainWindow,QPushButton
from InterfazCompresor import Ui_Compresor
from PIL import Image


class CompersoFiles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Compresor()
        self.ui.setupUi(self)

        self.ui.Subir.clicked.connect(self.cargar)
        self.ui.Comprimir.clicked.connect(self.compresor)

        self.show()


    def cargar(self):
        archivoURL = QFileDialog.getOpenFileName(self,'Abrir Archivo','C:\\',"" )
        print("la direcccion es: ",archivoURL[0])
    
    def compresor(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CompersoFiles()
    window.show()
    sys.exit(app.exec_())