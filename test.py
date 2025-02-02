import time
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_string(length):
    prime_string = ''
    num = 2
    while len(prime_string) < length:
        if is_prime(num):
            prime_string += str(num)
        num += 1
    return prime_string[:length]

a = int(input("donee i : "))
def solution(a):
    prime_string = generate_prime_string(10005)
    print(prime_string[a])

