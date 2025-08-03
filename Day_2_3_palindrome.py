def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Example call
text = "A man, a plan, a canal: Panama"
print("Is Palindrome:", isPalindrome(text))
