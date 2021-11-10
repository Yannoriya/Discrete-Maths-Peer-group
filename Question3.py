import itertools

size_of_set_A = int(input('Enter the size of the list A: '))
size_of_set_B = int(input('Enter the size of the list B: '))

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
    print('\n')
    data_entry = input(f'Enter SET B item {counter + 1}: ')
    raw_list_setB.append(data_entry)
    counter += 1
    if size_of_set_B == counter:
        run = False
list_set_B = set(raw_list_setB)

#Part A is intersection of A and B
list_set_A_question_a = set(list_set_A)
list_set_B_question_a = set(list_set_B)

if list_set_B_question_a.issubset(list_set_A_question_a) == True:
    print('\n(a) B is a subset of A')
else:
    print('\n(a) B is not a subset of A')

#Part B is set difference
list_set_A_question_b = set(list_set_A)
list_set_B_question_b = set(list_set_B)

print(f'(b) A-B = {list_set_A_question_b - list_set_B_question_b}')

#Part C is the set

list_set_A_question_c = set(list_set_A)
list_set_B_question_c = set(list_set_B)
print(f'(c) A X B = {list(itertools.product(list_set_A_question_c, list_set_B_question_c))}', end="\n\n")
