/*
 * main.cpp
 *   created on: April 24, 2013
 * last updated: June 13, 2013
 *       author: liushujia
 */

#ifndef __ENVIRONMENT__
#include "environment.h"
#endif

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main( int argc, char* argv[] ){
	InitURandom(); 
	int maxNumOfTrial;

	TEnvironment* gEnv = new TEnvironment();
	gEnv->fFileNameTSP=(char*)malloc(100);	
	gEnv->fFileNameTSP=argv[1];
	maxNumOfTrial=10000;
	gEnv->Npop=1000;
	gEnv->Nch=100;
	gEnv->define();
	
	for( int n = 0; n < maxNumOfTrial; ++n ){ 
		gEnv->doIt(); 
		
		//gEnv->Npop += 10;
		//if (n == 80){
		//	gEnv->Nch=200;
		//}
		//gEnv->printOn(n);
		//gEnv->writeBest();
	}
	//system("pause");
	return 0;
}
