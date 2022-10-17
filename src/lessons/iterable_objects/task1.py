s_input = input("Enter a sentence:")

s = list(s_input)
cl_brackets = [']', '}', ')']
op_brackets = ['[', '{', '(']
s_brackets = []
inside_brackets = []

for i in s:
    if i == '{' or i == '}' or i == '[' or i == ']' or i == '(' or i == ')':
        s_brackets.append(i)
print(s_brackets)

for i in s_brackets:
    if i in op_brackets:
        inside_brackets.append(i)
        if len(inside_brackets) == 0:
            print("Wrong")
    if i in cl_brackets:
        index = cl_brackets.index(i)
        op_bracket = op_brackets[index]
        if inside_brackets[-1] == op_bracket:
            inside_brackets = inside_brackets[:-1]
        else:
            print("Wrong")
if len(inside_brackets) == 0:
    print("Correct")
