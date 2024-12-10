#!/usr/bin/python3
# -*- coding: utf-8 -*-


TOWERS = 'ABC'
START = TOWERS[0]
FINISH = TOWERS[2]

OTHER = {
    (TOWERS[0], TOWERS[1]) : TOWERS[2],
    (TOWERS[0], TOWERS[2]) : TOWERS[1],
    (TOWERS[1], TOWERS[0]) : TOWERS[2],
    (TOWERS[1], TOWERS[2]) : TOWERS[0],
    (TOWERS[2], TOWERS[0]) : TOWERS[1],
    (TOWERS[2], TOWERS[1]) : TOWERS[0]
}


def move_disc(dep, dest):
    print('{:s} -> {:s}'.format(dep, dest))

def solve(ndiscs, dep, dest):
    '''
    :param ndiscs: (int) nbre de disques à déplacer depuis la tour dep
    :param dep, dest: (str)
    :return: (NoneType)
    :effet de bord: affiche la suite des coups pour déplacer nbdiscs depuis la 
          tour dep vers la tour dest
    :CU: dep, dest in 'ABC', dep != dest
    '''
    if ndiscs > 0:
        aux = OTHER[(dep, dest)]
        solve(ndiscs - 1, dep, aux)
        move_disc(dep, dest)
        solve(ndiscs - 1, aux, dest)

    
def main(ndiscs):
    '''
    :param ndiscs: (int) le nombre de disques initialement sur la tour A
    :return: (NoneType)
    :effet de bord: suite des mouvements à effectuer pour résoudre le problème
        des tours de Hanoi à ndiscs disques
    '''
    solve(ndiscs, START, FINISH)
    print(moves_sequence(ndiscs))
    
def usage():
    print('Usage: {:s} <n>'.format(sys.argv[0]))
    print('where\n\t<n> = number of discs.')
    # exit(1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        usage()
    else:
        try:
            ndiscs = int(sys.argv[1])
        except ValueError:
            usage()

        main(ndiscs)

        # exit(0)
