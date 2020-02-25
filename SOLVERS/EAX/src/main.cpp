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
	gEnv->fFileNameTSP=(char*)malloc(200);	
	gEnv->fFileNameTSP=argv[1];
	gEnv->Npop=1000;
	gEnv->Nch=100;
	gEnv->define();
	while(1){ 
		gEnv->doIt(); 
	}
	return 0;
}
