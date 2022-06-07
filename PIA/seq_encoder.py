import threading
import time
import os

def encodelzw(startindex, endindex, rank):
    global DICTIONARY_SIZE
    string = ''
    compressed_data = []
    DATA
    print('|' * 10, f'MODULO SECUENCIAL -> CODIFICANDO {DATA}')
    for symbol in DATA:
        string_plus_symbol = string + symbol
        if string_plus_symbol in DICTIONARY:
            string = string_plus_symbol
        else:
            compressed_data.append(DICTIONARY[string])
            if len(DICTIONARY) <= MAXIMUM_SIZE:
                DICTIONARY[string_plus_symbol] = DICTIONARY_SIZE
                DICTIONARY_SIZE += 1
            string = symbol
    if string in DICTIONARY:
        compressed_data.append(DICTIONARY[string])
    RESULT = compressed_data
    return RESULT

def format_compressed_data(compressed_data):
    output_string = ''
    for j in range(len(compressed_data)):
        if j < len(compressed_data) - 1:
            output_string += f"{compressed_data[j]}, "
        else:
            output_string += str(compressed_data[j])
    return output_string

def format_bin_compressed_data(compressed_data):
    output_string = ''
    for j in range(len(compressed_data)):
        if j < len(compressed_data) - 1:
            output_string += str(compressed_data[j])
        else:
            output_string += str(compressed_data[j])
    return output_string

start_time = time.time()

BITS = 9

# GLOBAL
# LEER ARCHIVO
file = open('data.txt', 'r')
DATA = file.read()

# DICCIONARIO SE INICIALIZA CON 256 CARACTERES ASCII O UTC2
DICTIONARY_SIZE = pow(2,int(BITS-1))
print('~' * 10, f'INICIALIZANDO DICCIONARIO CON {DICTIONARY_SIZE} CARACTERES ASCII')
#DICTIONARY_SIZE = 65536

DICTIONARY = {chr(i): i for i in range(DICTIONARY_SIZE)}  
# CON 9 BITS SE PUEDE TENER UN DICCIONARIO DE HASTA 512 ESPACIOS

MAXIMUM_SIZE = pow(2,int(BITS))


RESULT = encodelzw(1, len(DATA), 0)


print('=' * 10, f'RESULTADO DE LA CODIFICACION: {RESULT}')
print('~' * 10, "TIEMPO DE EJECUCION:  %s " % (round((time.time() - start_time),2)*1000), " Mili-segundos")


    
print('~' * 10, 'GUARDANDO STRING CODIFICADO')
# MOSTRAR Y GUARDAR RESULTADO
output = open('encoded_data.txt', 'w+')
output_string = format_compressed_data(RESULT)
output.write(output_string)
output.close()

output = open('encoded_data.bin', 'w+')
output_string = format_bin_compressed_data(RESULT)
output.write(output_string)
output.close()

decodedFile = os.path.getsize('decoded_data.txt')
encodedFile = os.path.getsize('encoded_data.bin')

sizeE = 0
sizeD = 0 
for i in RESULT:
  sizeE += i

for j in range(len(DATA)):
  sizeD += ord(DATA[j])

print('~' * 10, 'TAMAÑO DEL ARCHIVO DE-CODIFICADO: ', sizeD, "BITS")
print('~' * 10, 'TAMAÑO DEL ARCHIVO CODIFICADO: ', sizeE, "BITS")

radioCompresion = sizeE/sizeD
print('~' * 10, 'RADIO DE COMPRESION: ', radioCompresion, " BITS/SIMBOLO")

#GUARDAR TIEMPO TXT
size = os.path.getsize('data.txt')
output = open('Tiempos/tiempo_se-%s.txt' % (size), 'w+')
output_string = str(round((time.time() - start_time),2)*1000)
output.write(output_string)
output.close()
