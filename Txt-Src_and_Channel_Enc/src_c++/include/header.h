/** 
 * @authors Brandon Esquivel, Yassir Wagon, Reinier Camacho
 * @date Enero 2020
 * @warning UCR EIE
 * @mainpage Manejo de Archivos: Compresion y descompresion en Python y C++
 * @brief Implementacion del Laboratorio 2 del curso IE0217 Estructuras abstractas y algoritmos para ingeniería.
 * @section intro_sec Introduccion
 * En el presente codigo se muestra la solucion implementada el laboratorio 2 del curso IE0217 Estructuras abstractas y algoritmos para ingeniería, de la escuela de Ingenieria Electrica , EIE, UCR.
 * En este laboratorio el equipo de trabajo debera implementar, en Python y C++, un algoritmo de compresion y descompresion de texto basado en reemplazos. Dicho algoritmo funciona de la siguiente manera:
 * 1- Tomando como entrada un archivo con texto, se establece un umbral de reemplazo.
 * 2. Para cada palabra cuya frecuencia sea igual o mayor a la del umbral de reemplazo, cambiar su hilera de caracteres por otra. Agregue en un archivo aparte una tabla con cada uno de los reemplazos, indicando la palabra original y su nueva hilera.
 * @section compile_sec Compilacion
 * Ejecute el comando make en la carpeta raiz (Lab2) luego para correr ejecute make run o bien ./bin/main (int Umbral) archivo.txt 
 * 
 * **/ 



//INCLUDES
#include <ctime>
#include <cstdlib>
#include <stdio.h>
#include <sstream>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <exception>
#include <type_traits>
#include <fstream>
#include <string.h>
#include "../include/contarPalabras.h"
#include <cctype>