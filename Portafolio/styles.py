# Estilos comunes para los componentes como los botones, etc.

from tkinter import ttk

# Esta función define cada uno de los estilos de cada componente en la aplicación
def get_app_style():
  app_style = ttk.Style()

  app_style.configure('EstiloBotonesInferiores.TButton', relief='flat', 
                 foreground='#000000', 
                 background='#D9D9D9',
                 height= 25,
                 width=20,
                 borderwidth=4, font=('Inter Bold', 20))

  app_style.configure('BotonPersonalizado.TButton', 
                 relief='flat', 
                 foreground='#555454', 
                 background='#B3D5EE', 
                 borderwidth=4, font=('Inter Bold', 12))

  return app_style


