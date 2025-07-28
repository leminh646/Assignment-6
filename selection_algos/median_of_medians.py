def median_of_medians(A, k):
    # Base case: if the list is small, sort and return the k-th smallest
    if len(A) <= 5:
        return sorted(A)[k]

    # Step 1: Divide A into sublists of 5 elements each
    sublists = [A[i:i + 5] for i in range(0, len(A), 5)]

    # Step 2: Sort each sublist and get its median
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Step 3: Find the median of medians recursively
    pivot = median_of_medians(medians, len(medians) // 2)

    # Step 4: Partition the original array into three lists
    lows = [el for el in A if el < pivot]
    highs = [el for el in A if el > pivot]
    pivots = [el for el in A if el == pivot]

    # Step 5: Recurse into the appropriate partition
    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot  # pivot is the answer
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))

# Test case
if __name__ == "__main__":
    data = [9, 1, 5, 3, 7, 6, 8, 2, 4]
    k = 4  # Looking for the 5th smallest element (0-based index)
    result = median_of_medians(data, k)
    print(f"The {k+1}-th smallest element is: {result}") # prints 5
