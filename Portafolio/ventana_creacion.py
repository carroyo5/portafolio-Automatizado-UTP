import tkinter as tk 
from tkinter import ttk 
from styles import get_app_style
from manipular_json import manipularJson

class PantallaCreacion(tk.Toplevel):
  def __init__(self, inicio) -> None:
        super().__init__(inicio)
        self.title('PA - Portafolio Automatizado')
        self.geometry('1280x720')
        self.resizable(width=False, height=False)

        #Obtener los estilos del archivo styles
        estilo = get_app_style()

       
        