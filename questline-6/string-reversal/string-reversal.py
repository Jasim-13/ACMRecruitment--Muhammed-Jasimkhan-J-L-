# Program to reverse a string using iterative and recursion
# iterative method
def reverse_iterative(s):
    rev = ""                 # empty string to store result
    for i in s:              # go through each letter
        rev = i + rev        # add letter in front
    return rev
# recursion method
def reverse_recursive(s):
    if s == "" or len(s) == 1:   # stop when string is empty or 1 letter
        return s
    else:
        # call function again for rest of string, then add first letter at last
        return reverse_recursive(s[1:]) + s[0]

# main program
text = input("Enter a string: ")
print("Original:", text)
print("Reversed (loop):", reverse_iterative(text))
print("Reversed (recursion):", reverse_recursive(text))
