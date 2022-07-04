from pickletools import optimize
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

        self.archivosURL =  ''   
        self.extenciones = [".jpg",".jpeg",".png"]
        self.show()


    def cargar(self):
        self.archivosURL = QFileDialog.getExistingDirectory(self, "Abrir Carpeta")

    
    def compresor(self):
        
        for filename in os.listdir(self.archivosURL):
            direcc = self.archivosURL + "/" + filename
            nombre, extencion = os.path.splitext(direcc)
            if( extencion in self.extenciones):
                image = Image.open(direcc)
                image.save(self.archivosURL + "compressed_" + filename, optimize = True, quality = 60) 
        #D:\Users\Balles\Documents\Work,Computational\python\compresor\Compreso-de-imagenes\Imagenes
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CompersoFiles()
    window.show()
    sys.exit(app.exec_())