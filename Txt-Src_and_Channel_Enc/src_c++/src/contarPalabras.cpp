
// Implementacion de la clase COntarPalabras que se encarga de analizar el texto fuente a procesar, obtiene direntes valores como la probabilidad y genera datos de salida para encriptacion y codificacion huffman
// INCLUDES
#include "../include/header.h"

// DEFINES

using namespace std;

    //metodos
// set y get umbral
void contarPalabras::setUmbral(int u){
    this->umbral = u;
}

int contarPalabras::getUmbral(){
    return this->umbral;
}


int contarPalabras::getCantidadPalabras(){
return this->cantidadPalabras;
}


int contarPalabras::getCantidadPalabrasUmbral(){
return this->cantidadPalabrasUmbral;
}

int contarPalabras::getApariciones(int index){
return this->apariciones.at(index);
}


int contarPalabras::contar(char nombre[]){

    f = fopen(nombre,"r");                                                  // Abriendo archivo en modo lectura

    if (f == NULL) {                                                        // Comprobando que se abrio bien
        cout << "No se pudo abrir el archivo.\n"<< endl;
        exit(1);
    }

    fscanf(f, "%s", palabra_actual);                                        // Se escanea la primer palabra y se guarda.
    apariciones.push_back(1);
    cantidadPalabras++;                                                     // contador de palabras no repetidas
    cantidadPalabrasUsadas++;                                               // contador de palabras, apariciones totales repetidas
    palabras.push_back(palabra_actual);                                     // Agregando palabra inicial
    while(!feof(f)){                                                        // Mientras no sea el fin del archivo, escanea palabra por palabra y la almacena en palabra_actual
        bool agregar = true;                                                // Bandera de comprobacion si la palabra esta repetida
        cantidadPalabrasUsadas++;
        fscanf(f, "%s", palabra_actual);                                    // Escanea palabra por palabra y la almacena en palabra_actual
        for( size_t i = 0; i < palabras.size(); ++i)                        // Recorre el vector verificando si la palabra ya esta guardada
        {
            if(this->palabras[i]==this->palabra_actual){                    // SI LA PALABRA ESTA REPETIDA, SE LA SALTA
                agregar = false;
                apariciones.at(i) = apariciones.at(i)+1;                    // sumando contador de apariciones de cicha palabra.
                break;
            }
        }
        if(agregar==true){                                                  // Agrega cada palabra NO REPETIDA en una posicion del vector palabras y aumenta el contador de palabas
            this->palabras.push_back(this->palabra_actual);
            this->cantidadPalabras++;
            this->apariciones.push_back(1);
        }
    }               // fin while
    fclose(f);                                                              // Cerrando archivo
    cout << "Se han contado las palabras. Total de palabras usadas: " << this->cantidadPalabrasUsadas << endl;
    cout << "Se han contado las palabras. Total de palabras usadas NO REPETIDAS: " << this->cantidadPalabras << endl;
    return this->cantidadPalabras;
}




void contarPalabras::guardarPalabras(char nombre[]){

cout << "\nIniciando conteo sobre umbral definido..." << endl;

 f = fopen(nombre,"r");                                                         // Abriendo archivo en modo lectura
    if (f == NULL) {                                                            // Comprobando que se abrió bien
        cout << "No se pudo abrir el archivo.\n"<< endl;
        exit(1);
    }

    for (size_t i = 0; i < palabras.size(); i++){                                 // Se recorre el vector de palabras guardadas
        n=0;
        while(!feof(f)){                                                          // Mientras no sea el fin del archivo escanea palabra por palabra
            fscanf(f, "%s", palabra_actual);                                      // Recorre el vector hasta el numero de palabras contadas NO repetidas y aumenta su contador
            if (palabras[i]==palabra_actual){                                     // Si la palabra leida concuerda con la analizada actualmente del vector, se suma el contador
                n++;
            }
        }
        rewind(f);                                                                  // Reestableciendo Puntero del archivo abierto para nueva iteracion de lectura
        if(n>=umbral){                                                              // Si el numero de repeticiones de la palabra es mayor que el umbral, se agrega al vector de palabras sobre umbral
            palabrasUmbral.push_back(palabras[i]);
            cantidadPalabrasUmbral++;                                                // Aumentando contador de palabras a sustituir
        }
    }

    cout << "Done...!" << endl;
    fclose(f);                                                                       // Cerrando archivo abierto
}



void contarPalabras::crearTabla(){
    cout << "Creando tabla data.tab ... " << endl;                                        // Encabezado

    ofstream tabla;                                                                     // Abriendo archivo .tab para escribir tabla
    tabla.open("../results/data.tab");
    double probabilidad = 0.000;                                                                           // Recorriendo vector con palabras
    for(int j=0; j<cantidadPalabrasUmbral; j++){
       probabilidad = ((double)(apariciones.at(j))/((double)cantidadPalabrasUsadas))*100;
        tabla   <<  palabrasUmbral[j] << "\t\t" << apariciones.at(j) << "\t\t" << probabilidad <<  endl;                   // Apend
    }
    cout << "\nFinalizado. " << endl;
    tabla.close();                                                                                  // Cerrando archivo

}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






