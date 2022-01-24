#include <iostream>


using std::cin;
using std::cout;

int main(){
	int deckE = 52;
	int cardNum = 13;
	int cardType = 4;
	int firstParCombination = cardNum * (cardType + 2);
	cout << "\nPosibles combinaciónes de un par: " << firstParCombination;
	
	// Se usa la exprexión (cardType + 2) como una representación de las posibles combinaciones
	// Se discriman los valores del posible par anterior de todos los tipos de cartas
	
	int secParCombination = (cardNum - 1) * (cardType + 2);
	cout << "\nPosibles combinaciónes de dos pares: " << secParCombination;
	
	// Se discriminaran 4 cartas de los dos pares encontrados y otras cuatro cartas de los valores identigos pero de otra categoria
	// Ejemplo: Si se saca un 2 de corazon y 2 de treboles, se ignorara el 2 de diamantes y el 2 corazon inverso porque se volveria una tercia
	
	deckE = deckE - 8;
	
	int totalCombinations = ((firstParCombination * secParCombination)/2) * 44;
	cout << "\nPosibles combinaciónes de dos pares en un as de 5 cartas: " << totalCombinations;
}

	//int diceFaces;
	//cout << "";
	//cin >> diceFaces;
	
