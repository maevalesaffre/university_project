import subprocess

def print_fail() :
    print('\033[1;31mTEST FAILED\033[0m')

def print_pass() :
    print('\033[;32mTEST PASSED\033[0m')

def print_result(cp, expected_out) :
    if cp.returncode == 0 and cp.stdout == expected_out :
        print_pass()
    else:
        print(cp.stdout)
        print(cp.stderr)
        print_fail()
    
def test_command(arglist, expected, capture=False, timeout=1) :
    cmd = " ".join(arglist)
    print("Testing :" , cmd)
    try:
        cp = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=timeout)
        if expected != cp.returncode :
            print_fail()
        elif not capture :
            print_pass()
        return cp
    except subprocess.TimeoutExpired as e :
        print("Timeout expired !")
        print_fail()
        return nil
    except FileNotFoundError as e :
        print("Cannot find the % command".format(arglist[0]))
        print_fail()
        return nil


