def Quicksort(A, p, r):
    if p < r:
        print(f"\nQuicksort called with p={p}, r={r}")
        q = Partition(A, p, r)
        Quicksort(A, p, q - 1)
        Quicksort(A, q + 1, r)

def Partition(A, p, r):
    x = A[r]
    i = p - 1
    print(f"\nPartition called with p={p}, r={r}, pivot element x={x}")
    for j in range(p, r):
        # Prepare A[i] for printing
        if 0 <= i < len(A):
            A_i = A[i]
        else:
            A_i = "Undefined"
        # Prepare A[j] for printing
        A_j = A[j]
        print(f"  In Partition: i={i}, j={j}, A[i]={A_i}, A[j]={A_j}")
        if A[j] <= x:
            i = i + 1
            # Swap A[i] and A[j]
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            print(f"    Swapped A[i]={A[i]} with A[j]={A[j]}")
    # Swap A[i + 1] and A[r]
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    print(f"  Swapped pivot A[i+1]={A[i+1]} with A[r]={A[r]}")
    print(f"  Partitioned array: {A[p:r+1]}")
    return i + 1

# Example usage
A = [2,1,3,4,7,5,6,8]
A = [9, 16, 0, 4, 1]
print(f"Initial array: {A}")
Quicksort(A, 0, len(A) - 1)
print(f"\nSorted array: {A}")
