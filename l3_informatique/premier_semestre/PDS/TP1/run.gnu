set title "Octets et vitesse d'execution"
set logscale x
set xlabel "Octets du buffer"
set logscale y
set ylabel "temps en milis"
set style data linespoints
plot "temps.dat"
pause -1  "Hit return to continue"
