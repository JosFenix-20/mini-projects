#include<iostream>

using namespace std;


double TEMPERATURA(double dato,int origen, int destino){
    double tempC;
	// Convertir origen a Celsius
    switch(origen) {
        case 1: // Celsius
            tempC = dato;
            break;
        case 2: // Fahrenheit a Celsius
            tempC = (dato - 32) * 5.0 / 9.0;
            break;
        case 3: // Kelvin a Celsius
            tempC = dato - 273.15;
            break;
        default:
            cout << "Unidad de origen no válida\n";
            return 0;
    }

    // Convertir Celsius a destino
    switch(destino) {
        case 1: // Celsius
            return tempC;
        case 2: // Celsius a Fahrenheit
            return tempC * 9.0 / 5.0 + 32;
        case 3: // Celsius a Kelvin
            return tempC + 273.15;
        default:
            cout << "Unidad destino no válida\n";
            return 0;
    }
}

double DISTANCIA(double dato, int origen, int destino){
	double valorEnMetros;

    // Convertir origen a metros
    switch(origen) {
        case 1: // Metros
            valorEnMetros = dato;
            break;
        case 2: // Pies a metros
            valorEnMetros = dato * 0.3048;
            break;
        default:
            cout << "Unidad de origen no válida\n";
            return 0;
    }

    // Convertir metros a destino
    switch(destino) {
        case 1: // Metros
            return valorEnMetros;
        case 2: // Metros a pies
            return valorEnMetros / 0.3048;
        default:
            cout << "Unidad destino no válida\n";
            return 0;
    }
}

double MONEDA(double dato, int origen, int destino){
	double cantidadEnSoles;

    // Convertir origen a soles
    switch(origen) {
        case 1: // Soles (PEN)
            cantidadEnSoles = dato;
            break;
        case 2: // Dólares a soles
            cantidadEnSoles = dato*3.7;
            break;
        case 3: // Yenes a soles
            cantidadEnSoles = dato*0.028;
            break;
        default:
            cout << "Moneda de origen no válida\n";
            return 0;
    }

    // Convertir soles a destino
    switch(destino) {
        case 1: // Soles
            return cantidadEnSoles;
        case 2: // Soles a dólares
            return cantidadEnSoles / 3.7;
        case 3: // Soles a yenes
            return cantidadEnSoles / 0.028;
        default:
            cout << "Moneda destino no válida\n";
            return 0;
    }
}

void MENU(){
	int op,op_origen,op_destino;
	double dato;
	do{
		cout<<"\n.: Elige la conversion :.\n"
			<<"1. Temperatura\n"
			<<"2. Distancia\n"
			<<"3. Moneda\n"
			<<"0. Salir\n"
		    <<"ingrese una opcion: ";
		cin>>op;
		cout<<"\nOrigen - Destino:"<<endl;
		switch(op){
			case 1:
				cout<<"ingrese el dato: ";cin>>dato;
			    cout << "1. Celsius\n"
		    	     << "2. Fahrenheit\n"
		    	     << "3. Kelvin\n"
		        	 << "ingrese una opcion: ";
				cout<<"De ";cin >> op_origen;cout<<" a ";cin>>op_destino;
				cout<<"Resultado: "<<TEMPERATURA(dato,op_origen,op_destino)<<endl;
				break;
			case 2:
			    cout<<"ingrese el dato: ";cin>>dato;
				cout << "1. metros\n"
		    	     << "2. pies\n"
		        	 << "ingrese una opcion: ";
				cout<<"De ";cin >> op_origen;cout<<" a ";cin>>op_destino;
				cout<<"Resultado: "<<DISTANCIA(dato,op_origen,op_destino);
				break;
			case 3:
			    cout<<"ingrese el dato: ";cin>>dato;
				cout << "1. soles\n"
		    	     << "2. dolares\n"
		        	 << "3. yenes\n"
					 << "ingrese una opcion: ";
				cout<<"De ";cin >> op_origen;cout<<" a ";cin>>op_destino;
				cout<<"Resultado: "<<MONEDA(dato,op_origen,op_destino);
				break;
			case 0	:
				cout<<"Hasta luego °^°/";
				break;
			default:
				cout<<"Opcion no permitida";
				break;
		}
	}while(op != 0);
}

int main(){
	MENU();
}