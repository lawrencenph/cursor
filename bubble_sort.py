def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    
    Time Complexity: O(n²) in worst and average cases, O(n) in best case
    Space Complexity: O(1)
    
    Args:
        arr (list): List of comparable elements to sort
        
    Returns:
        list: Sorted list
    """
    n = len(arr)
    
    # Create a copy to avoid modifying the original list
    arr_copy = arr.copy()
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize the algorithm
        # If no swapping occurs in a pass, array is sorted
        swapped = False
        
        # Last i elements are already in place
        # Compare adjacent elements
        for j in range(0, n - i - 1):
            # If current element is greater than next element, swap them
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
    
    return arr_copy


def bubble_sort_in_place(arr):
    """
    Bubble Sort Algorithm that modifies the original list in place
    
    Args:
        arr (list): List of comparable elements to sort (will be modified)
        
    Returns:
        None (modifies the original list)
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    print("Bubble Sort Implementation")
    print("=" * 40)
    
    for i, test_arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Original array: {test_arr}")
        
        # Using the function that returns a new sorted list
        sorted_arr = bubble_sort(test_arr)
        print(f"Sorted array:   {sorted_arr}")
        
        # Verify the original array is unchanged
        print(f"Original unchanged: {test_arr}")
        
        # Using the in-place function
        arr_copy = test_arr.copy()
        bubble_sort_in_place(arr_copy)
        print(f"In-place sorted: {arr_copy}")
    
    # Performance demonstration
    print("\n" + "=" * 40)
    print("Performance Demonstration")
    print("=" * 40)
    
    import random
    import time
    
    # Create a larger array for performance testing
    large_array = [random.randint(1, 1000) for _ in range(1000)]
    
    print(f"Sorting array of {len(large_array)} elements...")
    
    start_time = time.time()
    sorted_large = bubble_sort(large_array)
    end_time = time.time()
    
    print(f"Bubble sort took {end_time - start_time:.4f} seconds")
    print(f"First 10 elements: {sorted_large[:10]}")
    print(f"Last 10 elements: {sorted_large[-10:]}")
    
    # Verify it's actually sorted
    is_sorted = all(sorted_large[i] <= sorted_large[i+1] for i in range(len(sorted_large)-1))
    print(f"Array is correctly sorted: {is_sorted}") 