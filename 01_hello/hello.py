#!/usr/bin/env python3
"""
Author : Zaki Rucker <zakirucker@mac.com>
Date   : 2021-09-06
Purpose: Greet the user"""

import argparse

# --------------------------------------------------
parser = argparse.ArgumentParser(
    description='Greet the user',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-n', '--name',
                    metavar='name', default='World',
                    help='Name to greet')


args = parser.parse_args()

print('Hello, ' + args.name + '!')
