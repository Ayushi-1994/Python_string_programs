# Palindrome Check
 
## Problem
 
Check whether a string reads the same forward and backward.
 
Example:
 
MADAM
 
Reverse:
 
MADAM
 
Both are equal.
 
## Logic
 
Step 1:
Reverse the string.
 
```python
text[::-1]
```
 
Step 2:
Compare original string with reversed string.
 
```python
text == text[::-1]
```
 
If both are same:
 
Palindrome
 
Else:
 
Not Palindrome
 
## Time Complexity
 
O(n)
 
## Space Complexity
 
O(n)
