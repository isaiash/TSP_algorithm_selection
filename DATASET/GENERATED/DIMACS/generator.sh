#!/bin/bash

./portgen $1 $2 > PORTGEN/PORTGEN_$3.tsp
./portcgen $1 $2 > PORTCGEN/PORTCGEN_$3.tsp
#./portmgen $1 $2 > PORTMGEN/$3.tsp
