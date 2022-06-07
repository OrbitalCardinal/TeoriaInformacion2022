import threading
import time
import os

def decodelzw(compressed_data, rank):
    global NEXT_CODE
    decompressed_data = []
    string = ''
    print('|' * 10, f'HILO {rank} DECODIFICANDO -> {compressed_data}')
    for code in compressed_data:
        if code not in DICTIONARY:
            DICTIONARY[code] = string + (string[0])
        decompressed_data += DICTIONARY[code]
        if not(len(string) == 0):
            DICTIONARY[NEXT_CODE] = string + (DICTIONARY[code][0])
            NEXT_CODE += 1
        string = DICTIONARY[code]
    print('=' * 10, f'RESULTADO HILO {rank}  -> {decompressed_data}')
    DECODE_RESULT[rank] = decompressed_data
    
def parse_compressed_data(compressed_data):
    compressed_data = [i.split(',') for i in compressed_data.split('\n')]
    for i in range(len(compressed_data)):
        for j in range(len(compressed_data[i])):
            compressed_data[i][j] = int(compressed_data[i][j])
    return compressed_data

def open_compressed_data(file):
    file = open(file, 'r')
    compressed_data = file.read()
    parsed_compressed_data = parse_compressed_data(compressed_data)
    return parsed_compressed_data

# Paralelizar decodificacion
start_time = time.time()
BITS = 17

print('~' * 10, 'ABRIENDO ARCHIVO DE CODIFICACION')
RESULT = open_compressed_data('encoded_data.txt')
print('~' * 10, 'INICIALIZANDO DICCIONARIO CON 256 CARACTERES ASCII')
DICTIONARY_SIZE = pow(2,int(BITS-1))
DICTIONARY = dict([(x, chr(x)) for x in range(DICTIONARY_SIZE)])

MAXIMUM_SIZE = pow(2,int(BITS)) 
NEXT_CODE = 256

P = 4
DECODE_RESULT = [[] for p in range(P)]
print('~' * 10, f'UTILIZANDO {P} HILOS')

for rank in range(P):
    # Ejecutar en paralelo
    args = (RESULT[rank], rank)
    t = threading.Thread(target=decodelzw, args=args)
    t.start()
    t.join()

print('~' * 10, 'UNIFICANDO RESULTADOS DECODIFICADOS')
DECODE_RESULT = ''.join(sum(DECODE_RESULT, []))
print('~' * 10, f'RESULTADO FINAL DE DECODIFICACION => {DECODE_RESULT}')
print('~' * 10, "TIEMPO DE EJECUCION:  %s " % (round((time.time() - start_time),2)*1000), " Mili-segundos")

print('~' * 10, 'GUARDANDO DE CODIFICACION')
output_file = open('decoded_data.txt', 'w+')
output_file.write(DECODE_RESULT)
output_file.close()

decodedFile = os.path.getsize('decoded_data.txt')
print('~' * 10, 'TAMAÑO DEL ARCHIVO CODIFICADO: ', decodedFile, "BYTES")

#GUARDAR TIEMPO TXT
size = os.path.getsize('data.txt')
output = open('Tiempos/tiempo_pd-%s.txt' % (size), 'w+')
output_string = str(round((time.time() - start_time),2)*1000)
output.write(output_string)
output.close()