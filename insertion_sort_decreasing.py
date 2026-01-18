"""
MSCS 532 - Assignment 1
Insertion Sort Algorithm (Monotonically Decreasing Order)

This program implements the Insertion Sort algorithm as described in
Chapter 2 of "Introduction to Algorithms" (CLRS), modified to sort
elements in monotonically decreasing order instead of increasing.
"""

def insertion_sort_decreasing(arr):
    """
    Sorts a list of numbers in monotonically decreasing order
    using the Insertion Sort algorithm.

    Parameters:
    arr (list): A list of integers or floating-point numbers

    Returns:
    None: The list is sorted in-place
    """

    # Loop through the array starting from the second element
    # because the first element is already considered sorted
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        key = arr[i]

        # Initialize j to the index just before i
        j = i - 1

        # Move elements that are smaller than key one position ahead
        # of their current position to make space for key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at the correct position
        arr[j + 1] = key


def main():
    """
    Main function to demonstrate the insertion sort algorithm.
    """

    # Sample array to be sorted
    data = [25, 17, 31, 13, 2, 89, 54]

    print("Original array:")
    print(data)

    # Call the insertion sort function
    insertion_sort_decreasing(data)

    print("\nSorted array in monotonically decreasing order:")
    print(data)


# Execute the main function
if __name__ == "__main__":
    main()
