import os
from tkinter import messagebox
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
import datetime

class crearPortafolio():
    def __init__(self, ruta_predefinda) -> None:
        self.ruta_carpeta = ruta_predefinda
        self.crear_carpeta(self.ruta_carpeta, 'Ejemplo')
        
    def crear_carpeta(self, ruta_carpeta, nombreCarpeta):
        try:
            if len(self.ruta_carpeta) == 0 or None:
                messagebox.showwarning('Advertencia', 'Se debe selecciona una ruta donde crear el portafolio.')
            else:
                ruta_completa = os.path.join(ruta_carpeta, nombreCarpeta)
                os.makedirs(ruta_completa)
        except FileExistsError:
            messagebox.showwarning('Advertencia', 'El portafolio que estás intentando crear ya existe, prueba con otro nombre.')
    
    def mover_archivos(self, carpeta_origen, carpetaDestino):
        pass

    def crear_portada(self):
        self.doc = Document()

        imagen_utp = self.doc.add_picture(r'.\Portafolio\imagenes\logo_utp.png', 
                        width=Cm(3), 
                        height= Cm(3))    
        imagen_utp.alignment = 3
        imagen_utp.left = Cm(0)
        imagen_utp.top = Cm(0)
        imagen_fisc = self.doc.add_picture(r'.\Portafolio\imagenes\logo_fisc.png', 
                        width=Cm(3), 
                        height= Cm(3))
        imagen_fisc.alignment = 2
        imagen_fisc.right = Cm(14)
        imagen_fisc.top = Cm(0)

        self.crear_parrafos(
                                'Universidad Tecnológica de Panamá', 
                                'Arial',
                                12, 
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(
                                'Facultad de Ingeniería de Sistemas Computacionales',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(
                                'Departamento de computacion y simulacion de sistemas',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(
                                'Licenciatura en Ingeniería de Sistemas y computación',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.doc.add_paragraph()
        self.crear_parrafos(    'Nombre de la materia',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.doc.add_paragraph()
        self.crear_parrafos(    'Estudiante:',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.doc.add_paragraph()
        self.crear_parrafos(    'Nombre del estudiante',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.doc.add_paragraph()
        self.crear_parrafos(    'Profesor:',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(    'Nombre del profesor',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        for _ in range(4):
            self.doc.add_paragraph()
        self.crear_parrafos(    '1IL-XXX',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(    self.obtener_semestre(),
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.doc.save('Ejemplo portada.docx')

    def crear_parrafos(self, texto, fuente, size, alineacion):
        p = self.doc.add_paragraph(texto)
        p.alignment = alineacion

        run = p.runs[0]
        font = run.font
        font.name = fuente
        font.size = Pt(size)
    
    def obtener_semestre(self):
        fecha_actual = datetime.datetime.now()
        if 8 <= fecha_actual.month <=12:
            return str('Semestre II, '+str(fecha_actual.year))
        elif 1 <= fecha_actual.month <= 3:
            return str('Verano, '+str(fecha_actual.year))
        else:
            return  str('Semestre I, '+str(fecha_actual.year))

if __name__ == '__main__':
    test = crearPortafolio(r'C:\Users\HP Envy\Downloads')
    test.crear_portada()