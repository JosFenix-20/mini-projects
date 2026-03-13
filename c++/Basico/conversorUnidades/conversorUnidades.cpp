#include <iostream>

using namespace std;

double sumar(double num_1,double num_2){
	return num_1+num_2;
}

double restar(double num_1,double num_2){
	return num_1-num_2;
}

double multiplicar(double num_1,double num_2){
	return num_1*num_2;
}

double dividir(double num_1,double num_2){
	if(num_2==0){
		cout<<"no se puede dividir entre 0"<<endl;
	}
	return num_1/num_2;
}

int main(){
	int opcion;
	double num_1,num_2,resultado;
	char repit;
	do {
        cout << "\n .:Calculadora en C++ :.\n"
             << "1. Sumar\n"
             << "2. Restar\n"
             << "3. Multiplicacion\n"
             << "4. Division\n"
             << "Elije una opcion: ";
        cin >> opcion;

        cout << "Ingrese el primer numero: ";
        cin >> num_1;
        cout << "Ingrese el segundo numero: ";
        cin >> num_2;

        switch (opcion) {
            case 1:
                resultado = sumar(num_1, num_2);
                cout << "Resultado: " << resultado << endl;
                break;
            case 2:
                resultado = restar(num_1, num_2);
                cout << "Resultado: " << resultado << endl;
                break;
            case 3:
                resultado = multiplicar(num_1, num_2);
                cout << "Resultado: " << resultado << endl;
                break;
            case 4:
                resultado = dividir(num_1, num_2);
                cout << "Resultado: " << resultado << endl;
                break;
            default:
                cout << "Opcion inválida." << endl;
        }

        cout << "\n¿Desea realizar otra operacion? (s/n): ";
        cin >> repit;
	}while(repit=='s'||repit=='S');
	cout<<"Gracias! °^°/"<<endl;
}