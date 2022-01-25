# Author: Luis Daniel García Leal

# Tamaño total del deck estandar
deckE <- 52

# Numero totales de cartas de cada categoria. (Se toman en cuenta cartas como el Joker o el rey)
cardNum <- 13

# Existen cuatro tipos de cartas: treboles, corazones, diamantes y corazones invertidos
cardType <- 4

# Son el par de cartas que estamos buscando.
par <- 2

# Se usa la exprexión (cardType + 2) como una representación de las posibles combinaciones
# Se discriman los valores del posible par anterior de todos los tipos de cartas.

firstParCombination <- cardNum * (cardType + par)
firstParCombination

# Se discriminaran 4 cartas de los dos pares encontrados y otras cuatro cartas de los valores identigos pero de otra categoria
# Ejemplo: Si se saca un 2 de corazon y 2 de treboles, se ignorara el 2 de diamantes y el 2 corazon inverso porque se volveria una tercia

secParCombination <- (cardNum - 1) * (cardType + par)
secParCombination

deckE = deckE - 8
deckE

totalCombinations = ((firstParCombination * secParCombination)/2) * deckE
totalCombinations

