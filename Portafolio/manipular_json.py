import json
import os
from tkinter import messagebox

class manipularJson():   
    def __init__(self) -> None:
        self.ruta_carpeta = '.\\Portafolio\\usuario\\'
        self.ruta_completa = os.path.join(self.ruta_carpeta, 'credenciales.json')        
    #Si el json no existe, se accedera a este metodo
    def crear_json(self, datos_credenciales):
        with open(self.ruta_completa, 'w') as credenciales:
            json.dump(datos_credenciales, credenciales, indent=4)
    
    #Actualizar informacion del json
    def actualizar_json(self, nuevos_credenciales):
        with open (self.ruta_completa, 'r') as credenciales:
            datos_actuales = json.load(credenciales)
        datos_actuales.update(nuevos_credenciales)
        with open(self.ruta_completa, 'w') as credenciales:
            json.dump(nuevos_credenciales, credenciales, indent=4)
    
    def borrar_json(self)->None:
        if os.path.exists(self.ruta_completa):
            os.remove(self.ruta_completa)
        else:
            pass

    def cargar_credenciales(self):
        if self.existe_json():
            with open(r'.\Portafolio\usuario\credenciales.json', 'r', encoding='utf-8') as archivo:
                self.datos = json.load(archivo)
                return self.datos

    def existe_json(self):
        if os.path.exists(self.ruta_completa):
            return True