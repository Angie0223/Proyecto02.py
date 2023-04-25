import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import math
import numpy as np
from tkinter import filedialog

# Tupla con los nombres de las figuras geométricas a utilizar, posteriormente se utilizará para formar matrices de datos para Reportes
figuras = ("Cuadrado:","Rectángulo:","Triángulo:","Rombo:","Pentágono:","Hexágono:","Circulo:","Trapecio:","Paralelogramo:")


# Clases de Areas y Perimetros:

# Area (patrón: Factory):

# Clase base
class Area:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contador = 0

    def contar(self):
        self.contador += 1

# Sub clases
class CuadradoA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

class RectanguloA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

class TrianguloA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

class RomboA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

class PentagonoA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

class HexagonoA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

class CirculoA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

class TrapecioA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

class ParalelogramoA(Area):
    def __init__(self, nombre):
        super().__init__(nombre)

# Objetos pertenecientes a la clase de Áreas:

cuadradoAA = CuadradoA("Cuadrado Area")
rectanguloAA = RectanguloA("Rectangulo Area")
trianguloAA = TrianguloA("Triangulo Area")
romboAA = RomboA("Rombo Area")
pentagonoAA = PentagonoA("Pentagono Area")
hexagonoAA = HexagonoA("Hexagono Area")
circuloAA = CirculoA("Circulo Area")
trapecioAA = TrapecioA("Trapecio Area")
paralelogramoAA = ParalelogramoA("Paralelogramo Area")

# Perímetro (Singleton):
class Perimetro(object):
    
    __instance = None
    
    def __init__(self):
        self.cuadradoP = 0
        self.rectanguloP = 0
        self.trianguloP = 0
        self.romboP = 0
        self.pentagonoP = 0
        self.hexagonoP = 0
        self.circuloP = 0
        self.trapecioP = 0
        self.paralelogramoP = 0
     
    def __new__(cls,*args,**kwargs):
        if not isinstance(cls.__instance, cls):
            cls._instance = object.__new__(cls)

        return cls._instance

    def SumaCuadradoP(self):
        self.cuadradoP += 1
    
    def SumaRectanguloP(self):
        self.rectanguloP += 1
        
    def SumaTrianguloP(self):
        self.trianguloP += 1
    
    def SumaRomboP(self):
        self.romboP += 1
        
    def SumaPentagonoP(self):
        self.pentagonoP += 1
        
    def SumaHexagonoP(self):
        self.hexagonoP += 1
        
    def SumaCirculoP(self):
        self.circuloP += 1
        
    def SumaTrapecioP(self):
        self.trapecioP += 1
        
    def SumaParalelogramoP(self):
        self.paralelogramoP += 1
        
    def DevolverCuadradoP(self):
        return (self.cuadradoP)
    
    def DevolverRectanguloP(self):
        return (self.rectanguloP)
    
    def DevolverTrianguloP(self):
        return (self.trianguloP)
    
    def DevolverRomboP(self):
        return (self.romboP)
    
    def DevolverPentagonoP(self):
        return (self.pentagonoP)
    
    def DevolverHexagonoP(self):
        return (self.hexagonoP)
    
    def DevolverCirculoP(self):
        return (self.circuloP)
    
    def DevolverTrapecioP (self):
        return (self.trapecioP)
    
    def DevolverParalelogramoP(self):
        return (self.paralelogramoP)
   
# Objeto de la clase perímetro
perimetroPP = Perimetro()
 
# Funciones:

# Crear matrices de reporte
def CrearMatriz(tupla,vector):
    matriz = np.array([tupla,vector])
    
    return matriz

