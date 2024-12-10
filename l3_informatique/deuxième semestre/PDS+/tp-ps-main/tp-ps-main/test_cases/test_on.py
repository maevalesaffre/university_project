#!/usr/bin/python3

from test_process import *

test_command(["../on", "true", "do", "true"], expected=0)
test_command(["../on", "true", "do", "false"], expected=1)
test_command(["../on", "false", "do", 'echo "ok"'], expected=1)

out = test_command(["../on", "true", "do", 'echo "ok"'], expected=0, capture=True)
print_result(out, "ok\n")

test_command(["../on", "true", "do", 'echo "ok" > txt.txt'], expected=0)

out = test_command(["../on", "true", "do", "cat txt.txt"], expected=0, capture=True)
print_result(out, "ok\n")

test_command(["../on", "true", "do", 'echo "test" > txt.txt'], expected=0)

out = test_command(["../on", "true", 'do', 'cat txt.txt'], expected=0, capture=True)
print_result(out, "test\n")

test_command(["../on", "true", "do", 'echo "pds+" > second.txt'], expected=0)

out = test_command(["../on", "cp", "second.txt", "txt.txt", "do", 'cat txt.txt'], expected=0, capture=True)
print_result(out, "pds+\n")
