def find132pattern(nums):
    stack, third = [], float('-inf')
    for num in reversed(nums):
        if num < third:
            return True
        while stack and num > stack[-1]:
            third = stack.pop()
        stack.append(num)
    return False

print(find132pattern([1, 2, 3, 4]))      # False
print(find132pattern([3, 1, 4, 2]))      # True
print(find132pattern([-1, 3, 2, 0]))     # True
