import random
import time

# Function for Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

# Function for Binary Search
def binary_search(arr, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

# Generating a sorted array of 10,000 random integers
arr = sorted(random.sample(range(1, 1000000), 10000))

# Choose a target to search
target = random.choice(arr)

# Linear Search Test
start_time = time.time()
linear_result = linear_search(arr, target)
linear_search_time = time.time() - start_time

# Binary Search Test
start_time = time.time()
binary_result = binary_search(arr, target, 0, len(arr) - 1)
binary_search_time = time.time() - start_time

print(f"Linear search took: {linear_search_time:.10f} seconds, Result: {linear_result}")
print(f"Binary search took: {binary_search_time:.10f} seconds, Result: {binary_result}")
