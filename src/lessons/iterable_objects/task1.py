s_input = input("Enter a sentence:")

s = list(s_input)
s_brackets = []

for i in s:
    if i == '{' or i == '}' or i == '[' or i == ']' or i == '(' or i == ')':
        s_brackets.append(i)
print(s_brackets)

while len(s_brackets) > 0:
    if ']' in s_brackets:
        num1 = s_brackets.index(']')
        s1 = s_brackets[:num1]
        s1.reverse()
        if '[' in s1:
            num2 = s1.index('[')
            if num2 == 0:
                s_brackets.pop(num1)
                s_brackets.pop(num1-1)
            # print(s_brackets)
    elif '}' in s_brackets:
        num3 = s_brackets.index('}')
        s2 = s_brackets[:num3]
        s2.reverse()
        if '{' in s2:
            num4 = s2.index('{')
            if num4 == 0:
                s_brackets.pop(num3)
                s_brackets.pop(num3-1)
            # print(s_brackets)
    elif ')' in s_brackets:
        num5 = s_brackets.index(')')
        s3 = s_brackets[:num5]
        s3.reverse()
        if '(' in s3:
            num6 = s3.index('(')
            if num6 == 0:
                s_brackets.pop(num5)
                s_brackets.pop(num5-1)
            # print(s_brackets)
    else:
        break

if s_brackets == []:
    print("Correct")
else:
    print("Wrong")