# Cálculo de perimetros
def CalculoPerimetros(opcion, datos):
    if opcion == 1: # Cuadrado
        perimetro = 4*datos[0]
        perimetroPP.SumaCuadradoP()
    elif opcion == 2: # Rectangulo
        perimetro = datos[0] +datos[1] +datos[0] +datos[1]
        perimetroPP.SumaRectanguloP()
    elif opcion == 3: # Triangulo
        perimetro = datos[0]+datos[1]+datos[2]
        perimetroPP.SumaTrianguloP()
    elif opcion == 4: # Rombo
        perimetro = 4*datos[0]
        perimetroPP.SumaRomboP()
    elif opcion == 5: # Pentágono
        perimetro = 5*datos[0]
        perimetroPP.SumaPentagonoP()
    elif opcion == 6: # Hexágono
        perimetro = 6*datos[0]
        perimetroPP.SumaHexagonoP()
    elif opcion == 7: # Círculo
        perimetro = math.pi*2*datos[0]
        perimetroPP.SumaCirculoP()
    elif opcion == 8: # Trapecio
        perimetro = datos[0]+datos[1]+(2*datos[2])
        perimetroPP.SumaTrapecioP()
    else: # Paralelogramo
        perimetro = 2*(datos[0]+datos[1])
        perimetroPP.SumaParalelogramoP()
    
    return perimetro

# Cálculo de áreas
def CalculoAreas(opcion, datos):
    
    # Diccionario con los metodos de la clase Areas
    diccAreas = {1:cuadradoAA.contar,2:rectanguloAA.contar,3:trianguloAA.contar,4:romboAA.contar,5:pentagonoAA.contar,6:hexagonoAA.contar,7:circuloAA.contar,8:trapecioAA.contar,9:paralelogramoAA.contar}
    
    diccAreas[opcion]() # Llamada al método
    
    if opcion == 1: # Cuadrado
        area = datos[0]**2
    elif opcion == 2: # Rectangulo
        area = datos[0] * datos[1]
    elif opcion == 3: # Triangulo
        semi = (datos[0]+datos[1]+datos[2])/2
        area = math.sqrt(semi*(semi-datos[0])*(semi-datos[1])*(semi-datos[2]))
    elif opcion == 4: # Rombo
        area = (datos[0]*datos[1])/2
    elif opcion == 5: # Pentágono
        area = (datos[0]*datos[1])/2
    elif opcion == 6: # Hexágono
        area = (datos[0]*datos[1])/2
    elif opcion == 7: # Círculo
        area = math.pi*(datos[0]**2)
    elif opcion == 8: # Trapecio
        area = ((datos[0]+datos[1])*datos[2])/2
    else: # Paralelogramo
        area = datos[0]*datos[1]
    
    return area

# Crear matrices de reporte
def CrearMatriz(tupla,vector):
    matriz = np.array([tupla,vector])
    
    return matriz.T

# Guardar los datos del reporte en un archivo de texto
def guardar_matrices(matriz1, descripcion1, matriz2, descripcion2):
    # abrir la ventana de diálogo para elegir la ubicación del archivo
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.asksaveasfile(defaultextension=".txt")
    
    # guardar la primera matriz en el archivo de texto
    np.savetxt(archivo, matriz1, delimiter="\t", fmt="%s", header=descripcion1)
    
    # escribir una línea en blanco en el archivo
    archivo.write("\n")
    
    # guardar la segunda matriz en el archivo de texto
    np.savetxt(archivo, matriz2, delimiter="\t", fmt="%s", header=descripcion2)
    
    # cerrar el archivo
    archivo.close()

