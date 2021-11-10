import itertools

size_of_set_A = int(input('Enter the size of the set A: '))
size_of_set_B = int(input('Enter the size of the set B: '))

run = True
counter = 0
raw_list_setA = []
while run:
    data_entry = input(f'Enter SET A item {counter + 1}: ')
    raw_list_setA.append(data_entry)
    counter += 1
    if size_of_set_A == counter:
        run = False
list_set_A = set(raw_list_setA)


run = True
counter = 0
raw_list_setB = []
while run:
    data_entry = input(f'\nEnter SET B item {counter + 1}: ')
    raw_list_setB.append(data_entry)
    counter += 1
    if size_of_set_B == counter:
        run = False
list_set_B = set(raw_list_setB)

#Part A is intersection of A and B
Truth_value = list_set_B.issubset(list_set_A)
print(Truth_value)

#Part B is set difference
list_set_A_question_b = set(list_set_A)
list_set_B_question_b = set(list_set_B)

print(f'(b) The difference of SET A and B is {list_set_A_question_b - list_set_B_question_b}', end="\n\n")

#Part C is the set

list_set_A_question_c = set(list_set_A)
list_set_B_question_c = set(list_set_B)
print(f'(c) The cross product of SET A and B is {print(list(itertools.product(list_set_A_question_c, list_set_B_question_c)))}', end="\n\n")
