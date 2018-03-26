from __future__ import division
import numpy as np

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
values = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024,
          0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020,
          0.001]
dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
       'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
       'Z': 25}


def find_length(ciphertext):
    for m in range(1, 20):
        z = [[]] * m
        for k in range(len(z)):
            z[k] = []
        i = 0
        while i < len(ciphertext):
            z[i % m].append(ciphertext[i])
            i = i+1
        s = [0]*m
        freq = [[0] * 26 for i in range(m)]
        for i in range(len(z)):
            n = len(ciphertext)//m
            for j in range(0, 26):
                freq[i][j] = z[i].count(letters[j])
                s[i] = s[i] + float(((freq[i][j])*(freq[i][j]-1)))/(n*(n-1))
        avg = np.mean(s)
        eps = 0.065-avg
        if eps < 0.01:
            return m, freq


def find_key(ciphertext, freq, m):
    key = [0] * m
    n = len(ciphertext) // m
    for i in range(m):
        maximum = 0
        freq[i][:] = [x / n for x in freq[i]]
        for g in range(26):
            temp = shift(freq[i], g)
            res = np.dot(temp, values)
            if res > maximum:
                maximum = res
                key[i] = g
    for z in range(m):
        print(letters[key[z]])
    return key


def decrypt(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        plaintext.append(letters[(dic[ciphertext[i]]-key[i % len(key)]) % 26])
    return plaintext


def shift(l, n):
    return l[n:] + l[:n]
