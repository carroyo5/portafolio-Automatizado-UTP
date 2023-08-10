import json
import os

class manipularJson():   
    def __init__(self) -> None:
        self.ruta_carpeta = '.\\Portafolio\\usuario\\'

    #Si el json no exxiste, se accedera a este metodo
    def crear_json(self, datos_credenciales):
        self.ruta_completa = os.path.join(self.ruta_carpeta, 'credenciales.json')
        with open(self.ruta_completa, 'w') as credenciales:
            json.dump(datos_credenciales, credenciales, sort_keys=True, indent=4)
    
    #Actualizar informacion del json
    def actualizar_json(self, nuevos_datos):
        with open (self.ruta_completa, 'r') as credenciales:
            datos_actuales = json.load(credenciales)
        
        datos_actuales.update(nuevos_datos)
    
        with open(self.ruta_completa, 'w') as credenciales:
            json.dump(nuevos_datos, credenciales, indent=4)
    

if __name__ == '__main__':
    datos_ejemplo = {"Nombre": 'Cristhian', 
                    "Apellido": 'Arroyo',
                    "Grupo del curso": '1IL-123',
                    "Tareas": 'Tarea1',
                    "Materia": 'Programacion avanzada',
                    "Profesor": 'Jose Rangel'}
    test = manipularJson()
    test.crear_json(datos_ejemplo)