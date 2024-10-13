```bash
 ___  _____  ____   __    ___    ____  ____    __      __        __    ____  __  __  ____  __      __   
/ __)(  _  )(  _ \ /__\  / __)  (  _ \( ___)  (  )    /__\      /__\  (  _ \(  )(  )( ___)(  )    /__\  
\__ \ )(_)(  )___//(__)\ \__ \   )(_) ))__)    )(__  /(__)\    /(__)\  ) _ < )(__)(  )__)  )(__  /(__)\ 
(___/(_____)(__) (__)(__)(___/  (____/(____)  (____)(__)(__)  (__)(__)(____/(______)(____)(____)(__)(__)
```
# :stew: (Sopas de la Abuela) :older_woman:

## :mag: Descripción
`Sopas de la Abuela` es una aplicación en Python diseñada para generar sopas de letras de manera automática a partir de un archivo de texto con palabras. La aplicación crea archivos PDF en tamaño A4 que contienen una grilla de letras y una lista de palabras a buscar, distribuidas aleatoriamente en distintas direcciones (horizontal, vertical, diagonal, y sus variantes inversas).

Este proyecto está inspirado en mi abuela, que al día del primer commit tiene 90 años. Durante muchos años ha disfrutado de resolver sopas de letras, y esta actividad ha sido clave para mantener su mente activa y su bienestar cognitivo. Para ella, resolver sopas de letras es casi una forma de meditación, una práctica que le ayuda a mantenerse presente en el momento y disfrutar del ahora.

![Captura_de_pantalla_2024-10-12_22-23-22.png](/screenshots/Captura_de_pantalla_2024-10-12_22-23-22.png)


## :bulb: Características
- Generación automática de sopas de letras a partir de un archivo .txt.
- Las palabras pueden colocarse en las siguientes direcciones:
  - Horizontal (normal e inversa)
  - Vertical (normal e inversa)
  - Diagonal (hacia arriba y hacia abajo, normal e inversa)
- Soporte para personalización de cantidad de palabras en la sopa de letras.
- Si se solicita una cantidad mayor de palabras que las disponibles, las palabras se repiten para completar.
- La salida es un archivo PDF con un diseño claro y fácil de leer:
  - Encabezado con el título.
  - Grilla con letras grandes en mayúsculas.
  - Tabla inferior con las palabras a buscar.
  - Pie de página con el número de página.
---

## :arrow_heading_down: Instalación

### Requisitos previos

