#!/bin/bash

if [ ! -e test_cases/arbo ];
then
    mkdir -p test_cases/arbo/subdir/subsubdir
    mkdir -p test_cases/arbo/tmp
    echo "Un fichier normal" > test_cases/hello.txt
    ln -s ../hello.txt test_cases/arbo/link
    echo "Explication" > test_cases/arbo/README.txt
    echo "important!" > test_cases/arbo/subdir/data.txt
    echo "pas important ?" > test_cases/arbo/subdir/data2.txt
    echo "bye" > test_cases/arbo/subdir/subsubdir/bye.txt
    echo "hello" > test_cases/arbo/subdir/subsubdir/hello.txt
    echo "encore des données" > test_cases/arbo/tmp/data.txt
    ln -s arbo test_cases/dir_sym
fi
