# Write a function to check if a given string of parentheses (and other characters) is balanced.

def is_balanced(expression):
    """
    Function to check if a given string of parentheses is balanced.

    :param expression: String containing parentheses and possibly other characters.
    :return: True if the parentheses are balanced, False otherwise.
    """
    # Dictionary to map opening to closing parentheses
    matching_parentheses = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    # Stack to keep track of opening parentheses
    stack = []

    # Iterate through each character in the expression
    for char in expression:
        # If it's an opening parenthesis, push to the stack
        if char in matching_parentheses:
            stack.append(char)
        # If it's a closing parenthesis
        elif char in matching_parentheses.values():
            # If stack is empty or top of stack does not match, it's unbalanced
            if not stack or matching_parentheses[stack.pop()] != char:
                return False

    # If stack is empty, all parentheses were matched; otherwise, it's unbalanced
    return len(stack) == 0


# Example usage
print(is_balanced("(a + b) * [c - d]"))  # Output: True
print(is_balanced("[a * (c + d])"))      # Output: False
print(is_balanced("{[()]}"))             # Output: True
print(is_balanced("((()))"))             # Output: True
print(is_balanced("{[}]"))               # Output: False
