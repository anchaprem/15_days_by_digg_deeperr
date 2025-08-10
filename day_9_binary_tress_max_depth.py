def find132pattern(nums):
    stack = []
    third = float('-inf')
    
    for num in reversed(nums):
        if num < third:
            return True
        while stack and num > stack[-1]:
            third = stack.pop()
        stack.append(num)
    
    return False

# Example
nums = [3, 1, 4, 2]
print(find132pattern(nums))  # Output: True
