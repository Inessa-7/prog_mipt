#!/usr/bin/python
import argparse


def fibb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)


parser = argparse.ArgumentParser()
parser.add_argument('number', type=int, help='Fibbonaci number')
args = parser.parse_args()
print(fibb(args.number))
