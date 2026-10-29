#print prime number between 1 and 50

for n in range(2, 51):
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, end=" ")