# -*- coding: utf-8 -*-
"""
Created on Sat May 14 22:44:19 2022

@author: ldgar
"""

from os import path 
pathTest = path.exists('encoded.txt') == True

# Se valida que el archivo este creado
if( path.exists('encoded.txt') == False):
    f = open("encoded.txt", "x")
    x = input("Archivo a codificar no existe, ingrese un string: ")
    f = open("encoded.txt", "a")
    f.write(x)
    f.close()
        

with open('encoded.txt') as f:
    contents = f.read()
    
print(contents)


lines = []
values = []
with open('dictionary.txt') as f:
    lines = f.readlines()
    
    


dictionaries = []
count = 0
for line in lines:
    count += 1
    i = list(line.split(" "))
    dictionaries.append(i)
    
    values.append(line)
    
    
print("values: ", dictionaries)


textfile = open("decoded.txt", "w")


dictionaryString = dictionaries[0]
dictionaryString.pop()
dictionaryIndex = dictionaries[1]
maxLenght = dictionaries[2][0]
print(maxLenght)


i = 0

while i < len(contents):
    for j in range(len(dictionaryString)):
        print(contents[i:i + int(maxLenght)], " oooooh   ", dictionaryIndex[j])
        if(contents[i:i +int(maxLenght)] == dictionaryIndex[j]):
            print("siii", dictionaryString[j])
            textfile.write(dictionaryString[j])
    i += int(maxLenght)
            
    
    

print(i)
    

