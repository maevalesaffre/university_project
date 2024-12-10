#!/bin/bash

#######################################
### THIS FILE SHOULD NOT BE CHANGED ###
#######################################

./test_cases/create_arbo.sh

rm -f grade.txt
echo "0" > grade.txt
for file in $(echo $@| tr ' ' '\n'|sort -n);
do
    ./$file grade.txt
done
grade=$(awk '{s+=$1} END {print s}' grade.txt)
rm grade.txt

echo "Grade: $grade (estimation)"
