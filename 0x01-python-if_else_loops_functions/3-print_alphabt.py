#!/usr/bin/python3

for a in range(97, 123):
    if a == 101 or a == 113:
        continue
    print("{}".format(chr(a)), end="", flush=True)
