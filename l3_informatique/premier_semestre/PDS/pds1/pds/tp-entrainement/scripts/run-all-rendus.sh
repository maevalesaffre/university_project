#!/usr/bin/env bash

echo "# Resultats " > results.csv 

for i in rendus/*
do
    nom=$(basename $i)
    cp $i/answers.c .
    vote=`make test-docker | grep "Grade" | sed "s/[^0-9]//g"`
    echo "$nom, $vote"
    echo "$nom, $vote" >> results.csv
done
    
