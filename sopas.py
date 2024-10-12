import random
import string
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
import sys

def leer_palabras(archivo):
    """Lee palabras desde un archivo txt, una por línea."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return [line.strip().upper() for line in f.readlines()]
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return []

def generar_sopa(palabras, tam_grilla):
    """Genera la sopa de letras colocando las palabras en distintas direcciones."""
    grilla = [['' for _ in range(tam_grilla)] for _ in range(tam_grilla)]
    
    #SETEAR DIFICULTAD agregando o quitando direcciones de las palabras
    direcciones = [
        'horizontal', 
        'horizontal_inverso', 
        'vertical', 
        'vertical_inverso',
        'diagonal_arriba',        
        'diagonal_abajo'
        
    ]

    '''
    direcciones = [
        'horizontal', 
        'horizontal_inverso', 
        'vertical', 
        'vertical_inverso',
        'diagonal_arriba', 
        'diagonal_arriba_inverso', 
        'diagonal_abajo', 
        'diagonal_abajo_inverso'
    ]
    '''
    
    for palabra in palabras:
        colocada = False
        intentos = 0
        while not colocada and intentos < 100:
            direccion = random.choice(direcciones)
            colocada = colocar_palabra(grilla, palabra, direccion)
            intentos += 1
    
    # Rellenar el resto de la grilla con letras aleatorias
    for i in range(tam_grilla):
        for j in range(tam_grilla):
            if grilla[i][j] == '':
                #----PARA DEBUG ------------------------
                grilla[i][j] = random.choice(string.ascii_uppercase)
                # grilla[i][j] = ' '
    
    return grilla

def colocar_palabra(grilla, palabra, direccion):
    """Intenta colocar la palabra en la grilla en la dirección dada."""
    tam_grilla = len(grilla)
    longitud = len(palabra)
    
    if direccion == 'horizontal':
        fila = random.randint(0, tam_grilla - 1)
        col = random.randint(0, tam_grilla - longitud)
        if all(grilla[fila][col + i] in ['', palabra[i]] for i in range(longitud)):
            for i in range(longitud):
                grilla[fila][col + i] = palabra[i]
            return True
    
    elif direccion == 'horizontal_inverso':
        fila = random.randint(0, tam_grilla - 1)
        col = random.randint(longitud - 1, tam_grilla - 1)
        if all(grilla[fila][col - i] in ['', palabra[i]] for i in range(longitud)):
            for i in range(longitud):
                grilla[fila][col - i] = palabra[i]
            return True
    
    elif direccion == 'vertical':
        fila = random.randint(0, tam_grilla - longitud)
        col = random.randint(0, tam_grilla - 1)
        if all(grilla[fila + i][col] in ['', palabra[i]] for i in range(longitud)):
            for i in range(longitud):
                grilla[fila + i][col] = palabra[i]
            return True
    
    elif direccion == 'vertical_inverso':
        fila = random.randint(longitud - 1, tam_grilla - 1)
        col = random.randint(0, tam_grilla - 1)
        if all(grilla[fila - i][col] in ['', palabra[i]] for i in range(longitud)):
            for i in range(longitud):
                grilla[fila - i][col] = palabra[i]
            return True
    
    elif direccion == 'diagonal_abajo':
        fila = random.randint(0, tam_grilla - longitud)
        col = random.randint(0, tam_grilla - longitud)
        if all(grilla[fila + i][col + i] in ['', palabra[i]] for i in range(longitud)):
            for i in range(longitud):
                grilla[fila + i][col + i] = palabra[i]
            return True
    
    elif direccion == 'diagonal_abajo_inverso':
        fila = random.randint(longitud - 1, tam_grilla - 1)
        col = random.randint(longitud - 1, tam_grilla - 1)
        if all(grilla[fila - i][col - i] in ['', palabra[i]] for i in range(longitud)):
            for i in range(longitud):
                grilla[fila - i][col - i] = palabra[i]
            return True
    
    elif direccion == 'diagonal_arriba':
        fila = random.randint(longitud - 1, tam_grilla - 1)
        col = random.randint(0, tam_grilla - longitud)
        if all(grilla[fila - i][col + i] in ['', palabra[i]] for i in range(longitud)):
            for i in range(longitud):
                grilla[fila - i][col + i] = palabra[i]
            return True
    
    elif direccion == 'diagonal_arriba_inverso':
        fila = random.randint(0, tam_grilla - longitud)
        col = random.randint(longitud - 1, tam_grilla - 1)
        if all(grilla[fila + i][col - i] in ['', palabra[i]] for i in range(longitud)):
            for i in range(longitud):
                grilla[fila + i][col - i] = palabra[i]
            return True
    
    return False

def crear_pdf(archivo_pdf, grillas, palabras_por_pagina, tam_grilla):
    """Genera un PDF con las sopas de letras."""
    pdf = canvas.Canvas(archivo_pdf, pagesize=A4)
    
    for idx, grilla in enumerate(grillas):
        pdf.setFont("Courier", 8)
        # pdf.drawString(50, 800, f"ˎ_ˏ/^\ˎ Sopas de la Abuela ˏ/^\ˎ_ˏ")        
        pdf.drawString(20, 800, f" ___  _____  ____   __    ___    ____  ____    __      __        __    ____  __  __  ____  __      __   ")        
        pdf.drawString(20, 792, f"/ __)(  _  )(  _ \ /__\  / __)  (  _ \( ___)  (  )    /__\      /__\  (  _ \(  )(  )( ___)(  )    /__\  ")        
        pdf.drawString(20, 784, f"\__ \ )(_)(  )___//(__)\ \__ \   )(_) ))__)    )(__  /(__)\    /(__)\  ) _ < )(__)(  )__)  )(__  /(__)\ ")        
        pdf.drawString(20, 776, f"(___/(_____)(__) (__)(__)(___/  (____/(____)  (____)(__)(__)  (__)(__)(____/(______)(____)(____)(__)(__)")                  
        pdf.setFont("Courier", 16)
        pdf.drawString(380, 750, f"[Sopa de Letras #{idx + 1}]")
        
        # Dibujar la grilla
        x_offset = 80
        y_offset = 650
        for i, fila in enumerate(grilla):
            for j, letra in enumerate(fila):
                pdf.drawString(x_offset + j * 15, y_offset - i * 15, letra)
        
        # Dibujar las palabras debajo
        y_offset = 100
        pdf.setFont("Helvetica", 14)
        palabras_tabla = palabras_por_pagina[idx]
        tabla = Table([palabras_tabla[i:i + 4] for i in range(0, len(palabras_tabla), 4)], colWidths=4 * [4 * cm])
        tabla.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
        tabla.wrapOn(pdf, 100, y_offset)
        tabla.drawOn(pdf, 50, y_offset)
        
        pdf.showPage()
    
    pdf.save()
def ajustar_lista_palabras(palabras, cantidad):
    """
    Ajusta la lista de palabras según el número dado.
    Si cantidad es 0, se toma la lista tal cual.
    Si cantidad es mayor a la longitud de la lista, se repiten las palabras desde el inicio.
    """
    if cantidad == 0:
        return palabras  # Toma la lista tal cual
    else:
        # Repetimos las palabras si es necesario hasta llegar a la cantidad deseada
        palabras_repetidas = []
        while len(palabras_repetidas) < cantidad:
            palabras_repetidas.extend(palabras)
        # Devolvemos exactamente la cantidad solicitada
        return palabras_repetidas[:cantidad]
#--------------MAIN (CONFIGURACION)-------------------
def main(archivo_palabras='list.txt', tam_grilla=20, palabras_por_hoja=20,pdf_salida='sopa_de_letras.pdf', cant_palabras=0):
    #----CONFIG------
    tam_grilla=27
    #palabras_por_hoja=20
    # pdf_salida='sopa_de_letras.pdf'
    cant_palabras = 400 #0: toma la lista tal cual, otro numero si es necesario repite

    #----parametros externos
    args = sys.argv
    archivo_palabras = args[1] if args[1] else archivo_palabras
    tam_grilla = int(args[2]) if args[2] else tam_grilla
    palabras_por_hoja = int(args[3]) if args[3] else palabras_por_hoja
    pdf_salida = args[4] if args[4] else pdf_salida
    print(args)

    palabras = leer_palabras(archivo_palabras)
    palabras = ajustar_lista_palabras(palabras, cant_palabras)
    if not palabras:
        return

    grillas = []
    palabras_en_hojas = []
    
    for i in range(0, len(palabras), palabras_por_hoja):
        sub_lista = palabras[i:i + palabras_por_hoja]
        grilla = generar_sopa(sub_lista, tam_grilla)
        grillas.append(grilla)
        palabras_en_hojas.append(sub_lista)
    
    crear_pdf(pdf_salida, grillas, palabras_en_hojas, tam_grilla)
    print("PDF generado con éxito")

if __name__ == "__main__":
    main()