Asegúrate de tener instalado Python 3 en tu sistema. Si no lo tienes, puedes instalarlo desde [aquí](https://www.python.org/downloads/).

También necesitas instalar algunas dependencias adicionales:

```bash
pip install reportlab Pillow
```
### Clonar el repositorio
Para comenzar, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/neocronos666/sopas-de-la-abuela.git
cd sopas-de-la-abuela
```

## :video_game:  Uso
Puedes ejecutar la aplicación desde la línea de comandos. El programa toma un archivo de texto con una palabra por línea y genera un archivo PDF con la sopa de letras.

### Comandos básicos
```bash
python sopas_abuela.py [archivo_palabras.txt] [tam_grilla] [cantidad_palabras] [pdf_salida] [cant_palabras] [en_columnas]
```


- `archivo_palabras.txt`: Es el archivo de texto que contiene las palabras (opcional, por defecto usa `list.txt`).
- `tam_grilla` : Es el tamaño (filas y columnas) totales de la sopa de letras.
- `cantidad_palabras`: Número de palabras que se desean en la sopa de letras. Si es 0, usará todas las palabras de la lista. Si es un numero mayor a la cantidad de la lista repetira las primeras.
- `pdf_salida`: Nombre del archivo de salida
- `cant_palabras` : Este numero determina cuantas palabras se van a utilizar, si se deja en 0, se toman todas las palabras de la lista, si se elije un numero menor se corta la lista, pero si se elije un numero mayor la lista continua desde el principio tanto como sea necesario.
- `en_columnas`: `True` = Muestra las referencias en columnas `False`:las muestra en parrafo (util para palabras largas que se tocan entre columnas)


### Ejemplo de uso
```bash
python sopas.py palabras.txt 27 20 salida.pdf 0
```
Esto generará una archivo PDF llamado `salida.pdf`en la misma ubicacion que `sopas.py`conteniendo una sopas de letras de 27x27 casillas con 20 palabras de la lista `palabras.txt`. 

Notese que hay una sopa de letras por hoja y la cantidad de hojas que tendra el documento está dada por el cociente de la cantidad de lineas de `archivo_palabras.txt` y `cantidad_palabras` o sea que si hay 100 lineas en el archivo, 20 por hoja, 100/20=5 , el documento tendra 5 hojas.

### Frontend Bash
Tambien existe un script de bash que funciona como frontend, sigue siendo por linea de comandos pero es mas amigable que usar el `.py`directamente, debe ejecutarse lo siguiente:

```bash
bash crear_sopas.sh
```
Otra forma de correrlo es:

```bash
chmod +x ejecutar_sopas.sh
./crear_sopas.sh
```
Se vera algo asi:

![Captura_de_pantalla_2024-10-12_16-50-59.png](/screenshots/Captura_de_pantalla_2024-10-12_16-50-59.png)

## :wrench: Personalización
Para poder personalizar aun más el archivo es necesario modificar el codigo fuente. No se preocupe, está claramente indicado donde se puede modificar para personalizarlo.
Luego de modificarlo puede correr el frontend o simplemente correr el script `sopas.py` desde su editor sin ningun parametro adicional, para que tome los valores por defecto configurados cuando editó el archivo.

### Dificultad:
Para setear la dificultad debe encontrar el siguiente bloque:
```python
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
```
Puede editarla o comentyarla para que hayan menos direcicones en las que aparecen las palabras, o para que no hayan inversas, etc.

### Parametros
Debería buscar la funcion main para setear los ajustes por defecto:
```python
def main(archivo_palabras='list.txt', tam_grilla=20, palabras_por_hoja=20,pdf_salida='sopa_de_letras.pdf', cant_palabras=0):
     # ===============CONFIGURACION==============================
    archivo_palabras = './lists/varios.txt'
    tam_grilla = 32 
    palabras_por_hoja = 40 
    pdf_salida = './PDFs/varios.pdf'
    cant_palabras = 800 #0: toma la lista tal cual, otro numero si es necesario repite
    generar_fondo = True  #T: Genera letras aleatorias de fondo; F:no
    en_columnas = False #T: Muestra las referencias en columnas F:las muestra en parrafo
    # ==========================================================
```
Las cuatro lineas debajo de `-CONFIG-`pueden ser editadas para tomar esos valores siempre sin tener que especificarlos por comandos, incluso una vez establecidos se puede correr sin parametros `sopas.py`y tomará esos valores  

## :memo: Salida PDF
Cada página del PDF generado contiene:

1. **Encabezado**: Con el título "Sopas de la Abuela".
2. **Subtitulo**: Con el número de la página.
3. **Grilla**: Una grilla de letras mayúsculas donde las palabras se distribuyen aleatoriamente según las opciones de dirección.
4.  **Tabla inferior**: Con las palabras a buscar en la sopa de letras, distribuidas en 4 columnas.


## :older_woman: Créditos
Este proyecto fue creado por [Sergio Silvstri](https://github.com/neocronos666) con amor y dedicación pensando en mi abuela, quien a sus 90 años sigue resolviendo sopas de letras como una forma de mantenerse mentalmente activa y presente en el momento. Para ella, estas sopas son más que un pasatiempo; son una manera de meditar y disfrutar del ahora.

# :muscle: Creditos a terceros
- El título del proyecto fue generado con arte ASCII en [patorjk.com](https://patorjk.com/software/taag/#p=display&f=Bulbhead&t=Sopas%20de%20la%20Abuela) usando la fuente "Bulbhead".
- La lista `castellano.txt`la tomé prestada de [elcastellano.org](https://www.elcastellano.org/lista_alfabetica)
- Las listas `campo.txt`, `memorias.txt`, `naturaleza.txt` y `varios.txt` las generé usando ChatGPT4.o.


## :ox: Licencia
Este proyecto está bajo la licencia GPL. Puedes ver más detalles en el archivo [LICENSE](LICENSE) incluido en este repositorio.

