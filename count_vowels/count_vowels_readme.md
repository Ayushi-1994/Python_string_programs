# Count Vowels

## Problem

Count total vowels present in a string.

## Logic

Convert string into lowercase.

```python
text.lower()
```

Loop through every character.

Check:

```python
if ch in "aeiou"
```

If vowel found:

Increase counter.

```python
count += 1
```

Finally print count.

## Time Complexity

O(n)

## Space Complexity

O(1)
