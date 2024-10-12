```bash
 ___  _____  ____   __    ___    ____  ____    __      __        __    ____  __  __  ____  __      __   
/ __)(  _  )(  _ \ /__\  / __)  (  _ \( ___)  (  )    /__\      /__\  (  _ \(  )(  )( ___)(  )    /__\  
\__ \ )(_)(  )___//(__)\ \__ \   )(_) ))__)    )(__  /(__)\    /(__)\  ) _ < )(__)(  )__)  )(__  /(__)\ 
(___/(_____)(__) (__)(__)(___/  (____/(____)  (____)(__)(__)  (__)(__)(____/(______)(____)(____)(__)(__)
```
# :stew: (Sopas de la Abuela) :older_woman:

## :mag: Descripción
Sopas de la Abuela es una aplicación en Python diseñada para generar sopas de letras de manera automática a partir de un archivo de texto con palabras. La aplicación crea archivos PDF en tamaño A4 que contienen una grilla de letras y una lista de palabras a buscar, distribuidas aleatoriamente en distintas direcciones (horizontal, vertical, diagonal, y sus variantes inversas).

Este proyecto está inspirado en mi abuela, que al día del primer commit tiene 90 años. Durante muchos años ha disfrutado de resolver sopas de letras, y esta actividad ha sido clave para mantener su mente activa y su bienestar cognitivo. Para ella, resolver sopas de letras es casi una forma de meditación, una práctica que le ayuda a mantenerse presente en el momento y disfrutar del ahora.

![Captura de pantalla_2024-10-12_15-25-34.png](/screenshots/Captura_de_pantalla_2024-10-12_15-25-34.png)

> [!NOTE]
>El título del proyecto fue generado con arte ASCII en [patorjk.com](https://patorjk.com/software/taag/#p=display&f=Bulbhead&t=Sopas%20de%20la%20Abuela) usando la fuente "Bulbhead".



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
python sopas_abuela.py [archivo_palabras.txt] [cantidad_palabras]
```
- `archivo_palabras.txt`: Es el archivo de texto que contiene las palabras (opcional, por defecto usa `list.txt`).
- `cantidad_palabras`: Número de palabras que se desean en la sopa de letras. Si es 0, usará todas las palabras de la lista. Si es un numero mayor a la cantidad de la lista repetira las primeras.

```bash
python sopas_abuela.py palabras.txt 20
```
Esto generará sopas de letras con 20 palabras de la lista 'palabras.txt'. Si la lista tiene menos palabras, se repetirán para completar las 20.

## :wrench: Personalización
El código es fácilmente modificable para ajustarse a tus necesidades:

- **Cantidad de palabras:** Puedes ajustar cuántas palabras se utilizan por hoja con el segundo argumento en la línea de comandos. Si necesitas una cantidad mayor que las palabras en el archivo, se repetirán automáticamente.
- **Direcciones de las palabras:** Las palabras se distribuyen en las ocho direcciones posibles (horizontal, vertical, diagonal, y sus versiones inversas). Puedes modificar esto en el código si quieres cambiar el comportamiento.
- **Diseño del PDF:** El archivo PDF generado incluye una grilla de letras en mayúsculas, con tipografía grande para facilitar la lectura. Puedes personalizar la fuente, tamaño y diseño general editando el archivo principal.

## :memo: Salida PDF
Cada página del PDF generado contiene:

1. **Encabezado**: Con el título "Sopas de la Abuela".
2. **Subtitulo**: Con el número de la página.
3. **Grilla**: Una grilla de letras mayúsculas donde las palabras se distribuyen aleatoriamente según las opciones de dirección.
4.  **Tabla inferior**: Con las palabras a buscar en la sopa de letras, distribuidas en 4 columnas.

## :older_woman: Créditos
Este proyecto fue creado con amor y dedicación pensando en mi abuela, quien a sus 90 años sigue resolviendo sopas de letras como una forma de mantenerse mentalmente activa y presente en el momento. Para ella, estas sopas son más que un pasatiempo; son una manera de meditar y disfrutar del ahora.

## :ox: Licencia
Este proyecto está bajo la licencia GPL. Puedes ver más detalles en el archivo LICENSE incluido en este repositorio.
