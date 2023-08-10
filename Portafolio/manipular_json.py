import json
import os

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
    
    def existe_json(self):
        if os.path.exists(self.ruta_completa):
            return True
        else:
            return False