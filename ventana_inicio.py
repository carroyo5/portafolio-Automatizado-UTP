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
        ruta.config(text=f'Carpeta Seleccionada: {carpeta_seleccionada}', font=('Inter Bold', 12), foreground='#75AD3C')
    else:
        ruta.config(text='No se ha seleccionado ninguna carpeta.',font=('Inter Bold', 12), foreground='red')


#Titulo
tk.Label(ventana_inicio, text= 'Portafolio Automatizado', font=('Inter Bold',16)).pack()
#Logo
imagen_logo = tk.PhotoImage(file = r'.\imagenes\Logo.png')
ttk.Label(ventana_inicio, image=imagen_logo).place(x=570, y=150)
#Configuracion del estilo del boton
estiloBotonPortafolio = ttk.Style()
estiloBotonPortafolio.configure('BotonPersonalizado.TButton', 
                 relief='ridge', 
                 foreground='#555454', 
                 background='#B3D5EE', 
                 borderwidth=4, font=('Inter', 12))
#Espacio en blanco
tk.Label(text='').pack()
imagen_buscador = tk.PhotoImage(file = r'.\imagenes\imagen_buscador.png')
#Configuracion del boton del portafolio
boton_portafolio = ttk.Button(ventana_inicio, text='Selecciona la ruta donde quieres guardar tu portafolio',
           style='BotonPersonalizado.TButton',
           image=imagen_buscador,
           compound='left', 
           command=seleccion_carpeta)
boton_portafolio.pack()

#boton_imagen = tk.Label(ventana_inicio, image=imagen_buscador)
#boton_imagen.place(x=boton_portafolio.winfo_x(), y=boton_portafolio.winfo_y())

tk.Label(text='').pack()
ruta = tk.Label(ventana_inicio, text='')
ruta.pack()
#Configuracion del estilo del boton de Crear nuevo Portafolio
estiloBotonCrearPortafolio = ttk.Style()
estiloBotonPortafolio.configure(
    'BotonPersonalizadoCrearPortafolio.TButton',
    relief='ridge',
    foreground='#000000',
    background='#D9D9D9',
    borderwidth=4, font=('Inter',32))


ventana_inicio.mainloop()