#!/bin/sh

cd test_cases

# Tests for on

echo "Testing the on program" 
python3 test_on.py
rm *.txt


echo "Testing the do program"
python3 test_do.py



