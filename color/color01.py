#!user/bin/env python

import crayons


def main():
    #print 'red string' in red
        print(crayons.red('red string'))
#RWB txt
        print('{}white {}'.format(crayons.red('red'), crayons.blue("blue")))
        crayons.disable()
        print('{}white{}'.format(crayons.red('red'), crayons.blue('blue')))
        print(crayons.red('red string', bold = true))


