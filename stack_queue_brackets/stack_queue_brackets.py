from stack_and_queue.stack import Stack

def validatebrackets(string):
    """
    Validate a string of brackets to ensure they are well-formed.

    Parameters:
    string (str): The string of brackets to validate.

    Returns:
    bool: True if all brackets are well-formed and balanced 
    False otherwise.
    """
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = Stack()
    if not string:
        return False
    for i in string: # check if the string is empty
        if i in brackets:
            # If the character is an open bracket, push it onto the stack
            stack.push(i)
        elif i in brackets.values():
            # If the character is a closing bracket, check if it matches the topmost open bracket on the stack
            if stack.is_empty():
                return False
            open_brackets = stack.pop()
            if i != brackets[open_brackets]:
                return False
            
    # If all brackets are well-formed, the stack should be empty
    return stack.is_empty()

string = '({[]]})'
print(string, '> ' ,validatebrackets(string))

        
    
    


