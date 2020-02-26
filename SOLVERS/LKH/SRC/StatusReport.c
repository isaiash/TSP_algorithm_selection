#include "LKH.h"

void StatusReport(GainType Cost, double EntryTime, char *Suffix)
{
    if (Penalty) {
        printff("Cost = " GainFormat "_" GainFormat, CurrentPenalty, Cost);
        if (Optimum != MINUS_INFINITY && Optimum != 0) {
            if (ProblemType != CCVRP && ProblemType != TRP &&
                ProblemType != MLP &&
                MTSPObjective != MINMAX && MTSPObjective != MINMAX_SIZE)
                printff(", Gap = %0.4f%%",
                        100.0 * (Cost - Optimum) / Optimum);
            else
                printff(", Gap = %0.4f%%",
                        100.0 * (CurrentPenalty - Optimum) / Optimum);
        }
        printff(", Time = %0.2f sec. %s",
                fabs(GetTime() - EntryTime), Suffix);
    } else {
        printff("Cost = " GainFormat, Cost);
        if (Optimum != MINUS_INFINITY && Optimum != 0)
            printff(", Gap = %0.4f%%", 100.0 * (Cost - Optimum) / Optimum);
        printff(", Time = %0.2f sec. %s%s",
                fabs(GetTime() - EntryTime), Suffix,
                Cost < Optimum ? "<" : Cost == Optimum ? "=" : "");
    }
    printff("\n");
}

void StatusReport2(GainType Cost, GainType *Best_Cost,double *prev_time, double EntryTime, char *Suffix)
{
    if (Cost < *Best_Cost){
        *Best_Cost = Cost;
        *prev_time = clock();
        printff(GainFormat " %.6f\n", *Best_Cost, (*prev_time - initial_time)/CLOCKS_PER_SEC);
    }
    if ((clock() - *prev_time)/CLOCKS_PER_SEC > 600){
        printff(GainFormat " %.6f\n", *Best_Cost, (clock() - initial_time)/CLOCKS_PER_SEC);
        exit(0);
    }
}