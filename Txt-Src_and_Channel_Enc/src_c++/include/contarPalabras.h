#pragma once

//INCLUDES

#include "../include/header.h"

//DEFINES
#define MAX_LARGO_PALABRA 50
using namespace std;

/** @brief Implementacion de la clase contarPalabras que se encarga de la lectura del archivo de texto, analisis de informacion y calculo de probabilidad
    @author Brandon Esquivel
    @date September,2020.
    */
class contarPalabras{
    private:
        int n;/**cantidad de apariciones de la palabra*/
        int umbral;/**valor Umbral de apariciones para incluir una palabra*/
        FILE *f;/**Archivo de entrada por leer*/
        FILE *cf;/**Archivo de escritura salida para sustituir*/
        char palabra_actual[MAX_LARGO_PALABRA];/**Almacena la palabra obtenida actual en lectura*/
        int cantidadPalabrasUmbral;/**Contador de palabras que sobrepasan el umbral*/
        int cantidadPalabras;/**Contador de palabras total No repetidas*/
        int cantidadPalabrasUsadas;/**Contador de palabras total en el texto*/
        vector<string> palabras;/**Guarda las palabras del texto leido para contarlas*/
        vector<string> palabrasUmbral;/**Guarda las palabras del texto leido que aparezcan mas de u(Umbral) Veces*/
        vector<int> apariciones;/** Vector que indica las repeticiones de las palabras del vector palabras, con el fin de calcular la probabilidad*/

    public:
        /** Default constructor. */
        contarPalabras();
        
        /** Custom constructor. */
        contarPalabras(int umbral);


        /** Manejo del valor Umbral U de conteo de palabras: set y get
        @param umbral - Valor Umbral entero de cantidad de apariciones
        @return umbral - limite de apariciones para incluir en la sustitucion*/
        void setUmbral(int umbral);
        int getUmbral();

        /** Inicia a guardar las palabras del texto para analizar su numero de apariciones y devuelve la cantidad total de palabras
        @param f - archivo de entrada a manipular 
        @return cantidadPalabras - Cantidad total de palabras del archivo */
        int contar(char nombre[]);
        
        /** Get para obtener las cantidades de palabras totales, sobre el umbral y apariciones de una palabra por indice
        @return cantidadPalabras 
        @return cantidadPalabrasenUnmbral */
        int getCantidadPalabras();
        int getCantidadPalabrasUmbral();
        int getApariciones(int index);

        /** Cuenta las palabras del texto y guarda en el vector palabrasUmbral aquellas que aparezcan mas de U veces
        @param f - archivo de entrada a manipular */
        void guardarPalabras(char nombre[]);


        /** @brief Crea la tabla in.tab con las palabras a sustituir y su nueva cadena */
        void crearTabla();

        /** @brief Sutituye las palabras sobre umbral en el archivo de texto in.rep */
        void sustituir(char nombre[]);

        /** @brief decifra las palabras en el archivo de texto codificado */
        void decifrar(char nombre[]);

        /** Default destructor
        @brief Destruye el objeto contarPalabras */
        ~contarPalabras();
};
