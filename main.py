#!/bin/python3
if (__name__=='__main__'):
    from time import sleep
    from sys import stdout
    with open("text.txt", "r", encoding = 'utf-8') as f:
        for line in f.readlines():
            for character in [char for char in line]:
                print(character, end="")
                stdout.flush()
                sleep(0.1)
            sleep(0.7)
        print(end="\n")