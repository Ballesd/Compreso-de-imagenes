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

        self.guadadoURL = ''
        self.archivosURL =  ''   
        self.ui.Subir.clicked.connect(self.cargar)
        self.ui.Comprimir.clicked.connect(self.compresor)
        self.ui.Guardar.clicked.connect(self.cargarGU)
        self.extenciones = [".jpg",".jpeg",".png",".mp3"]
        self.show()

    #Carga la carpeta que comprimira los archivos
    def cargar(self):
        self.archivosURL = QFileDialog.getExistingDirectory(self,"Abrir Carpeta de archivos")

    #Carga la carpeta en donde reservara los archivos comprimidos   
    def cargarGU(self):
        self.guadadoURL = QFileDialog.getExistingDirectory(self,"Abrir Carpeta de guardado")

    #Compirme los archivos     
    def compresor(self):
        for filename in os.listdir(self.archivosURL):
            direcc = self.archivosURL + "/" + filename
            nombre, extencion = os.path.splitext(direcc)
            if( extencion in self.extenciones):
                image = Image.open(direcc)
                if(self.guadadoURL == ''):
                    image.save(self.archivosURL + "compressed_" + filename, optimize = True, quality = 60)
                else:
                    image.save(self.guadadoURL+ "/" + "compressed_" + filename, optimize = True, quality = 60)
                    
                
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CompersoFiles()
    window.show()
    sys.exit(app.exec_())