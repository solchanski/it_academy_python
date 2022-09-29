s = input("Введите предложение:")

unique = ""

new_s = s.replace(" ", "")

for symbol in new_s:
    if symbol in unique:
        continue
    unique = unique + symbol

print(unique)