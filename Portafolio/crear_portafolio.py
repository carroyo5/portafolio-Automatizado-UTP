import os
from tkinter import messagebox
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
import datetime
from manipular_json import manipularJson
from docx2pdf import convert
class crearPortafolio():
    LISTA_CARPETAS = ['PORTADA', 
                    'DESCRIPCIÓN DEL CURSO',
                    'PRESENTACIÓN GENERAL DEL ESTUDIANTE',
                    'ACTIVIDADES O ASIGNACIONES', 
                    'MATERIAL DIDACTICO DEL CURSO',
                    'CONCLUSIÓN']
    
    def __init__(self, ruta_predefinda, nombre_carpeta) -> None:
        self.ruta_carpeta = ruta_predefinda
        self.nombre_carpeta = nombre_carpeta
        self.crear_carpetas(self.ruta_carpeta, self.nombre_carpeta)

    def crear_carpetas(self, ruta_carpeta, nombreCarpeta):
        #Crear carpeta principal del portafolio
        try:
            if not self.ruta_carpeta:
                messagebox.showwarning('Advertencia', 'Se debe selecciona una ruta donde crear el portafolio.')
                return
            else:
                ruta_completa = os.path.join(ruta_carpeta, nombreCarpeta)
                os.makedirs(ruta_completa)
        except FileExistsError:
            messagebox.showwarning('Advertencia', 'El portafolio que estás intentando crear ya existe, prueba con otro nombre.')
        #Carear subcarpetas del portafolio
        try:
            if os.path.exists(ruta_completa):
                for subcarpetas in self.LISTA_CARPETAS:
                    ruta_subcarpetas = os.path.join(ruta_completa, subcarpetas)
                    os.makedirs(ruta_subcarpetas)
            else:
                messagebox.showwarning('Advertencia', 'La carpeta principal del portafolio no existe, intentalo de nuevo.')
        except Exception as h:
            print(h)
        
        try:
            if os.path.exists(os.path.join(ruta_completa, self.LISTA_CARPETAS[3])):
                cargar_datos = manipularJson()
                credenciales_usuario = cargar_datos.cargar_credenciales()
                for nombre, condicion in credenciales_usuario['Subcarpeta_actividades'].items():
                    ruta_subcarpetas = os.path.join(ruta_completa, self.LISTA_CARPETAS[3])
                    if condicion:
                        os.makedirs(nombre.upper())
        except Exception as e:
            print(e)

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
        
        cargar_datos = manipularJson()
        credenciales_usuario = cargar_datos.cargar_credenciales()
        
        self.crear_parrafos(
                                'Universidad Tecnológica de Panamá', 
                                'Arial',
                                12, 
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(
                                credenciales_usuario['Credenciales']['Facultad'],
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(
                                'Departamento de computacion y simulacion de sistemas',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(
                                credenciales_usuario['Credenciales']['Carrera'],
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.doc.add_paragraph()
        self.crear_parrafos(    credenciales_usuario['Credenciales']['Materia'],
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.doc.add_paragraph()
        self.crear_parrafos(    'Estudiante:',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(    credenciales_usuario['Credenciales']['Nombre']+' '+credenciales_usuario['Credenciales']['Apellido'],
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.doc.add_paragraph()
        self.crear_parrafos(    'Profesor:',
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(    credenciales_usuario['Credenciales']['Profesor'],
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        for _ in range(4):
            self.doc.add_paragraph()
        self.crear_parrafos(    credenciales_usuario['Credenciales']['Grupo'],
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        self.crear_parrafos(    self.obtener_semestre(),
                                'Arial',
                                12,
                                WD_PARAGRAPH_ALIGNMENT.CENTER)
        
        ruta = os.path.join(self.ruta_carpeta, self.nombre_carpeta)
        ruta_guardado = str(os.path.join(ruta, 'PORTADA')+'\Portada.docx')
        try:
            self.doc.save(ruta_guardado)
            convert(ruta_guardado)
            os.remove(ruta_guardado)
        except Exception as e:
            messagebox.showwarning('Advertencia', e)

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
    test = crearPortafolio(r'C:\Users\HP Envy\Downloads', 'Portafolio de Ejemplo')
    test.crear_portada()