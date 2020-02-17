FILES=../DATASET/PUBLIC/TSPLIB/*.tsp
for f in $FILES
do
    bash CLK/run.sh $f > "Results/CLK/TSPLIB/${f##*/}.res"
done

FILES=../DATASET/PUBLIC/TNM/*.tsp
for f in $FILES
do
    bash CLK/run.sh $f > "Results/CLK/TNM/${f##*/}.res"
done
