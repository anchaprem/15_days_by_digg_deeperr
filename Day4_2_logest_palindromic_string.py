def longestPalindrome(s):
    res = ""
    
    for i in range(len(s)):
        temp1 = expandFromCenter(s, i, i)
        temp2 = expandFromCenter(s, i, i + 1)
        if len(temp1) > len(res):
            res = temp1
        if len(temp2) > len(res):
            res = temp2
    
    return res

def expandFromCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

print(longestPalindrome("babad"))  # Output: "bab" or "aba"
