from random import randint
from time import sleep
rnd2 = randint(1,30)
color=0
def gentree():
    print("\033c","\033[0m")
    for x in range(1,23):
        rnd1 = randint(1,rnd2)
        color=randint(0,1)
        if x==1:
            ch="$"
        elif rnd1%4==0:
            ch="o"
        elif rnd1%3==0:
            ch="i"
        else:
            ch="*"
        #if color == 0:
            colors='\033[1;31m'
        #else:
            colors='\033[1;32m'

        print("{:^33}".format(ch*x))

    print("\033[33m{:^33}".format("|||"))
    print("{:^33}\033[0m".format("|||"))
    sleep(.75)
while True:
    gentree()
