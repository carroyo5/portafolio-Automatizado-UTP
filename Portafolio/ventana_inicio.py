import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

#Configuracion de la ventana de inicio
ventana_inicio = tk.Tk()
ventana_inicio.title('PA - Portafolio Automatizado')
ventana_inicio.geometry('1280x720')
ventana_inicio.resizable(width=False, height=False)
def seleccion_carpeta():
    carpeta_seleccionada = filedialog.askdirectory()
    if carpeta_seleccionada:
        ruta.config(text=f'Ruta seleccionada: {carpeta_seleccionada}', font=('Inter Bold', 12), foreground='#75AD3C')
    else:
        ruta.config(text='No se ha seleccionado ninguna carpeta.',font=('Inter Bold', 12), foreground='red')
#Funcion para el boton de salir y cerrar la pantalla principal
def funcion_boton_salir():
    ventana_inicio.destroy()
#Titulo
tk.Label(ventana_inicio, text= 'Portafolio Automatizado', font=('Inter Bold',16)).pack()
#Logo
imagen_logo = tk.PhotoImage(file = r'.\Portafolio\imagenes\Logo.png')
ttk.Label(ventana_inicio, image=imagen_logo).place(x=570, y=150)
#Configuracion del estilo del boton
estiloBotonPortafolio = ttk.Style()
estiloBotonPortafolio.configure('BotonPersonalizado.TButton', 
                 relief='flat', 
                 foreground='#555454', 
                 background='#B3D5EE', 
                 borderwidth=4, font=('Inter Bold', 12))
#Espacio en blanco
tk.Label(text='').pack()
imagen_buscador = tk.PhotoImage(file = r'.\Portafolio\imagenes\imagen_buscador.png')
#Configuracion del boton del portafolio
boton_portafolio = ttk.Button(ventana_inicio, text='Selecciona la ruta donde quieres guardar tu portafolio',
           style='BotonPersonalizado.TButton',
           image=imagen_buscador,
           compound='left', 
           command=seleccion_carpeta)
boton_portafolio.pack()
tk.Label(text='').pack()
ruta = tk.Label(ventana_inicio, text='')
ruta.pack()
#Imagen del portafolio nuevo
imagen_nuevo_portafolio = tk.PhotoImage(file= r'.\Portafolio\imagenes\nuevo_archivo.png')
#Estilo del portafolio nuevo
estiloBotonesInferiores = ttk.Style()
estiloBotonesInferiores.configure(
    'EstiloBotonesInferiores.TButton', 
                 relief='flat', 
                 foreground='#000000', 
                 background='#D9D9D9',
                 height= 25,
                 width=20,
                 borderwidth=4, font=('Inter Bold', 20))
#Boton para crear un portafolio nuevo
boton_nuevo_portafolio = ttk.Button(text='Crear nuevo portafolio',
    style= 'EstiloBotonesInferiores.TButton',
     image= imagen_nuevo_portafolio,
     compound='left').place(x=80, y=200)
#Imagen de las credenciales
imagen_credenciales = tk.PhotoImage(file= r'.\Portafolio\imagenes\credenciales.png')
#Boton para crear llenar la informacion de los credenciales
boton_nuevo_portafolio = ttk.Button(text='Mis credenciales',
    style= 'EstiloBotonesInferiores.TButton',
     image= imagen_credenciales,
     compound='left').place(x=80, y=300)
#Imagen para salir
imagen_salir = tk.PhotoImage(file= r'.\Portafolio\imagenes\salir.png')
boton_salir = ttk.Button(text='Salir',
    style= 'EstiloBotonesInferiores.TButton',
     image= imagen_salir,
     compound='left', command= lambda: funcion_boton_salir()).place(x=80, y=400)
tk.Label(text='Hecho por y para estudiantes con mucho ♥', font=('Inter Regular',12)).place(x=30,y=680)
ventana_inicio.mainloop()