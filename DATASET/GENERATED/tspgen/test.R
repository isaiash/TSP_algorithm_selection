library(ggplot2)
library(gridExtra)
devtools::load_all(".")

args <- commandArgs(trailingOnly = TRUE)

n = as.numeric(args[1])
pm = 0.1
x = generateRandomNetwork(n, lower = 0, upper = 1)
y = x

#y$coordinates = doRotationMutation(y$coordinates, pm = pm)
y$coordinates = replicate2(y$coordinates, doMutation, pm = pm, n = 50)

#grid.arrange(autoplot(x) + xlim(c(-1, 2)) + ylim(c(-1, 2)), autoplot(y) + xlim(c(-1, 2)) + ylim(c(-1, 2)), nrow = 1L)
#grid.arrange(autoplot(y), nrow = 1L)

write.table(y, paste("coordinates/",args[1]), row.names = FALSE, col.names = FALSE, quote = FALSE)
