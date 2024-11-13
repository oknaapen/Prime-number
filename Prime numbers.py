def isPrime(x):
    if x <2:
        return False
    elif x ==2:
        return True
    for n in range(2,x):
        if x % n == 0:
          return False
    return True

def primeGenerator(f,t):
    list =[]
    for i in range(f,t):
        if isPrime(i) == True:
            list.append(i)
    print(list)

f = int(input())
t = int(input())

print(primeGenerator(f,t))
