def longest_palindromic_substring(s):
   
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
       
        return s[left+1:right]

    longest = ""
    for i in range(len(s)):
        
        odd = expand(i, i)
        
        even = expand(i, i+1)

        
        bigger = odd if len(odd) > len(even) else even

        
        if len(bigger) > len(longest):
            longest = bigger

    return longest
text = input("Enter a string: ")
print("Longest Palindromic Substring:", longest_palindromic_substring(text))


