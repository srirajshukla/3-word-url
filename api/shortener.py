import os
import random
from pathlib import Path

data_file = os.path.join(Path(__file__).resolve().parent, 'data\\words.txt')

with open(data_file, 'r') as f:
    words = f.read().splitlines()


def short(url):
    maxsize = len(words) - 1
    r1 = random.randint(0, maxsize)
    r2 = random.randint(0, maxsize)
    r3 = random.randint(0, maxsize)

    w1 = words[r1]
    w2 = words[r2]
    w3 = words[r3]

    w1 = w1[0].upper() + w1[1:]
    w2 = w2[0].upper() + w2[1:]
    w3 = w3[0].upper() + w3[1:]

    shortURLGen = w1 + w2 + w3

    return shortURLGen


if __name__ == "__main__":
    url = "http://www.google.com"
    print(short(url))
    url2 = "http://www.google.com"
    print(short(url2))
