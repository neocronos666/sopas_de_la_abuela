import random
import string
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.units import cm
import sys
import re


def leer_palabras(archivo):
    """Lee palabras desde un archivo txt, una por línea."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            # return [line.strip().upper() for line in f.readlines()]
            # return [re.sub(r'[^A-Za-z\n]', '', line.strip().upper()) for line in f.readlines()]
            return [re.sub(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\n]', '', line.strip().upper()) for line in f.readlines()]
    except FileNotFoundError:
        print(f"Archivo no encontrado.({archivo})")
        return []

def generar_sopa(palabras, tam_grilla, fondo = True):
    """Genera la sopa de letras colocando las palabras en distintas direcciones."""
    grilla = [['' for _ in range(tam_grilla)] for _ in range(tam_grilla)]
    # ==========================================================
    #SETEAR DIFICULTAD agregando o quitando direcciones de las palabras
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
    # ==========================================================
    ''' ----PLANTILLA----
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
                if fondo:
                    grilla[i][j] = random.choice(string.ascii_uppercase)
                else:              
                    grilla[i][j] = ' '    
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

def crear_pdf(archivo_pdf, grillas, palabras_por_pagina, tam_grilla, columnas = True):
    """Genera un PDF con las sopas de letras."""
    pdf = canvas.Canvas(archivo_pdf, pagesize=A4)
    
    for idx, grilla in enumerate(grillas):
        
        #------Dibujar Encabezado-----
        pdf.setFont("Courier", 8)
        # pdf.drawString(50, 800, f"ˎ_ˏ/^\ˎ Sopas de la Abuela ˏ/^\ˎ_ˏ")        
        pdf.drawString(40, 800, r' ___  _____  ____   __    ___    ____  ____    __      __        __    ____  __  __  ____  __      __   ')        
        pdf.drawString(40, 792, r'/ __)(  _  )(  _ \ /__\  / __)  (  _ \( ___)  (  )    /__\      /__\  (  _ \(  )(  )( ___)(  )    /__\  ')        
        pdf.drawString(40, 784, r'\__ \ )(_)(  )___//(__)\ \__ \   )(_) ))__)    )(__  /(__)\    /(__)\  ) _ < )(__)(  )__)  )(__  /(__)\ ')        
        pdf.drawString(40, 776, r'(___/(_____)(__) (__)(__)(___/  (____/(____)  (____)(__)(__)  (__)(__)(____/(______)(____)(____)(__)(__)')                  
        pdf.setFont("Courier", 16)
        pdf.drawString(380, 750, f"[Sopa de Letras #{idx + 1}]")
        pdf.drawString(40, 750, 'Tema: ' + archivo_pdf.split('/')[-1].split('.')[0])
        
        #-------Dibujar la grilla-----
        x_offset = 50
        y_offset = 720
        for i, fila in enumerate(grilla):
            for j, letra in enumerate(fila):
                pdf.drawString(x_offset + j * 15, y_offset - i * 15, letra)
        #------Dibujar Creditos--------
        pdf.setFont("Courier", 10)
        pdf.drawString(40, 810, 'https://github.com/neocronos666/sopas_de_la_abuela')                  

        #------Dibujar tabla ----------
        x_offset = 20
        y_offset = 70
        pdf.setFont("Helvetica", 14)
        palabras_tabla = palabras_por_pagina[idx]
        if columnas:
            cant_cols=5            
            
            tabla = Table([palabras_tabla[i:i + cant_cols] for i in range(0, len(palabras_tabla), cant_cols)], colWidths=4 * [4 * cm])
            tabla.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT')]))
            tabla.wrapOn(pdf, 100, y_offset)
            tabla.drawOn(pdf, 20, y_offset)
        else:
            elementos = []
            styles = getSampleStyleSheet()
            tag_string = " | ".join(palabras_tabla)
            parrafo = Paragraph(tag_string, style=styles['Normal'])
            elementos.append(parrafo)
            parrafo.wrapOn(pdf, 500, y_offset)
            parrafo.drawOn(pdf, 50, y_offset)
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
def main(archivo_palabras='list.txt', tam_grilla=20, palabras_por_hoja=20,pdf_salida='sopa_de_letras.pdf', cant_palabras=0):
    # ===============CONFIGURACION==============================
    archivo_palabras='./lists/castellano.txt'
    tam_grilla=32 
    palabras_por_hoja=60 
    pdf_salida='./PDFs/241024 Castellano.pdf'
    cant_palabras = 2000 #0: toma la lista tal cual, otro numero si es necesario repite
    generar_fondo=True  #T: Genera letras aleatorias de fondo; F:no
    en_columnas = False #T: Muestra las referencias en columnas F:las muestra en parrafo
    # ==========================================================
    #----parametros externos
    args = sys.argv
    archivo_palabras = args[1] if len(args) > 1 and args[1] else archivo_palabras
    tam_grilla = int(args[2]) if len(args) > 2 and args[2] else tam_grilla
    palabras_por_hoja = int(args[3]) if len(args) > 3 and args[3] else palabras_por_hoja
    pdf_salida = args[4] if len(args) > 4 and args[4] else pdf_salida
    # print(args)

    palabras = leer_palabras(archivo_palabras)
    palabras = ajustar_lista_palabras(palabras, cant_palabras)
    if not palabras:
        return
    grillas = []
    palabras_en_hojas = []    
    for i in range(0, len(palabras), palabras_por_hoja):
        sub_lista = palabras[i:i + palabras_por_hoja]
        grilla = generar_sopa(sub_lista, tam_grilla,generar_fondo)
        grillas.append(grilla)
        palabras_en_hojas.append(sub_lista)    
    crear_pdf(pdf_salida, grillas, palabras_en_hojas, tam_grilla, en_columnas)
    print(f"PDF generado con éxito: \'{pdf_salida}\'")

if __name__ == "__main__":
    main()