// BETA VERSION - BRAINSTORM ONLY >:)





void contarPalabras::sustituir(char nombre[]){
    cout << "\nSe procede a realizar compresion por sustitucion..." << endl;                // Encabezado

    char caracter;                                                              // Variable auxiliar para guardar caracter.
    string add = "";                                                            // Variable temporal para almacenar
    f = fopen(nombre,"r");                                                      // Abriendo copia para sustituir
    if (f == NULL) {                                                            // Comprobando que se abrio bien
        cout << "No se pudo abrir el archivo.\n"<< endl;
        exit(1);
    }

    fscanf(f, "%c", &caracter);                                              // Escaneando primer caracter (solucion error de ultimo caracter)
    while(!feof(f)){                                                         // Mientras no sea el fin del archivo escanea palabra por palabra 
        add = add + caracter;                                                // Concatenando cadenas
        fscanf(f, "%c", &caracter);                                          // Escaneando caracter
    }


    for(int j=0; j<cantidadPalabrasUmbral; j++){                             // Realizando sustitucion
            int pos = add.find(palabrasUmbral[j]);                           // Se obtiene la posicion de la palabra a sustituir en el string
            stringstream ss;                                                 // Se crea objeto stringstream para cast
            ss << j;                                                         // Agregando valor de iterador para sustitucion con @j -> @1, @2... etc
            string sust = "@"+ ss.str();                                     // Cast y sustitucion con @, utilizable para codificacion
            while(pos!= -1){                                                 // Pos devuelve -1 cuando termina
                add.replace(pos, palabrasUmbral[j].size(), sust);            // Reemplazando palabra por codigo
                pos = add.find(palabrasUmbral[j], pos + sust.size());        // Solucion para que continue sustituyendo luego de la actual sustitucion (Sino se embucla)
            }
    }
    fclose(f);                                                                // Cerrando archivo
        // Se creo el string sustituido, ahora se incluye en in.rep

        ofstream cp;                                                          // Abriendo archivo in.rep para realizar sustitucion
        cp.open("../results/zip.txt");

        for(size_t j = 0; j<add.size(); j++){                                 // Recorriendo string add comprimido caracter por caracter para escribirlo en el archivo de salida                 
            caracter = add.at(j);                                             // Obteniedo caracter
            cp << caracter;                                                   // Escribiendo en archivo de salida
        }
        cp.close();                                                           // Cerrando archivo

     cout << "\nSutitucion Completada. Archivo de salida codificado creado." << endl;

}




void contarPalabras::decifrar(char nombre[]){
    cout << "\nSe procede a realizar descompresion por sustitucion..." << endl;                // Encabezado

    char caracter;
    int pos = 0;                                                              // Variable auxiliar para guardar caracter.
    string add = "";
    string num = "";                                                           // Variable temporal para almacenar
    f = fopen(nombre,"r");                                                      // Abriendo copia para sustituir
    if (f == NULL) {                                                            // Comprobando que se abrio bien
        cout << "No se pudo abrir el archivo.\n"<< endl;
        exit(1);
    }

    fscanf(f, "%c", &caracter);                                              // Escaneando primer caracter (solucion error de ultimo caracter)
    while(!feof(f)){                                                         // Mientras no sea el fin del archivo escanea palabra por palabra 
        add = add + caracter;                                                // Concatenando cadenas
        fscanf(f, "%c", &caracter);                                          // Escaneando caracter
    }
    fclose(f);

    for (int i = 0; i < add.size(); i++)
    {   int j = 0;
        if(add.at(i) == '@'){
            j = i;
            while( isdigit(add.at(j+1)) )
            {
                num = num + add.at(j+1);
                j++;
            }
            stringstream intValue(num);
            intValue >> pos;
            add.replace(i,num.size()+1,palabrasUmbral.at(pos));
            num = "";
            pos = 0;
        }
    }
// Se creo el string sustituido, ahora se incluye en unzip.txt

        ofstream cp;                                                          // Abriendo archivo in.rep para realizar sustitucion
        cp.open("../results/unzip.txt");

        for(size_t j = 0; j<add.size(); j++){                                 // Recorriendo string add comprimido caracter por caracter para escribirlo en el archivo de salida                 
            caracter = add.at(j);                                             // Obteniedo caracter
            cp << caracter;                                                   // Escribiendo en archivo de salida
        }
        cp.close();                                                           // Cerrando archivo

     cout << "\nSutitucion Completada. Archivo de salida creado." << endl;
}



//metodo de creacion - Inicializa vectores
contarPalabras::contarPalabras(int umbral){
    this->umbral=umbral;
    this->cantidadPalabrasUmbral=0;
    this->cantidadPalabras=0;
    this->n=0;

}

contarPalabras::~contarPalabras(){
    //Do nothing
}
