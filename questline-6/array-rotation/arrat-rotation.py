# Program to rotate an array to the right by k steps
def rotate_array(nums, k):
    n = len(nums)
    k = k % n   # in case k is bigger than n
    rotated = [0] * n   # new list to store result
    # put each number in its new position
    for i in range(n):
        new_index = (i + k) % n
        rotated[new_index] = nums[i]

    return rotated
# main program
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Original array:", nums)
print("Rotated array:", rotate_array(nums, k))
