# Bubble Sort Program
# This program sorts a list of numbers in ascending order
# using the Bubble Sort technique.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):     # repeat passes     
        for j in range(n - i - 1):  # compare pairs
            if arr[j] > arr[j + 1]:
                # swap the numbers
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# Test the program
numbers = [5, 2, 9, 1, 5, 6]
print("Before sorting:", numbers)
print("After sorting:", bubble_sort(numbers))
