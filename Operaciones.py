from tkinter import filedialog, Tk


PalabrasReservadas = []

def openExtra():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo PXLA",
        initialdir = "./",
        filetypes = (
            ("archivos LFP", "*.pxla"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        print('\nNo se seleccionó ningun archivo')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print('\n"Lectura exitosa"\n')
        texto += "~"
        return texto

#Obtiene la cadena de texto
def purificacionExtra():
    estado = 0
    txtTemp = ""
    columna = 1
    fila = 1
    opcion = True

    text = openExtra()
    #print(text)

    for txt in text:
        opcion = True
        while opcion != False:
            if estado == 0:
                
                if isLetra(txt):
                    txtTemp += txt
                    estado =1
                    opcion = False

                elif isNumero(txt):
                    txtTemp += txt
                    estado =4

                elif ord(txt) == 35: # #
                    txtTemp += txt
                    estado = 5

                elif isSimbolo(txt): 
                    txtTemp += txt
                    estado = 2

                elif ord(txt) == 34: # "
                    txtTemp += txt
                    estado = 3
                    opcion = False

                elif ord(txt) == 64: # @
                    txtTemp += txt
                    estado = 6

                else:

                    if ord(txt) == 32 or ord(txt) == 10 or ord(txt) == 9 or txt == '~':
                        opcion = False
                        pass
                    else: #@
                        print("Error Lexico, se detecto " + txt + " en S0 F,C")

            elif estado == 1:
                opcion = False
                if (isLetra(txt)):
                    txtTemp += txt
                    estado = 1
                
                elif (isNumero(txt)):
                    txtTemp +=   txt
                    estado = 1

                else:
                    print("Se reconocio en S1: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                    txtTemp = ""
                    estado = 0
                    opcion = True

            elif estado == 2:
                print("Se reconocio en S2: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna ))
                txtTemp = ""
                estado = 0
                opcion = False

            elif estado == 3:
                
                if ord(txt) != 34:
                    txtTemp += txt
                    opcion = False
                else:
                    txtTemp += txt
                    print("Se reconocio en S2: '" + txtTemp + "' F: " + str(fila) + ", C: " + str(columna - len(txtTemp)))
                    txtTemp = ""
                    estado = 0
                    opcion = False
              


        # Control de filas y columnas
        # Salto de Linea
        if (ord(txt) == 10):
            columna = 0
            fila += 1
            continue
        # Tab Horizontal
        elif (ord(txt) == 9):
            columna += 4
            continue
        # Espacio
        elif (ord(txt) == 32):
            columna += 1
            continue
        
        columna += 1

    print("///////////////////")
    #print(txtTemp)

def isLetra(txt):
    if((ord(txt) >= 65 and ord(txt) <= 90) or (ord(txt) >= 97 and ord(txt) <= 122) or ord(txt) == 164 or ord(txt) == 165):
        return True
    else:
        return False

def isSimbolo(txt):
    
    if(ord(txt) == 61 or ord(txt) == 59 or ord(txt) == 123 or ord(txt) == 125  or ord(txt) == 91 or ord(txt) == 93):
        return True
    else:
        return False

def isNumero(txt):
    if ((ord(txt) >= 48 and ord(txt) <= 57)):
        return True
    else:
        return False


#Crea la tabla de tokens
def TablaTokens():
    
    global PalabrasReservadas
    PalabrasReservadas = ["TITULO","ANCHO","ALTO","FILAS","COLUMNAS","CELDAS","FILTROS","MIRRORX","MIRRORY","DOUBLEMIRROR","TRUE","FALSE"]
    #print(PalabrasReservadas)
    



    
