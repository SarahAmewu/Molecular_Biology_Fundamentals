with open("..\\Datasets\\fib_rab_data.txt", "r") as file:
    n, k = map(int, file.read().strip().split())

def fib(n, k):
    if n <= 2 :
        return 1
    
    return fib(n-1, k) + (k *fib(n-2, k))

print(fib(n, k))
