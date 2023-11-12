def search_insert_position(nums, x):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left
nums=[10,20,40,50,60,80]
x = int(input("Input a number to insert: "))
pos = search_insert_position(nums, x)
print(f"{x} should be inserted at position {pos}.")
nums.insert(pos, x)
print(nums)