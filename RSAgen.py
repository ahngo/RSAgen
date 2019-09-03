#!/usr/bin/env python3
# Generates small numbers used for RSA public/private keys.

import random
import math

# Function to check if a number is prime
def isPrime(n) : 
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

# Encrypt message m  
def encrypt(m, e, n):
    enc = (m ** e) % n
    return enc

# Decrypt message c
def decrypt(c, d, n):
    dec = (c ** d) % n
    return dec

# Extended euclidean algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
        
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m        

# Start program
random.seed()

# Naive way of generating prime numbers
p = random.randint(555, 10001)
while (isPrime(p) != True):
    p += 1

q = random.randint(555, 10001)
while (isPrime(q) != True):
    q += 1

n = p * q
z = (p-1) * (q-1)
e = random.randint(1, n)

while (math.gcd(z, e) != 1):
    e += 1
d = modinv(e, z)

print("p: " + str(p) + " q:" + str(q))
print("n (pq): " + str(n))
print("z: " + str(z))
print("e: " + str(e) + " d: " + str(d))
print("d: " + str(d))

m = 150
print(chr(m))
test = encrypt(m, e, n)
print(str(test))
dectest = decrypt(test, d, n)
print(dectest)