# Función para el reporte
def GeneracionReporte():
    # Vectores con los datos de perímetros y áreas
    vectorAreas = [cuadradoAA.contador,rectanguloAA.contador,trianguloAA.contador,romboAA.contador,pentagonoAA.contador,hexagonoAA.contador,circuloAA.contador,trapecioAA.contador,paralelogramoAA.contador]
    vectorPerimetros = [perimetroPP.DevolverCuadradoP(),perimetroPP.DevolverRectanguloP(),perimetroPP.DevolverTrianguloP(),perimetroPP.DevolverRomboP(),perimetroPP.DevolverPentagonoP(),perimetroPP.DevolverHexagonoP(),perimetroPP.DevolverCirculoP(),perimetroPP.DevolverTrapecioP(),perimetroPP.DevolverParalelogramoP()]

    # Matrices formadas para el reporte
    matrizAreas = CrearMatriz(figuras,vectorAreas)
    matrizPerimetros = CrearMatriz(figuras,vectorPerimetros)
    
    # Guardar los datos del reporte en un archivo txt
    
    guardar_matrices(matrizPerimetros,"Cantidad de veces que se calculó el perímetro por figuras:",matrizAreas,"Cantidad de veces que se calculó el área por figuras:")
    
# GUI Principales:
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de figuras")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/1.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()
        
        # Título principal
        self.title_Label = tk.Label(self.master, text="Bienvenido(a) a la calculadora de figuras")
        self.title_Label.config(font=("Arial", 20))
        self.title_Label.pack(pady=20)
        
        # Botones de opciones
        
        # Crear una lista de textos para los botones
        button_texts = ['Calcular área', 'Calcular perímetro', 'Generar Reporte', 'Salir']

        # Crear una lista vacía para almacenar los botones
        buttons = []

        # Crear los botones y agregarlos a la lista "buttons"
        for text in button_texts:
            
            if text == 'Calcular área':
                comando = self.show_area_window
            elif text == 'Calcular perímetro':
                comando = self.show_perimeter_window
            elif text == 'Generar Reporte':
                comando = self.generate_report
            else:
                comando = self.master.destroy
            
            button = tk.Button(self.master, text=text, command = comando, relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
            buttons.append(button)

        # Mostrar los botones en pantalla utilizando el método "pack()"
        for button in buttons:
            button.pack(pady=10) 
        
    def show_area_window(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
    def show_perimeter_window(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
    def generate_report(self):
        GeneracionReporte()
        messagebox.showinfo("Reporte", "Reporte generado correctamente")
         
class AreaWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de figuras")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/2.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()
        
        # Título
        self.title_Label = tk.Label(self.master, text="Seleccione una figura para calcular el área")
        self.title_Label.config(font=("Arial", 20))
        self.title_Label.pack(pady=20)
        
        # Botones de figuras
        frame1 = tk.Frame(self.master)
        frame1.pack(side=tk.TOP)
        
        self.cuadrado_Button = tk.Button(frame1, text="Cuadrado", command = self.AreaCuadrado,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.cuadrado_Button.pack(pady=10, side=tk.LEFT)
        
        self.rectangulo_Button = tk.Button(frame1, text="Rectángulo", command = self.AreaRectangulo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.rectangulo_Button.pack(pady=10, side=tk.LEFT)
        
        self.triangulo_Button = tk.Button(frame1, text="Triángulo", command = self.AreaTriangulo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.triangulo_Button.pack(pady=10,side=tk.LEFT)
        
        frame2 = tk.Frame(self.master)
        frame2.pack(side=tk.TOP)
        
        self.rombo_Button = tk.Button(frame2, text="Rombo", command = self.AreaRombo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.rombo_Button.pack(pady=10,side=tk.LEFT)
        
        self.pentagono_Button = tk.Button(frame2, text="Pentágono", command = self.AreaPentagono,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.pentagono_Button.pack(pady=10,side=tk.LEFT)
        
        self.hexagono_Button = tk.Button(frame2, text="Hexágono", command = self.AreaHexagono,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.hexagono_Button.pack(pady=10,side=tk.LEFT)
        
        frame3 = tk.Frame(self.master)
        frame3.pack(side=tk.TOP)
        
        self.circulo_Button = tk.Button(frame3, text="Círculo", command = self.AreaCirculo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.circulo_Button.pack(pady=10,side=tk.LEFT)
        
        self.trapecio_Button = tk.Button(frame3, text="Trapecio", command = self.AreaTrapecio,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.trapecio_Button.pack(pady=10,side=tk.LEFT)
        
        self.paralelogramo_Button = tk.Button(frame3, text="Paralelogramo", command = self.AreaParalelogramo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.paralelogramo_Button.pack(pady=10,side=tk.LEFT)
        
        frame4 = tk.Frame(self.master)
        frame4.pack(side=tk.TOP)
        
        self.volver_Button = tk.Button(frame4, text="Volver", command=self.show_main_window,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.volver_Button.pack(pady=10, side=tk.TOP)
        
        self.salir_Button = tk.Button(frame4, text="Salir", command=self.master.destroy,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.salir_Button.pack(pady=10, side=tk.TOP)
        
    def show_main_window(self):
        self.master.destroy()
        MainWindow(tk.Tk())
    
    def AreaCuadrado(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaCuadradoGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
        
    def AreaTriangulo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaTrianguloGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
    
    def AreaRectangulo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaRectanguloGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
    
    def AreaRombo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaRomboGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
            
    def AreaPentagono(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaPentagonoGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
            
    def AreaHexagono(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaHexagonoGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
            
    def AreaCirculo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaCirculoGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
            
    def AreaTrapecio(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaTrapecioGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
            
    def AreaParalelogramo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = AreaParalelogramoGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
        
class PerimetroWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de figuras")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/3.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()
        
        # Título
        self.title_Label = tk.Label(self.master, text="Seleccione una figura para calcular el perímetro")
        self.title_Label.config(font=("Arial", 20))
        self.title_Label.pack(pady=20)
        
        # Botones de figuras
        frame1 = tk.Frame(self.master)
        frame1.pack(side=tk.TOP)
        
        self.cuadrado_Button = tk.Button(frame1, text="Cuadrado", command = self.PerimetroCuadrado,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.cuadrado_Button.pack(pady=10, side=tk.LEFT)
        
        self.rectangulo_Button = tk.Button(frame1, text="Rectángulo", command = self.PerimetroRectangulo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.rectangulo_Button.pack(pady=10, side=tk.LEFT)
        
        self.triangulo_Button = tk.Button(frame1, text="Triángulo", command = self.PerimetroTriangulo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.triangulo_Button.pack(pady=10,side=tk.LEFT)
        
        frame2 = tk.Frame(self.master)
        frame2.pack(side=tk.TOP)
        
        self.rombo_Button = tk.Button(frame2, text="Rombo", command = self.PerimetroRombo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.rombo_Button.pack(pady=10,side=tk.LEFT)
        
        self.pentagono_Button = tk.Button(frame2, text="Pentágono", command = self.PerimetroPentagono,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.pentagono_Button.pack(pady=10,side=tk.LEFT)
        
        self.hexagono_Button = tk.Button(frame2, text="Hexágono", command = self.PerimetroHexagono,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.hexagono_Button.pack(pady=10,side=tk.LEFT)
        
        frame3 = tk.Frame(self.master)
        frame3.pack(side=tk.TOP)
        
        self.circulo_Button = tk.Button(frame3, text="Círculo", command = self.PerimetroCirculo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.circulo_Button.pack(pady=10,side=tk.LEFT)
        
        self.trapecio_Button = tk.Button(frame3, text="Trapecio", command = self.PerimetroTrapecio,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.trapecio_Button.pack(pady=10,side=tk.LEFT)
        
        self.paralelogramo_Button = tk.Button(frame3, text="Paralelogramo", command = self.PerimetroParalelogramo,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.paralelogramo_Button.pack(pady=10,side=tk.LEFT)
        
        frame4 = tk.Frame(self.master)
        frame4.pack(side=tk.TOP)
        
        self.volver_Button = tk.Button(frame4, text="Volver", command=self.show_main_window,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.volver_Button.pack(pady=10, side=tk.TOP)
        
        self.salir_Button = tk.Button(frame4, text="Salir", command=self.master.destroy,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.salir_Button.pack(pady=10, side=tk.TOP)
        
    def show_main_window(self):
        self.master.destroy()
        MainWindow(tk.Tk())
        
    def PerimetroCuadrado(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroCuadradoGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
            
    def PerimetroRectangulo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroRectanguloGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
            
    def PerimetroTriangulo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroTrianguloGUI(ventana)

            # Mostrar la ventana
            ventana.mainloop()
            
    def PerimetroRombo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroRomboGUI(ventana)
            
            # Mostrar la ventana
            ventana.mainloop()
    
    def PerimetroPentagono(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroPentagonoGUI(ventana)
            
            # Mostrar la ventana
            ventana.mainloop()
    
    def PerimetroHexagono(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroHexagonoGUI(ventana)
            
            # Mostrar la ventana
            ventana.mainloop()
    
    def PerimetroCirculo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroCirculoGUI(ventana)
            
            # Mostrar la ventana
            ventana.mainloop()
            
    def PerimetroTrapecio(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroTrapecioGUI(ventana)
            
            # Mostrar la ventana
            ventana.mainloop()
            
    def PerimetroParalelogramo(self):
            self.master.destroy()
            # Crear la ventana principal
            ventana = tk.Tk()

            # Crear la GUI
            figuras_gui = PerimetroParalelogramoGUI(ventana)
            
            # Mostrar la ventana
            ventana.mainloop()
 
#GUI de calculos de perímetros
class PerimetroCuadradoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un cuadrado")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/4.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un cuadrado", font=("Arial", 24))
        self.title_label.pack()

        # Agregar la caja de texto y el botón
        self.label = tk.Label(master, text="Lado: ")
        self.label.pack()

        self.textbox = tk.Entry(master)
        self.textbox.pack()

        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener el valor de la textbox y hacer algo con él
        data = self.textbox.get()
        try:
            # Convertir el valor a un número
            data = float(data)
            datos = []
            datos.append(data)
            perimetro = CalculoPerimetros(1,datos)
            messagebox.showinfo("Resultado", "El perímetro del cuadrado es: "+str(perimetro))
        except ValueError:
            # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
            messagebox.showerror("Error", "El lado ingresado debe ser un número.")

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()

class PerimetroRectanguloGUI:  
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un rectángulo")
        
        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/5.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un rectángulo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(2):
            self.labels.append(tk.Label(master, text=f"Lado {i+1}:"))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []
        for i in range(2):
            value = self.textboxes[i].get()

            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", f"El lado {i+1} debe ser un número.")
                return

        # Si todos los datos son números, hacer algo con ellos
        perimetro = CalculoPerimetros(2,datos)
        messagebox.showinfo("Resultado", "El perímetro del rectángulo es: "+str(perimetro))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()      
        
class PerimetroTrianguloGUI: 
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un triángulo")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/6.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()
        
        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un triángulo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(3):
            self.labels.append(tk.Label(master, text=f"Lado {i+1}:"))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []

        for i in range(3):
            value = self.textboxes[i].get()

            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", f"El lado {i+1} debe ser un número.")
                return

        # Si todos los datos son números, hacer algo con ellos
        perimetro = CalculoPerimetros(3,datos)
        messagebox.showinfo("Resultado", "El perímetro del triangulo es: "+str(perimetro))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class PerimetroRomboGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un rombo")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/7.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un rombo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar la caja de texto y el botón
        self.label = tk.Label(master, text="Lado: ")
        self.label.pack()

        self.textbox = tk.Entry(master)
        self.textbox.pack()

        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener el valor de la textbox y hacer algo con él
        data = self.textbox.get()
        try:
            # Convertir el valor a un número
            data = float(data)
            datos = []
            datos.append(data)
            perimetro = CalculoPerimetros(4,datos)
            messagebox.showinfo("Resultado", "El perímetro del rombo es: "+str(perimetro))
        except ValueError:
            # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
            messagebox.showerror("Error", "El lado ingresado debe ser un número.")

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class PerimetroPentagonoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un pentágono")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/8.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un pentágono", font=("Arial", 24))
        self.title_label.pack()

        # Agregar la caja de texto y el botón
        self.label = tk.Label(master, text="Lado: ")
        self.label.pack()

        self.textbox = tk.Entry(master)
        self.textbox.pack()

        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener el valor de la textbox y hacer algo con él
        data = self.textbox.get()
        try:
            # Convertir el valor a un número
            data = float(data)
            datos = []
            datos.append(data)
            perimetro = CalculoPerimetros(5,datos)
            messagebox.showinfo("Resultado", "El perímetro del pentágono es: "+str(perimetro))
        except ValueError:
            # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
            messagebox.showerror("Error", "El lado ingresado debe ser un número.")

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class PerimetroHexagonoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un hexágono")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/9.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un hexágono", font=("Arial", 24))
        self.title_label.pack()

        # Agregar la caja de texto y el botón
        self.label = tk.Label(master, text="Lado: ")
        self.label.pack()

        self.textbox = tk.Entry(master)
        self.textbox.pack()

        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener el valor de la textbox y hacer algo con él
        data = self.textbox.get()
        try:
            # Convertir el valor a un número
            data = float(data)
            datos = []
            datos.append(data)
            perimetro = CalculoPerimetros(6,datos)
            messagebox.showinfo("Resultado", "El perímetro del hexágono es: "+str(perimetro))
        except ValueError:
            # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
            messagebox.showerror("Error", "El lado ingresado debe ser un número.")

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class PerimetroCirculoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un círculo")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/10.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un círculo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar la caja de texto y el botón
        self.label = tk.Label(master, text="Radio: ")
        self.label.pack()

        self.textbox = tk.Entry(master)
        self.textbox.pack()

        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener el valor de la textbox y hacer algo con él
        data = self.textbox.get()
        try:
            # Convertir el valor a un número
            data = float(data)
            datos = []
            datos.append(data)
            perimetro = CalculoPerimetros(7,datos)
            messagebox.showinfo("Resultado", "El perímetro del círculo es: "+str(perimetro))
        except ValueError:
            # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
            messagebox.showerror("Error", "El radio ingresado debe ser un número.")

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class PerimetroTrapecioGUI: 
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un trapecio")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/11.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()
        
        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un trapecio", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(3):
            if i == 0:
                texto ="Base mayor:"
            elif i == 1:
                texto = "Base menor:"
            else:
                texto = "Lado:"
            self.labels.append(tk.Label(master, text=texto))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []

        for i in range(3):
            value = self.textboxes[i].get()
            
            if i == 0:
                texto ="La base mayor debe ser un número."
            elif i == 1:
                texto = "La base menor debe ser un número"
            else:
                texto = "El lado debe ser un número"

            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", texto)
                return

        # Si todos los datos son números, hacer algo con ellos
        perimetro = CalculoPerimetros(8,datos)
        messagebox.showinfo("Resultado", "El perímetro del trapecio es: "+str(perimetro))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class PerimetroParalelogramoGUI:  
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del perímetro de un paralelogramo")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/12.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 400), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del perímetro de un paralelogramo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(2):
            if i == 0:
                texto = "Base:"
            else:
                texto = "Lado:"
            self.labels.append(tk.Label(master, text=texto))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []
        for i in range(2):
            value = self.textboxes[i].get()
            
            if i == 0:
                texto = "La base debe ser un número."
            else:
                texto = "El lado debe ser un número."

            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", texto)
                return

        # Si todos los datos son números, hacer algo con ellos
        perimetro = CalculoPerimetros(9,datos)
        messagebox.showinfo("Resultado", "El perímetro del paralelogramo es: "+str(perimetro))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = PerimetroWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()      

#GUI de calculos de áreas
class AreaCuadradoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un cuadrado")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/4.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un cuadrado", font=("Arial", 24))
        self.title_label.pack()

        # Agregar la caja de texto y el botón
        self.label = tk.Label(master, text="Lado: ")
        self.label.pack()

        self.textbox = tk.Entry(master)
        self.textbox.pack()

        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener el valor de la textbox y hacer algo con él
        data = self.textbox.get()
        try:
            # Convertir el valor a un número
            data = float(data)
            datos = []
            datos.append(data)
            Area = CalculoAreas(1,datos)
            messagebox.showinfo("Resultado", "El área del cuadrado es: "+str(Area))
        except ValueError:
            # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
            messagebox.showerror("Error", "El lado ingresado debe ser un número.")

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()

class AreaRectanguloGUI:  
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un rectángulo")
        
        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/5.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un rectángulo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(2):
            self.labels.append(tk.Label(master, text=f"Lado {i+1}:"))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []
        for i in range(2):
            value = self.textboxes[i].get()

            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", f"El lado {i+1} debe ser un número.")
                return

        # Si todos los datos son números, hacer algo con ellos
        Area = CalculoAreas(2,datos)
        messagebox.showinfo("Resultado", "El área del rectángulo es: "+str(Area))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()      
        
class AreaTrianguloGUI: 
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un triángulo")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/6.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()
        
        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un triángulo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(3):
            self.labels.append(tk.Label(master, text=f"Lado {i+1}:"))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []

        for i in range(3):
            value = self.textboxes[i].get()

            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", f"El lado {i+1} debe ser un número.")
                return

        # Si todos los datos son números, hacer algo con ellos
        Area = CalculoAreas(3,datos)
        messagebox.showinfo("Resultado", "El área del triangulo es: "+str(Area))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class AreaRomboGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un rombo")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/7.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un rombo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(2):
            if i == 0:
                texto = "Diagonal mayor:"
            else:
                texto = "Diagonal menor:"
            self.labels.append(tk.Label(master, text=texto))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []
        for i in range(2):
            value = self.textboxes[i].get()
            if i == 0:
                texto = "La diagonal mayor debe ser un número."
            else:
                texto = "La diagonal menor debe ser un número."
            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", texto)
                return

        # Si todos los datos son números, hacer algo con ellos
        Area = CalculoAreas(4,datos)
        messagebox.showinfo("Resultado", "El área del rombo es: "+str(Area))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class AreaPentagonoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un pentágono")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/8.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un pentágono", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(2):
            if i == 0:
                texto = "Perímetro:"
            else:
                texto = "Apotema:"
            self.labels.append(tk.Label(master, text=texto))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []
        for i in range(2):
            value = self.textboxes[i].get()
            if i == 0:
                texto = "El perímetro debe ser un número."
            else:
                texto = "La apotema debe ser un número."
            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", texto)
                return

        # Si todos los datos son números, hacer algo con ellos
        Area = CalculoAreas(5,datos)
        messagebox.showinfo("Resultado", "El área del pentágono es: "+str(Area))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class AreaHexagonoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un hexágono")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/9.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un hexágono", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(2):
            if i == 0:
                texto = "Perímetro:"
            else:
                texto = "Apotema:"
            self.labels.append(tk.Label(master, text=texto))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []
        for i in range(2):
            value = self.textboxes[i].get()
            if i == 0:
                texto = "El perímetro debe ser un número."
            else:
                texto = "La apotema debe ser un número."
            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", texto)
                return

        # Si todos los datos son números, hacer algo con ellos
        Area = CalculoAreas(6,datos)
        messagebox.showinfo("Resultado", "El área del hexágono es: "+str(Area))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class AreaCirculoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un círculo")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/10.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un círculo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar la caja de texto y el botón
        self.label = tk.Label(master, text="Radio: ")
        self.label.pack()

        self.textbox = tk.Entry(master)
        self.textbox.pack()

        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener el valor de la textbox y hacer algo con él
        data = self.textbox.get()
        try:
            # Convertir el valor a un número
            data = float(data)
            datos = []
            datos.append(data)
            Area = CalculoAreas(7,datos)
            messagebox.showinfo("Resultado", "El área del círculo es: "+str(Area))
        except ValueError:
            # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
            messagebox.showerror("Error", "El radio ingresado debe ser un número.")

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class AreaTrapecioGUI: 
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un trapecio")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/11.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()
        
        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un trapecio", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(3):
            if i == 0:
                texto ="Base mayor:"
            elif i == 1:
                texto = "Base menor:"
            else:
                texto = "Altura:"
            self.labels.append(tk.Label(master, text=texto))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []

        for i in range(3):
            value = self.textboxes[i].get()
            
            if i == 0:
                texto ="La base mayor debe ser un número."
            elif i == 1:
                texto = "La base menor debe ser un número"
            else:
                texto = "La altura debe ser un número"

            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", texto)
                return

        # Si todos los datos son números, hacer algo con ellos
        Area = CalculoAreas(8,datos)
        messagebox.showinfo("Resultado", "El perímetro del trapecio es: "+str(Area))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()
        
class AreaParalelogramoGUI:  
    def __init__(self, master):
        self.master = master
        master.title("Cálculo del área de un paralelogramo")

        # Convertir la imagen a un objeto Image de PIL
        self.image = Image.open("C:/Users/aball/Desktop/Proyecto 2/12.jpg")
        
        # Crear una ventana tkinter y mostrar la imagen en un Label
        self.image = self.image.resize((400, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_Label = tk.Label(self.master, image=self.photo)
        self.image_Label.pack()

        # Agregar título
        self.title_label = tk.Label(master, text="Cálculo del área de un paralelogramo", font=("Arial", 24))
        self.title_label.pack()

        # Agregar etiquetas y cajas de texto para los datos
        self.labels = []
        self.textboxes = []

        for i in range(2):
            if i == 0:
                texto = "Base:"
            else:
                texto = "Altura:"
            self.labels.append(tk.Label(master, text=texto))
            self.labels[i].pack()

            self.textboxes.append(tk.Entry(master))
            self.textboxes[i].pack()

        # Agregar botones
        self.accept_button = tk.Button(master, text="Aceptar", command=self.accept_data,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.accept_button.pack()

        self.menu_button = tk.Button(master, text="Volver", command=self.return_to_menu,relief = "groove", borderwidth=3, background="#8B0000", foreground="white",font=("Ubuntu", 9))
        self.menu_button.pack()

    def accept_data(self):
        # Obtener los valores de las cajas de texto y verificar que sean números
        datos = []
        for i in range(2):
            value = self.textboxes[i].get()
            
            if i == 0:
                texto = "La base debe ser un número."
            else:
                texto = "La altura debe ser un número."

            try:
                value = float(value)
                datos.append(value)
            except ValueError:
                # Si el valor no se puede convertir a un número, mostrar un mensaje de error en una ventana emergente
                messagebox.showerror("Error", texto)
                return

        # Si todos los datos son números, hacer algo con ellos
        Area = CalculoAreas(9,datos)
        messagebox.showinfo("Resultado", "El área del paralelogramo es: "+str(Area))

    def return_to_menu(self):
        self.master.destroy()
        # Crear la ventana principal
        ventana = tk.Tk()

        # Crear la GUI
        figuras_gui = AreaWindow(ventana)

        # Mostrar la ventana
        ventana.mainloop()      


#Ejecucion inicial:
       
# Crear la ventana principal
ventana = tk.Tk()

# Crear la GUI
figuras_gui = MainWindow(ventana)

# Mostrar la ventana
ventana.mainloop()