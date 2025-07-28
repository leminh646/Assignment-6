import random

def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    # Step 1: Choose a random pivot
    pivot = random.choice(arr)

    # Step 2: Partition into 3 parts
    lows = [val for val in arr if val < pivot]
    highs = [val for val in arr if val > pivot]
    pivots = [val for val in arr if val == pivot]

    # Step 3: Recurse into the correct partition
    if k < len(lows):
        return randomized_quickselect(lows, k)
    if k < len(lows) + len(pivots):
        return pivot
    return randomized_quickselect(highs, k - len(pivots) - len(lows))

# Test case
if __name__ == "__main__":
    data = [9, 1, 5, 3, 7, 6, 8, 2, 4]
    k = 4  # 5th smallest element (0-based index)
    result = randomized_quickselect(data, k)
    print(f"The {k+1}-th smallest element is: {result}") # prints 5
