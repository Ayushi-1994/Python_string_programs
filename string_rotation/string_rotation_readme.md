STRING ROTATION CHECK

Problem:
Check whether one string
is a rotation of another.

Example:

waterbottle
erbottlewat

Output:
Rotation

Logic:

Concatenate first string
with itself.

waterbottlewaterbottle

If second string occurs inside
the new string, it is a rotation.

Time Complexity: O(n)
Space Complexity: O(n)
