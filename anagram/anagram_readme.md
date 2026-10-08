ANAGRAM CHECK

Problem:
Check whether two strings contain
the same characters.

Example:

listen
silent

Output:
Anagram

Logic:

Convert both strings to lowercase.

Sort both strings.

listen -> eilnst
silent -> eilnst

If sorted strings match,
they are anagrams.

Time Complexity: O(n log n)
Space Complexity: O(n)
