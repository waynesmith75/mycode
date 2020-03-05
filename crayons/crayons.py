#!/usr/bin/env/ python3

import crayons

def main():
    print(crayons.red('red')('red string'))

    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
    crayons.disable()
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = FALSE

    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

main()

