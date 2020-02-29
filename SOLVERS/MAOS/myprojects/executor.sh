cd $(dirname $0)

filename=${1##*/}
tsp_copy="tasks/TSP/instance/$filename"
cp $1 $tsp_copy

java -server -cp ../release/MAOS_SEQ.jar maosKernel.MAOSExecuter TSP:Problem=$filename N=300 Tcon=100 DUP_TIMES=10000 solver=STD_PRB_3Opt_REAX+SEAX:isAlpha=true opt=1
# -Xmx256M 
rm $tsp_copy
