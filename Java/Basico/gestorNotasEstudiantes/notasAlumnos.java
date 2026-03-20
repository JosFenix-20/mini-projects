package agenta_contactos;
import java.util.Scanner;
import java.util.ArrayList;
/**
 *
 * @author FENIX
 */
public class notasAlumnos {
//===================================================================
    static int long_alumnos;
    static ArrayList<ArrayList<Double>> gradeAlumno = new ArrayList<>();
    static ArrayList<String> nameAlumno = new ArrayList<>();
    static Scanner sc=new Scanner(System.in);
//===================================================================
    public static void main(String[] args) {       
        System.out.println("Ingrese el numero de alumnos: ");
        long_alumnos=sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < long_alumnos; i++) {
            String names;
            System.out.println("Alumno "+(i+1)+":");
            names=sc.nextLine();
            nameAlumno.add(names);
            ArrayList<Double> notas=new ArrayList<>();
            for(int j=0; j<3;j++){
    		double nota;
    		System.out.println("Notas: ");
                nota=sc.nextDouble();
                notas.add(nota);
            }
            gradeAlumno.add(notas);
            sc.nextLine();
    
        }
        MENU();
    }
//===================================================================
    public static void MENU(){
        Scanner sc=new Scanner(System.in);
        int op;
        String pantalla = """
                 .: Gestion de Alumnos :.
                1. Mostrar alumnos
                2. Promedio
                3. Maximos y minimos
                4. Agregar nuevos alumnos
                5. Borrar alumno del registro
                0. Salir
                """;
	do{
            System.out.println(pantalla + "Elije una opcion: \n");
            op=sc.nextInt();
            switch(op){
		case 1:
                    System.out.println("ALUMNOS REGISTRADOS:");
                    Mostrar_alumnos();
                    break;
		case 2:
                    System.out.println("PROMEDIO DE NOTAS:");
                    Promedio();
                    break;
		case 3:
                    System.out.println("Ranking de notas:");
                    Maximo_minimo();
                    break;
		case 4:
                    System.out.println("Agregar alumnos:");
                    add_alumnos();
                    break;
		case 5:
                    System.out.println("Borrar alumnos:");
                    delete_alumno();
                    break;
		case 0:
                    System.out.println("Hasta luego °^°/");
                    break;
		default:	
                    System.out.println("Opcion no permitida");
                    break;
		}
	}while(op != 0);
    }
//===================================================================
    public static void Mostrar_alumnos(){
        for (int i = 0; i < nameAlumno.size(); i++) {
            System.out.println("Alumno "+(i+1)+"["+nameAlumno.get(i)+"]: ");
            for (double n:gradeAlumno.get(i)) {
                System.out.println(n+" ");
            }
            System.out.println("");
        }
    }
//===================================================================
    public static void Promedio(){
        for (int i = 0; i < nameAlumno.size(); i++) {
            System.out.println("Alumno "+(i+1)+"["+nameAlumno.get(i)+"]: ");
            double contador=0;
            for(int j=0; j<gradeAlumno.get(i).size();j++){
                contador+=gradeAlumno.get(i).get(j);
            }
            double promedio=contador/3;
            System.out.println(promedio);
        }
    }
//===================================================================
    public static void Maximo_minimo(){
	double maximo=Double.NEGATIVE_INFINITY,minimo=Double.POSITIVE_INFINITY;
	int pos_max=0,pos_min=0;
	for(int i=0; i<nameAlumno.size() ;i++){
            double contador=0;
            for(int j=0; j<gradeAlumno.get(i).size();j++){
		contador+=gradeAlumno.get(i).get(j);
            }
            double promedio=contador/3;
            if(promedio>maximo){
                maximo=promedio;
		pos_max=i;
            }
            if(promedio<minimo){
                minimo=promedio;
                pos_min=i;
            }
        }
        System.out.println("Maximo: "+nameAlumno.get(pos_max)+" --> "+maximo);
        System.out.println("Minimo: "+nameAlumno.get(pos_min)+" --> "+minimo);
    }
//===================================================================
    public static void add_alumnos(){
	String nombre;
	char repetir;
	do{
            System.out.println("Alumno"+(nameAlumno.size()+1)+":");
            nombre=sc.nextLine();
            nameAlumno.add(nombre);
            ArrayList<Double> notas=new ArrayList<>();			
            for(int j=0; j<3;j++){
		double nota;
    		System.out.println("Notas "+(j+1)+": ");
                nota=sc.nextDouble();
                notas.add(nota);
            }
            gradeAlumno.add(notas);
            System.out.println("¿Desea agregar mas? s[si]/n[no]: ");
            repetir=sc.next().charAt(0);
	}while(repetir == 's' || repetir == 'S');
	System.out.println("actualizacion de alumnos:");
	Mostrar_alumnos();
    }
//===================================================================
    public static void delete_alumno(){
	int pos;
	Mostrar_alumnos();
	System.out.println("introduce el numero del alumno: ");
        pos=sc.nextInt();
        pos-=1;
	
	if (pos>= 0 && pos<nameAlumno.size()){
            nameAlumno.remove(pos);
            gradeAlumno.remove(pos);
            System.out.println("Alumno eliminado correctamente.\n");
            System.out.println("Alumno eliminado correctamente.\n");
        } else {
            System.out.println("Número inválido. No se eliminó ningún alumno\n");
        }
        Mostrar_alumnos();
    }   
}