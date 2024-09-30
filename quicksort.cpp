#include <iostream>
#include "quicksort.h"

// Partition function used by Quicksort
int partition(int arr[], int p, int r) {
    int x = arr[r]; // pivot element
    int i = p - 1;

    for (int j = p; j <= r - 1; j++) {
        if (arr[j] <= x) {
            i++;
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    // Swap arr[i+1] and arr[r] (pivot)
    int temp = arr[i + 1];
    arr[i + 1] = arr[r];
    arr[r] = temp;

    return i + 1;
}

//Fall 2024 - Small Assignment #1

// Quicksort function
void quicksort(int arr[], int p, int r) {
    if (p < r) {
        int q = partition(arr, p, r); // Get the partition index
        quicksort(arr, p, q - 1); // Sort the left part
        quicksort(arr, q + 1, r); // Sort the right part
    }
}

// Main function for receiving input from the bash script
int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <numbers...>" << std::endl;
        return 1;
    }

    int size = argc - 1; // First argument is the program name, so ignore it
    int arr[size];

    // Fill array with numbers from command-line arguments
    for (int i = 0; i < size; i++) {
        arr[i] = std::stoi(argv[i + 1]);
    }

    // Perform Quicksort
    quicksort(arr, 0, size - 1);

    // Print the sorted array
    std::cout << "Sorted array: ";
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
