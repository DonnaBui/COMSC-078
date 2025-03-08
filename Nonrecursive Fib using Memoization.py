def fib(n): # Recursive fib(n) function
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)
    
def memo(f): # Memoization function to store every value that has already been computed.
    # It prevents the recursive fib(n) function from recalculating values it already calculated in a previous recursive call because it returns the stored value from its cache dictionary.
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

    
def count(f): # used to count the number of function calls made to determine the Order of Growth
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted


"""Test the recursive fib(n) function without utilizing memo()"""
fib = count(fib) # used to count the number of function calls made
print("Result of fib(19):", fib(19)) # This should print 4181
print("Number of function calls made (without memo): ", fib.call_count) # 13529 function calls were made, making the Order of Growth O(b^n), or exponential.

print("")

"""Test the recursive fib(n) function with memo() to make it non-recursive"""
# This still utilizes the same recursive fib(n) function, but applies memo() to prevent it from recursively calculating values it already calculated.
countFib = count(fib)
fib = memo(countFib) # Apply memo() to fib while still retaining the ability to count function calls
print("Result of fib(19):", fib(19)) # Call the recursive fib function normally. It should still print 4181
print("Number of function calls made (with memo): ", countFib.call_count)
# By applying memo() to fib(n), the number of function calls are now only 20, making the Order of Growth O(n), or linear.
