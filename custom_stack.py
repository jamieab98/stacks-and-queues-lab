def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    opening = ['(', '[', '{']
    stack = []
    for i in s:
        if i in opening:
            stack.append(i)
        elif i == "}" and stack[len(stack)-1] == "{":
            stack.pop()
        elif i == ")" and stack[len(stack)-1] == "(":
            stack.pop()
        elif i == "]" and stack[len(stack)-1] == "[":
            stack.pop()
        else:
            return False
        
    if stack == []:
        return True
    else:
        return False

tester = "({}[])"

print(is_valid_parentheses(tester))