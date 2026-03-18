#include<iostream>
#include<vector>
#include<string>

using namespace std;

int 					long_alumnos;
vector<string> 			nameAlumno;
vector<vector<double>>  gradeAlumno;


void Mostrar_alumnos(){
	for(int i=0; i<nameAlumno.size() ;i++){
		cout<<"Alumno "<<(i+1)<<"["<<nameAlumno[i]<<"]: ";
		int j=1;
		for(double n:gradeAlumno[i]){
			cout<<n<<" ";
		}
		cout<<endl;
	}
}

void Promedio(){
	for(int i=0; i<nameAlumno.size() ;i++){
		cout<<"Alumno "<<(i+1)<<"["<<nameAlumno[i]<<"]: ";
		double contador=0;
		
		for(int j=0; j<gradeAlumno[i].size();j++){
			contador+=gradeAlumno[i][j];
		}
		double promedio=contador/3;
		cout<<promedio<<endl;
	}
}

void Maximo_minimo(){
	double maximo=-99,minimo=99;
	int pos_max,pos_min;
	for(int i=0; i<nameAlumno.size() ;i++){
		double contador=0;
		for(int j=0; j<gradeAlumno[i].size();j++){
			contador+=gradeAlumno[i][j];
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
	cout<<"Maximo: "<<nameAlumno[pos_max]<<" --> "<<maximo<<endl;
	cout<<"Minimo: "<<nameAlumno[pos_min]<<" --> "<<minimo<<endl;
}

void add_alumnos(){
	string nombre;
	double nota;
	char repetir;
	do{
		cout<<"Alumno "<<(nameAlumno.size()+1)<<":";cin>>nombre;nameAlumno.push_back(nombre);
		vector<double> notas;			
		for(int j=0; j<3;j++){
			cout<<"Nota"<<(j+1)<<": ";cin>>nota;notas.push_back(nota);
		}
		gradeAlumno.push_back(notas);
		cout<<"¿Desea agregar mas? s[si]/n[no]: ";cin>>repetir;
	}while(repetir == 's' || repetir == 'S');
	
	cout<<"actualizacion de alumnos:"<<endl;
	Mostrar_alumnos();
}

void delete_alumno(){
	int pos;
	Mostrar_alumnos();
	cout<<endl;
	
	cout<<"introduce el numero del alumno: ";cin>>pos;pos-=1;
	
	if (pos>= 0 && pos<nameAlumno.size()){
        nameAlumno.erase(nameAlumno.begin() + pos);
        gradeAlumno.erase(gradeAlumno.begin() + pos);
        cout << "Alumno eliminado correctamente.\n";
    } else {
        cout << "Número inválido. No se eliminó ningún alumno.\n";
    }
    
	Mostrar_alumnos();
}

void MENU(){
	int op;
	do{
	    cout << "\n .: Gestion de Alumnos :.\n"
	         << "1. Mostrar alumnos\n"
    	     << "2. Promedio\n"
        	 << "3. maximos y minimos\n"
	         << "4. Agregar nuevos alumnos\n"
    	     << "5. Borrar alumno del registro\n"
        	 << "6. Salir\n"
        	 << "Elije una opcion: "<<endl;
        cin >> op;		
		switch(op){
			case 1:
				cout<<"ALUMNOS REGISTRADOS:"<<endl;
				Mostrar_alumnos();
				break;
			case 2:
				cout<<"PROMEDIO DE NOTAS:";
				Promedio();
				break;
			case 3:
				cout<<"Ranking de notas:";
				Maximo_minimo();
				break;
			case 4:
				cout<<"Agregar alumnos:";
				add_alumnos();
				break;
			case 5:
				cout<<"Borrar alumnos:";
				delete_alumno();
				break;
			case 6	:
				cout<<"Hasta luego °^°/";
				break;
			default:	
				cout<<"Opcion no permitida";
				break;
		}
	}while(op != 6);
}

int main(){
	cout<<"Ingrese el numero de alumnos: ";cin>>long_alumnos;
	for(int i; i<long_alumnos;i++){
		string names;
		cout<<"Alumno "<<(i+1)<<":";cin>>names;nameAlumno.push_back(names);
		vector<double> notas;
		for(int j=0; j<3;j++){
			double nota;
			cout<<"Notas: ";cin>>nota;notas.push_back(nota);
		}
		gradeAlumno.push_back(notas);
	}
	MENU();
	return 0;
}