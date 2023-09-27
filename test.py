import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

regex = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\|]'
space = " "
alnum_string = []
alnum_strict_string = []
alnum_string_remove_space = []
special_string = []
expected_string = []

# program to replace the special symbols and spaces between two alphanumeric characters with a single space


for i in range(m):
    for j in range(n):
        if matrix[j][i].isalnum() or re.match(regex, matrix[j][i]):
            alnum_string.append(matrix[j][i])
        elif matrix[j][i] == space:
            alnum_string.append(space)

i = len(alnum_string) - 1
if alnum_string[-1].isalnum():
    j = len(alnum_string) - 1
else:
    while i >= 0:
        if alnum_string[i].isalnum():
            j = i
            break
        i = i - 1

for i in range(j+1):
    if alnum_string[i].isalnum():
        alnum_strict_string.append(alnum_string[i])
    elif alnum_string[i] == space:
        alnum_strict_string.append(" ")
    elif re.match(regex, alnum_string[i]):
        alnum_strict_string.append(" ")

cons_space = False
for char in alnum_strict_string:
    if char == ' ':
        if not consecutive_space:
            alnum_string_remove_space.append(char)
            consecutive_space = True
    else:
        alnum_string_remove_space.append(char)
        consecutive_space = False

i = j + 1
while i < len(alnum_string):
    special_string.append(alnum_string[i])
    i = i + 1

expected_string = alnum_string_remove_space + special_string
final_string = ''.join(expected_string)
print(final_string)