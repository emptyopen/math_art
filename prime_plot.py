import matplotlib.pyplot as plt
from math import sqrt; from itertools import count, islice
import datetime as dt
import random

WHITE_NOISE_OR_PRIMES = 'primes noise'

start = dt.datetime.now()

def Prime(n):
    if n & 1 == 0:
        return 2
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return 0


if 'noise' in WHITE_NOISE_OR_PRIMES:

    plt.figure(facecolor='w',figsize=(18.,11.))
    plt.subplots_adjust(left=.125,bottom=.1,right=.9,top=.92,wspace=.2,hspace=0.1)
    r = 500
    grid_r = ((r / 2) + 1) / 2 + 1
    plt.ylim(-grid_r, grid_r)
    plt.xlim(-grid_r, grid_r)
    plt.axis('off')

    current_point = [0, 0]
    current_direction = 'r'
    current_magnitude = 1
    next_direction = {'r':'u', 'u':'l', 'l':'d', 'd':'r'}
    number = 1

    for i in range(r):
        for j in range(current_magnitude):
            if random.randint(0,5) == 1:
                plt.plot(current_point[0], current_point[1], 'bo', markersize = 1.8)
            if current_direction == 'r':
                current_point = [current_point[0] + 1, current_point[1]]
            if current_direction == 'u':
                current_point = [current_point[0], current_point[1] - 1]
            if current_direction == 'l':
                current_point = [current_point[0] - 1, current_point[1]]
            if current_direction == 'd':
                current_point = [current_point[0], current_point[1] + 1]
            number += 1
        current_direction = next_direction[current_direction]
        if i % 2 == 1:
            current_magnitude += 1
    print('took {} seconds'.format((dt.datetime.now() - start).seconds))
    start = dt.datetime.now()
    #plt.show()
    plt.savefig('noise.png')

if 'primes' in WHITE_NOISE_OR_PRIMES:

    plt.figure(facecolor='w',figsize=(18.,11.))
    plt.subplots_adjust(left=.125,bottom=.1,right=.9,top=.92,wspace=.2,hspace=0.1)
    r = 500
    grid_r = ((r / 2) + 1) / 2 + 1
    plt.ylim(-grid_r, grid_r)
    plt.xlim(-grid_r, grid_r)
    plt.axis('off')

    current_point = [0, 0]
    current_direction = 'r'
    current_magnitude = 1
    next_direction = {'r':'u', 'u':'l', 'l':'d', 'd':'r'}
    number = 1

    for i in range(r):
        for j in range(current_magnitude):
            if Prime(number) == 0:
                plt.plot(current_point[0], current_point[1], 'bo', markersize = 1.8)
                #plt.text(current_point[0], current_point[1], number)
            if current_direction == 'r':
                current_point = [current_point[0] + 1, current_point[1]]
            if current_direction == 'u':
                current_point = [current_point[0], current_point[1] - 1]
            if current_direction == 'l':
                current_point = [current_point[0] - 1, current_point[1]]
            if current_direction == 'd':
                current_point = [current_point[0], current_point[1] + 1]
            number += 1
        current_direction = next_direction[current_direction]
        if i % 2 == 1:
            current_magnitude += 1
    print('took {} seconds'.format((dt.datetime.now() - start).seconds))
    #plt.show()
    plt.savefig('primes.png')
