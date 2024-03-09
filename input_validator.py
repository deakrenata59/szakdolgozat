import sys

def prepare_input(input):
    spaceless_input = ""
    for char in input.strip():
        if char.isalpha() or char in "()¬∧∨→":
            spaceless_input += char.upper()
    if spaceless_input:
        return spaceless_input
    raise ValueError

def validate_parentheses(input=''):
    try:
        stack = []
        for char in input:
            if char == '(':
                stack.append(char)
            elif char == ')':
                stack.pop()
        if len(stack):
            raise ValueError
    except ValueError:
        print("Error: input is invalid [there are more ( brackets than ).]")
    except IndexError:
        print("Error: input is invalid [there are more ) brackets than (.)]")

def validate_right_par(left_char, right_char): #)
    if left_char:
        if left_char in "(¬∧∨→":
            raise ValueError
    if right_char:
        if right_char in "(¬" or right_char.isalpha():
            raise ValueError
        
def validate_left_par(left_char, right_char): #(
    if left_char:
        if left_char.isalpha() or left_char == ")":
            raise ValueError
    if right_char:
        if right_char in ")∧∨→":
            raise ValueError
        
def validate_binary_operator(left_char, right_char):
    if left_char:
        if left_char in "(¬∧∨→":
            raise ValueError
    if right_char:
        if right_char in ")∧∨→":
            raise ValueError
        
def validate_negation(left_char, right_char):
    if left_char:
        if left_char == ")" or left_char.isalpha():
            raise ValueError
    if right_char:
        if right_char in "()∧∨→":
            raise ValueError
        
def validate_char(left_char, right_char):
    if left_char:
        if left_char == ")" or left_char.isalpha():
            raise ValueError
    if right_char:
        if right_char == "(" or right_char.isalpha():
            raise ValueError
        
def eliminate_needless_parentheses(input, starting_pos=0):
    for i in range(starting_pos, len(input)):
        if input[i] == "(" and i+1 != len(input) and input[i+1] == "(":
            left_par_ind = i
            j = i+1
            while input[j] != ')' and j < len(input):
                j += 1
            if input[j] == ')' and j+1 < len(input) and input[j+1] == ")":
                temp = input
                input = input[0:left_par_ind] + input[left_par_ind+1:j+1] + input[j+2:len(input)]
                return eliminate_needless_parentheses(input, i)
    return input

def validate_input(input):
    try:
        input = prepare_input(input)
        validate_parentheses(input)
        for i in range(0, len(input)):
            if input[i] == ')':
                validate_right_par(input[i-1] if i-1 >= 0 else "",input[i+1] if i+1 < len(input) else "")
            elif input[i] == '(':
                validate_left_par(input[i-1] if i-1 >= 0 else "",input[i+1] if i+1 < len(input) else "")
            elif input.isalpha():
                validate_char(input[i-1] if i-1 >= 0 else "",input[i+1] if i+1 < len(input) else "")
            elif input in "∧∨→":
                validate_binary_operator(input[i-1] if i-1 >= 0 else "",input[i+1] if i+1 < len(input) else "")
            elif input == "¬":
                validate_negation(input[i-1] if i-1 >= 0 else "",input[i+1] if i+1 < len(input) else "")
        return eliminate_needless_parentheses(input)
    except Exception:
        print("lmao rósz")
        sys.exit()
                

if __name__ == "__main__":
    #print(prepare_input(input("> ")))
    #validate_parentheses(input("> "))
    #validate_right_par("A", "¬")
    #validate_left_par("",")")ű
    print(validate_input("((@@(((A→B)))@@))"))
