

//INCLUDES

#include "../include/header.h"

//DEFINES

using namespace std;



int main(int argc, char *argv[]) {
if(argc<3) {
printf("Parametros insuficientes. Verifique.\n");
exit(1);
}
unsigned t0, t1;

t0=clock();
// INICIANDO CONTEO DE EJECUCION
contarPalabras contador(atoi(argv[1]));                                  // Declarando contador con umbral
contador.contar(argv[2]);

contador.guardarPalabras(argv[2]);

contador.crearTabla();



//////////////END//////////////
//BETA
contador.sustituir(argv[2]);
contador.decifrar("../results/zip.txt");
//////////////////////////////

// FINALIZA CONTEO DE EJECUCION
t1 = clock();
double time = (double(t1-t0)/CLOCKS_PER_SEC);                       // conversion de ticks a segundos
cout << "Tiempo de ejecucion: " << time << endl;

return 0;
}




