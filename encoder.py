# Global variables
position = []
sequence = []
numeralRep =[]

from os import path 
pathTest = path.exists('decoder.txt') == True

# Se valida que el archivo este creado
if( path.exists('decodedString.txt') == False):
    f = open("decodedString.txt", "x")
    x = input("Archivo a codificar no existe, ingrese un string: ")
    f = open("decodedString.txt", "a")
    f.write(x)
    f.close()

f = open("decodedString.txt", "r")
decodedString = f.readlines()[0]

sequence = ['<']
para = 0
for i in range(len(decodedString)):
    print("valor de i = ", i)
    if decodedString[i] in sequence:
        for k in range(len(decodedString)+1):
            if k > i:
                print(decodedString[i:k], "i:", i , "k",k)
                if decodedString[i:k] in sequence:
                    print(decodedString[i:k], "esta en", sequence)
                else:
                    sequence.append(decodedString[i:k])
                    i = k
                    para = k
                    print("decoded striiin", len(decodedString))
                    print(k)
                    if(k == len(decodedString)):
                        break
                    
                    print("valor de i =", i)
                print("valor de i = ", i)

    else:
        sequence.append(decodedString[i])
    print("valor de i = ", i)
    
    if(para == len(decodedString)):
        sequence.pop(0)
        print(sequence)
        break
f.close()



for i in range(len(sequence)):
    for j in range(len(sequence)):
        compareI = sequence[i]
        compareJ = sequence[j]
        #print(i, j)
        #print("compare I ", compareI, " compare J ", compareJ)
        #print("Si", compareI[1:len(compareI)], "es igual a ", compareJ)
        if(compareI[1:len(compareI)] == compareJ and len(compareI)-1 != 0):
            numeralRep.append(str(j+1) + compareI[len(compareI)-1] )
            break

        else:
            if(len(compareI)-1 == 0 and len(sequence) != i):
                numeralRep.append("0" + compareI)
                break
            else:
                #print(i, j)
                #print(compareI)
                #print("Sii", compareI[0], "es igual a ", compareJ)
                if(compareI[0] == compareJ and len(compareI)-1 != 0):
                    numeralRep.append(str(j+1) + compareI[len(compareI)-1])
                    
codedList = []
codedString = []
j = 0

for i in range(len(numeralRep)):
     compareI = numeralRep[i]
     print(compareI[0])
     if(compareI[0] == "0"):
         #print("holaaaa")
         codedList.append(j)
         codedString.append(compareI[-1])
         j += 1

i=0
for i in range(len(numeralRep)):
     compareI = numeralRep[i]
     if(compareI[0] != "0"):
         print(compareI)
         #print("Hola", compareI[1:])
         for j in range(len(codedList)):
             print(i)
             print(codedString)
             if(compareI[1:] == codedString[j]):
                 codedList.append(compareI[0] + " " + str(codedList[j] + 1))
                 codedString.append(compareI)


encodedString = []
appendingBin = []
maxLength = 0
                 
for i in range(len(codedList)):

    appendingBin = []
                 
    encodedType = codedList[i]
    
    if(isinstance(encodedType, int)):
        encodedString.append(bin(encodedType)[2:])
            
    if(isinstance(encodedType, str)):
        encodedType = encodedType.split()
        #print("Si: ", encodedType)
        
        for j in encodedType:
            print(type(j))
            print(j)
            j = int(j)
            j = bin(j)[2:]
            j = str(j)
            if(len(j)<2):
                j = "0"+ j 
            appendingBin.append(j)
        
        appendingBin = ["".join(appendingBin)]
        #print("apppending: ", len(appendingBin[0]))
        if len(appendingBin[0]) > maxLength:
            maxLength = len(appendingBin[0])
            #print("Max legnt: ", maxLength)
        print(appendingBin)
        encodedString.append(appendingBin[0])
        

for i in range(len(encodedString)):
    if len(encodedString[i]) < maxLength:
        addCeros = maxLength - len(encodedString[i])
        for j in range(addCeros):
            encodedString[i] = "0" + encodedString[i]      




textfile = open("encoded.txt", "w")

for element in encodedString:
    textfile.write(element)

textfile.close()
textfile = open("dictionary.txt", "w")

for element in sequence:
    textfile.write(element + " ")

textfile.write("\n")

for element in encodedString:
    textfile.write(element + " ")
    
textfile.write("\n" + str(maxLength))    
textfile.close()

print("1- String inicial: ", sequence)
print("2- Coded String: ",codedString)  
print("3- Coded List: ", codedList)             
print("4- Encoded String: ",encodedString)
print("Max lenght: ", maxLength)

#print(numeralRep)
#print(sequence)            