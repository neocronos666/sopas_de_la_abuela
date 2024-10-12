#!/bin/bash
clear
# Mostrar arte ASCII
echo " ___  _____  ____   __    ___    ____  ____    __      __        __    ____  __  __  ____  __      __   "
echo "/ __)(  _  )(  _ \ /__\  / __)  (  _ \( ___)  (  )    /__\      /__\  (  _ \(  )(  )( ___)(  )    /__\  "
echo "\__ \ )(_)(  )___//(__)\ \__ \   )(_) ))__)    )(__  /(__)\    /(__)\  ) _ < )(__)(  )__)  )(__  /(__)\ "
echo "(___/(_____)(__) (__)(__)(___/  (____/(____)  (____)(__)(__)  (__)(__)(____/(______)(____)(____)(__)(__)"
echo ""
echo "Bienvenido a Sopas de la Abuela"
echo "Siga las instrucciones para continuar, deje en blanco para salir"

# Preguntar por las variables
read -p "Ingrese el archivo de palabras (ej: list.txt): " archivo_palabras
[ -z "$archivo_palabras" ] && echo "Finalizando script." && exit 1

read -p "Ingrese el tamaño de la grilla (ej: 27): " tam_grilla
[ -z "$tam_grilla" ] && echo "Finalizando script." && exit 1

read -p "Ingrese la cantidad de palabras por hoja (ej: 20): " palabras_por_hoja
[ -z "$palabras_por_hoja" ] && echo "Finalizando script." && exit 1

read -p "Ingrese el nombre del archivo PDF de salida (ej: salida.pdf): " pdf_salida
[ -z "$pdf_salida" ] && echo "Finalizando script." && exit 1

read -p "Ingrese la cantidad de lineas a usar de la lista (Escribir 0 para usar todas)" cant_palabras
[ -z "$pdf_salida" ] && echo "Finalizando script." && exit 1


# Ejecutar el comando de Python
echo "Ejecutando el programa..."
python sopas.py "$archivo_palabras" "$tam_grilla" "$palabras_por_hoja" "$pdf_salida" "$cant_palabras"
clear
# Comprobar si se ejecutó correctamente
if [ $? -eq 0 ]; then
    echo "El programa se ejecutó con éxito."
else
    echo "Hubo un error al ejecutar el programa, compruebe que el archivo de lista de palabras exista y que no haya usado un caracter que no sea un numero para el tamaño de la grilla y cantidad de palabras."
fi
