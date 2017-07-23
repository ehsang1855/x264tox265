#!/usr/bin/python
def ask_ok(prompt,retries=3,reminder='Please try again!'):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no', 'nop','nope'):
            return False
        retries-=1
        if retries <0:
            raise ValueError('invalid user response')
        print(reminder)

