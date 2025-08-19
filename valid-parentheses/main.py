# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def valid_parentheses(s: str) -> bool:
    stack = []
    pair = {")": "(", "]": "[", "}": "{"}

    for character in s:
        if character in pair:
            top = stack.pop() if stack else None
            if pair[character] != top:
                return False
        else:
            stack.append(character)

    return not stack


print(valid_parentheses(s="([])"))
