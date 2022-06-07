import threading
import time
import os

def decodelzw(compressed_data):
    global NEXT_CODE
    decompressed_data = []
    string = ''
    print('|' * 10, f'DECODIFICANDO STRING SECUENCIAL -> {compressed_data}')
    for code in compressed_data:
        if code not in DICTIONARY:
            DICTIONARY[code] = string + (string[0])
        decompressed_data += DICTIONARY[code]
        if not(len(string) == 0):
            DICTIONARY[NEXT_CODE] = string + (DICTIONARY[code][0])
            NEXT_CODE += 1
        string = DICTIONARY[code]
    return decompressed_data

def open_compressed_data(file):
    file = open(file, 'r')
    compressed_data = file.read()
    parsed_compressed_data = parse_compressed_data(compressed_data)
    return parsed_compressed_data

def parse_compressed_data(compressed_data):
    compressed_data = [i.split(',') for i in compressed_data.split('\n')]
    for i in range(len(compressed_data)):
        for j in range(len(compressed_data[i])):
            compressed_data[i][j] = int(compressed_data[i][j])
    return compressed_data[0]

def format_decompressed_data(compressed_data):
    output_string = ''
    for j in range(len(compressed_data)):
        if j < len(compressed_data) - 1:
            output_string += f"{compressed_data[j]}"
        else:
            output_string += str(compressed_data[j])
    return output_string

# Decodificacion secuencial
start_time = time.time()
BITS = 9
DICTIONARY_SIZE = pow(2,int(BITS-1))
MAXIMUM_SIZE = pow(2,int(BITS)) 
NEXT_CODE = DICTIONARY_SIZE

print('~' * 10, 'ABRIENDO ARCHIVO DE CODIFICACION')
RESULT = open_compressed_data('encoded_data.txt')
print('~' * 10, f'INICIALIZANDO DICCIONARIO CON {DICTIONARY_SIZE} CARACTERES')
DICTIONARY = dict([(x, chr(x)) for x in range(DICTIONARY_SIZE)])

DECODE_RESULT = list()
DECODE_RESULT = decodelzw(RESULT)

print('~' * 10, 'UNIFICANDO RESULTADOS DECODIFICADOS')
print('~' * 10, f'RESULTADO FINAL DE DECODIFICACION => {DECODE_RESULT}')
print('~' * 10, 'GUARDANDO DE CODIFICACION')
print('~' * 10, "TIEMPO DE EJECUCION:  %s " % (round((time.time() - start_time),2)*1000), " Mili-segundos")
output_file = open('decoded_data.txt', 'w+')

decoded = format_decompressed_data(DECODE_RESULT)
output_file.write(decoded)
output_file.close()

decodedFile = os.path.getsize('decoded_data.txt')
encodedFile = os.path.getsize('encoded_data.txt')

print('~' * 10, 'TAMAÑO DEL ARCHIVO CODIFICADO: ', encodedFile)
print('~' * 10, 'TAMAÑO DEL ARCHIVO DE-CODIFICADO: ', decodedFile)

#GUARDAR TIEMPO TXT
size = os.path.getsize('data.txt')
output = open('Tiempos/tiempo_sd-%s.txt' % (size), 'w+')
output_string = str(round((time.time() - start_time),2)*1000)
output.write(output_string)
output.close()