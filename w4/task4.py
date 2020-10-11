#!/usr/bin/python
import argparse


def is_prime(n):
    if n == 1 or n == 2:
        return True
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


def make_list(l):
    answer = []
    i = 1
    while len(answer) != l:
        if is_prime(i):
            answer.append(i)
        i += 1
    return answer


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--show-all', action='store_true')
parser.add_argument('-f', '--file', type=argparse.FileType('w'), required=False)
parser.add_argument('number', type=int)
args = parser.parse_args()
number = args.number
if args.show_all:
    ans = make_list(number)
else:
    ans = make_list(number)[-1]

print(ans)

if args.file:
    ans = ' '.join(map(str, ans)) if type(ans) == list else str(ans)
    ans += '\n'
    args.file.write(ans)

