import sys
a, b = sys.stdin.readline().rstrip().split(" ")
a = list(a)
a = int(''.join(reversed(a)))
b = int(''.join(reversed(b)))
print(max(a, b))