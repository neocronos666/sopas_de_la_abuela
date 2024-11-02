import os
import random

def merge_dicc(min_length, max_length, sort_output,input_dir,output_file):
    
   
    processed_words = set()

    # Leer archivos en el directorio
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # Omitir líneas que comienzan con "-"
                    if line.startswith('-'):
                        continue
                    
                    # Limpiar palabra: quitar espacios, convertir a minúsculas
                    word = line.strip().lower()
                    
                    # Si contiene una coma, tomar la parte izquierda
                    if ',' in word:
                        word = word.split(',')[0]
                    
                    # Omitir palabras que contengan números
                    if any(char.isdigit() for char in word):
                        continue
                    
                    # Verificar tamaño de la palabra
                    word_length = len(word)
                    if word_length >= min_length and (max_length == 0 or word_length <= max_length):
                        processed_words.add(word)
    
    # Convertir a lista para ordenar o aleatorizar
    processed_words = list(processed_words)
    if sort_output:
        processed_words.sort()
    else:
        random.shuffle(processed_words)
    
    # Guardar palabras procesadas en el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as output:
        for word in processed_words:
            output.write(word + '\n')

# ------SETUP---------------------------
input_dir = './lists/RAE/'              # Directorio de donde toma los txt
output_file = './lists/rae.txt'         # Arrchivo de Salida
sort_output=False                       # T: Ordena la lista | F:La randomiza
min_length=5                            # Minimo Tamaño de palabras
max_length=0                            # Maximo Tamaño (0 toma todas)
# --------------------------------------
merge_dicc(min_length,max_length,sort_output,input_dir,output_file)
