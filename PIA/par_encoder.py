import threading
import time
import os

def encodelzw(startindex, endindex, rank):
    global DICTIONARY_SIZE
    string = ''
    compressed_data = []
    data = DATA[startindex:endindex+1]
    print('|' * 10, f'HILO {rank} -> CODIFICANDO {data}')
    for symbol in data:
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
    print('|' * 10, f'RESULTADO DE HILO {rank} -> {compressed_data}')
    RESULT[rank] = compressed_data
    
def format_compressed_data(compressed_data):
    output_string = ''
    for i in range(len(compressed_data)):
        rank = compressed_data[i]
        for j in range(len(compressed_data[i])):
            code = rank[j]
            if j < len(compressed_data[i]) - 1:
                output_string += f'{code},'
            else:
                output_string += str(code)
        if i < len(compressed_data) - 1:
            output_string += '\n'
    return output_string

# GLOBAL
start_time = time.time()
BITS = 9

# LEER ARCHIVO
file = open('data.txt', 'r')
DATA = file.read()
# DICCIONARIO SE INICIALIZA CON 256 CARACTERES ASCII
DICTIONARY_SIZE = pow(2,int(BITS-1))
print('~' * 10, f'INICIALIZANDO DICCIONARIO CON {DICTIONARY_SIZE} CARACTERES ASCII')
#DICTIONARY_SIZE = 65536
DICTIONARY = {chr(i): i for i in range(DICTIONARY_SIZE)}  
# CON 9 BITS SE PUEDE TENER UN DICCIONARIO DE HASTA 512 ESPACIOS

MAXIMUM_SIZE = pow(2,int(BITS))

# PARALELIZACION
P = 4  # NUMERO DE HILOS UTILIZADOS
offset = len(DATA) // P  # CARACTER EXTRA
RESULT = [[] for p in range(P)]  # LISTA DE RESULTADOS DE CADA HILO (BIDIMENSIONAL)

print('~' * 10, 'CODIFICANDO TROZOS DEL STRING EN CADA HILO')
for rank in range(P):
    # CALCULO DE LOS RANGOS DEL STRING PARA CADA HILO
    startindex = rank * offset
    if rank == P - 1:
        endindex = len(DATA) - 1
    else:
        endindex = startindex + offset - 1
        
    # EJECUCION PARALELA DE LA FUNCION DE CODIFICACION
    # CON CADA TROZO DEL STRING POR HILO
    args = (startindex, endindex, rank)
    t = threading.Thread(target=encodelzw, args=args)
    t.start()
    t.join()

print('=' * 10, f'RESULTADO DE LA CODIFICACION: {RESULT}')
print('~' * 10, "TIEMPO DE EJECUCION:  %s " % (round((time.time() - start_time),2)*1000), " Mili-segundos")

    
print('~' * 10, 'GUARDANDO STRING CODIFICADO')
# MOSTRAR Y GUARDAR RESULTADO
output = open('encoded_data.txt', 'w+')
output_string = format_compressed_data(RESULT)
output.write(output_string)
output.close()

decodedFile = os.path.getsize('decoded_data.txt')
encodedFile = os.path.getsize('encoded_data.bin')

sizeE = 0
sizeD = 0 

for i in RESULT:
  for k in i:
    sizeE += k

for j in range(len(DATA)):
  sizeD += ord(DATA[j])

print('~' * 10, 'TAMAÑO DEL ARCHIVO DE-CODIFICADO: ', sizeD, "BITS")
print('~' * 10, 'TAMAÑO DEL ARCHIVO CODIFICADO: ', sizeE, "BITS")


encodedFile = os.path.getsize('encoded_data.txt')
print('~' * 10, 'TAMAÑO DEL ARCHIVO CODIFICADO: ', encodedFile, "Bytes")

#GUARDAR TIEMPO TXT
size = os.path.getsize('data.txt')
output = open('Tiempos/tiempo_pe-%s.txt' % (size), 'w+')
output_string = str(round((time.time() - start_time),2)*1000)
output.write(output_string)
output.close()
