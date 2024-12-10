#!/usr/bin/python3

from test_process import *

test_command(['../do', 'true', 'true'], expected=0)
test_command(['../do', '-a', 'true', 'true'], expected=0)
test_command(['../do', '-o', 'true', 'true'], expected=0)
test_command(['../do', '-o', 'false', 'true'], expected=0)
test_command(['../do', '-o', 'true', 'false'], expected=0)

test_command(['../do', '-o', 'false', 'false'], expected=1)
test_command(['../do', '-a', 'true', 'false'], expected=1)
test_command(['../do', '-a', 'false', 'false'], expected=1)
test_command(['../do', '-a', 'false', 'true'], expected=1)

test_command(['../do', '-a', 'false', '"sleep 1"'], expected=1, timeout=2)
test_command(['../do', '-o', 'false', '"sleep 1"'], expected=0, timeout=2)

# Je ne peux pas tester proprement le coupe circuit
# (la shell retourne seulement quand tous les fils ont terminé)
test_command(['../do', '-a', '-c', 'false', '"sleep 2"'], expected=1, timeout=3)
test_command(['../do', '-o', '-c', 'true', '"sleep 2"'], expected=0, timeout=3)

