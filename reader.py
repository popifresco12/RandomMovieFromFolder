import os
import random

path = 'E:\\Pelis'

listaPelis = []


for folder in os.listdir(path):
    listaPelis.append(folder)

print(len(listaPelis))


def choose():
    print(random.choice(listaPelis))

choose()
