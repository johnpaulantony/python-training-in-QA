import time

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
start_time = time.time()
print(fib(35))
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")