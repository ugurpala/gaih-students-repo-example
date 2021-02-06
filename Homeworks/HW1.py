"""
Homework 1
Create a list and swap the second half of the list with the first
half of the list and print this list on the screen.

"""

nums = list(range(1,5))
print("Original list:")
print(nums)
print("\n")

nums[0], nums[1], nums[2], nums[3] = nums[2], nums[3], nums[0], nums[1]
print("New list:")
print(nums)
