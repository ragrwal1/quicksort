import time

call_counter = 0  # Global counter to track the number of function calls

def Quicksort(A, p, r, depth=0):
    global call_counter
    call_counter += 1
    indent = '    ' * depth  # Indentation based on recursion depth
    start_time = time.time()  # Start time for runtime measurement

    if p < r:
        print(f"{indent}Entering Quicksort call #{call_counter} with p={p}, r={r}\n")
        q = Partition(A, p, r, depth+1)
        Quicksort(A, p, q - 1, depth+1)
        Quicksort(A, q + 1, r, depth+1)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{indent}Exiting Quicksort call #{call_counter} with p={p}, r={r}, duration: {duration:.6f} seconds\n")
    else:
        print(f"{indent}Quicksort call #{call_counter} returns immediately as p={p} >= r={r}\n")
        end_time = time.time()

def Partition(A, p, r, depth=0):
    indent = '    ' * depth
    x = A[r]
    i = p - 1
    print(f"{indent}Partition called with p={p}, r={r}, pivot element x={x}\n")
    for j in range(p, r):
        A_j = A[j]
        print(f"{indent}  Comparing A[j]={A_j} (index {j}) with pivot x={x}\n")
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            print(f"{indent}    Swapped A[i]={A[i]} (index {i}) with A[j]={A[j]} (index {j})\n")
    A[i + 1], A[r] = A[r], A[i + 1]
    print(f"{indent}  Swapped pivot A[i+1]={A[i+1]} (index {i+1}) with A[r]={A[r]} (index {r})\n")
    print(f"{indent}  Partitioned subarray: {A[p:r+1]}\n")
    return i + 1

# Example usage
A = [9, 16, 0, 4, 1]
print("=====================================\n")
print(f"Initial array: {A}")
print("=====================================\n")
Quicksort(A, 0, len(A) - 1)
print("=====================================\n")
print(f"Sorted array: {A}")
print("=====================================\n")
