import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    # Abrir el cuadro de diálogo para seleccionar un archivo
    ruta_archivo = filedialog.askopenfilename()
    
    # Imprimir la dirección completa del archivo seleccionado
    print("El archivo seleccionado es: ", ruta_archivo)

# Crear la ventana principal
ventana = tk.Tk()

# Crear un botón para abrir el cuadro de diálogo de selección de archivos
boton_abrir_archivo = tk.Button(ventana, text="Seleccionar archivo", command=abrir_archivo)
boton_abrir_archivo.pack()

# Iniciar el bucle de eventos de la ventana principal
ventana.mainloop()