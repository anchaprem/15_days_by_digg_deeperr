def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1

print(twoSum([2, 7, 11, 15], 9))   # Output: [1, 2]
print(twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))  # Output: [4, 5]
