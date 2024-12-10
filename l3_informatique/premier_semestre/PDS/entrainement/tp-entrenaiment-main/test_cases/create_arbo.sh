#!/bin/bash

#######################################
### THIS FILE SHOULD NOT BE CHANGED ###
#######################################

if [ ! -e test_cases/arbo_test1 ];
then
    mkdir -p test_cases/arbo_test1 test_cases/arbo_test2/a test_cases/arbo_test2/sous_rep1 test_cases/arbo_test3/rep test_cases/arbo_test4/a/b test_cases/arbo_test5/not_link test_cases/arbo_test6/rep
    touch test_cases/arbo_test3/file
    mkfifo test_cases/arbo_test3/pipe
    ln -s not_link test_cases/arbo_test5/link 
    touch test_cases/arbo_test6/file
    ln -s rep test_cases/arbo_test6/link1 
    ln -s link1 test_cases/arbo_test6/link2 
    ln -s link2 test_cases/arbo_test6/link3
fi
