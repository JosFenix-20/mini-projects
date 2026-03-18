package calculadora;
import java.util.Scanner;
/**
 *
 * @author FENIX
 */
public class Calculadora {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int op;
        double num_1,num_2,resultado;
        String pantala = """
                .:CALCULADORA:.
                1. Suma
                2. Resta
                3. Multiplicar
                4. Dividir
                5. Salir
                """;
        do {
            sc.nextLine();
            System.out.println(pantala);
            System.out.println("Opcion: ");
            op=sc.nextInt();
            switch (op) {
                case 1:
                    System.out.println("Ingresa el primer numero: ");
                    num_1=sc.nextInt();
                    System.out.println("Ingresa el segundo numero: ");
                    num_2=sc.nextInt();
                    resultado=sumar(num_1,num_2);
                    System.out.println("Resultado: "+resultado);
                    break;
                case 2:
                    System.out.println("Ingresa el primer numero: ");
                    num_1=sc.nextInt();
                    System.out.println("Ingresa el segundo numero: ");
                    num_2=sc.nextInt();
                    resultado=restar(num_1,num_2);
                    System.out.println("Resultado: "+resultado);                    
                    break;
                case 3:
                    System.out.println("Ingresa el primer numero: ");
                    num_1=sc.nextInt();
                    System.out.println("Ingresa el segundo numero: ");
                    num_2=sc.nextInt();
                    resultado=multiplicar(num_1,num_2);
                    System.out.println("Resultado: "+resultado);                    
                    break;
                case 4:
                    System.out.println("Ingresa el primer numero: ");
                    num_1=sc.nextInt();
                    System.out.println("Ingresa el segundo numero: ");
                    num_2=sc.nextInt();
                    resultado=dividir(num_1,num_2);
                    System.out.println("Resultado: "+resultado);                    
                    break;
                case 5:
                    System.out.println("hasta luego <°^°>/");
                    break;
                default:
                    System.out.println("Opcion no valida");
            }
        } while (op != 5);
    }
    
    public static double sumar(double a,double b){
        return a+b;
    }
    
    public static double restar(double a,double b){
        return a-b;
    }
    
    public static double multiplicar(double a,double b){
        return a*b;
    }
    
    public static double dividir(double a,double b){
        if (b == 0) {
            throw new ArithmeticException("División por cero no permitida");
        }
        return a/b;
    }
}