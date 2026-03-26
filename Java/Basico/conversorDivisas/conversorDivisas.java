package agenta_contactos;
import java.util.Scanner;
/**
 *
 * @author FENIX
 */
public class conversorDivisas {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        MENU();
    }
    
    public static void MENU(){
        int op,op_origen,op_destino;
	double dato;
        String  pantalla_menu="""
                        .: Elige la conversion :.
			1. Temperatura
			2. Distancia
			3. Moneda
			0. Salir
		        ingrese una opcion:
                        """,
                pantalla_temperatura="""
                        .: Elige la conversion :.
			1. Celsius
			2. Fahrenheit
			3. Kelvin
		        ingrese una opcion:
                        """,
                pantalla_distancia="""
                        .: Elige la conversion :.
                        1. Metros
                        2. Pies
                        ingrese una opcion:                                   
                        """,
                pantalla_monedas="""
                        .: Elige la conversion :.
                        1. Soles
                        2. Dolares
                        3. Yenes
                        ingrese una opcion:                                   
                        """;
        
	do{
		System.out.println(pantalla_menu);
		op=sc.nextInt();
		switch(op){
			case 1:
                                System.out.println("Origen - Destino:");
                                System.out.println("ingrese el dato: ");
                                dato=sc.nextDouble();
                                System.out.println(pantalla_temperatura);
                                System.out.println("De ");
                                op_origen=sc.nextInt();
                                System.out.println(" a ");
                                op_destino=sc.nextInt();
                                System.out.println("Resultado: "+TEMPERATURA(dato,op_origen,op_destino));
				break;
			case 2:
                                System.out.println("Origen - Destino:");
                                System.out.println("ingrese el dato: ");
                                dato=sc.nextDouble();
                                System.out.println(pantalla_distancia);
                                System.out.println("De ");
                                op_origen=sc.nextInt();
                                System.out.println(" a ");
                                op_destino=sc.nextInt();
                                System.out.println("Resultado: "+DISTANCIA(dato,op_origen,op_destino));
				break;
			case 3:
                                System.out.println("Origen - Destino:");
                                System.out.println("ingrese el dato: ");
                                dato=sc.nextDouble();
                                System.out.println(pantalla_monedas);
                                System.out.println("De ");
                                op_origen=sc.nextInt();
                                System.out.println(" a ");
                                op_destino=sc.nextInt();
                                System.out.println("Resultado: "+MONEDA(dato,op_origen,op_destino));
				break;
			case 0	:
                                System.out.println("Hasta luego °^°/");
				break;
			default:
				System.out.println("Opcion no permitida");
				break;
		}
	}while(op != 0);
    }

    public static double TEMPERATURA(double dato,int origen, int destino){
    double tempC=0;
	// Convertir origen a Celsius
    switch(origen) {
        case 1 -> // Celsius
            tempC = dato;
        case 2 -> // Fahrenheit a Celsius
            tempC = (dato - 32) * 5.0 / 9.0;
        case 3 -> // Kelvin a Celsius
            tempC = dato - 273.15;
        default -> {
            System.out.println("Unidad de origen no válida");
            return 0;
            }
        }

    // Convertir Celsius a destino
    switch(destino) {
        case 1 -> {
            // Celsius
            return tempC;
            }
        case 2 -> {
            // Celsius a Fahrenheit
            return tempC * 9.0 / 5.0 + 32;
            }
        case 3 -> {
            // Celsius a Kelvin
            return tempC + 273.15;
            }
        default -> {
            System.out.println("Unidad de origen no válida");
            return 0;
            }
        }
    }

    public static double DISTANCIA(double dato, int origen, int destino){
    double valorEnMetros=0;

    // Convertir origen a metros
    switch(origen) {
        case 1 -> // Metros
            valorEnMetros = dato;
        case 2 -> // Pies a metros
            valorEnMetros = dato * 0.3048;
        default -> {
            System.out.println("Unidad de origen no válida");
            return 0;
            }
        }

    // Convertir metros a destino
    switch(destino) {
        case 1 -> {
            // Metros
            return valorEnMetros;
            }
        case 2 -> {
            // Metros a pies
            return valorEnMetros / 0.3048;
            }
        default -> {
            System.out.println("Unidad de origen no válida");
            return 0;
            }
        }
    }

    public static double MONEDA(double dato, int origen, int destino){
    double cantidadEnSoles;

    // Convertir origen a soles
    switch(origen) {
        case 1 -> // Soles (PEN)
            cantidadEnSoles = dato;
        case 2 -> // Dólares a soles
            cantidadEnSoles = dato*3.7;
        case 3 -> // Yenes a soles
            cantidadEnSoles = dato*0.028;
        default -> {
            System.out.println("Unidad de origen no válida");
            return 0;
            }
        }

    // Convertir soles a destino
    switch(destino) {
        case 1 -> {
            // Soles
            return cantidadEnSoles;
            }
        case 2 -> {
            // Soles a dólares
            return cantidadEnSoles / 3.7;
            }
        case 3 -> {
            // Soles a yenes
            return cantidadEnSoles / 0.028;
            }
        default -> {
            System.out.println("Unidad de origen no válida");
            return 0;
            }
        }
    }
}
