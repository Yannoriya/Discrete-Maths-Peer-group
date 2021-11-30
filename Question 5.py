size_of_set = int(input('Enter the size of the set X and Y: '))


run = True
counter = 0
raw_list_setx = []
while run:
    data_entry = input(f'Enter SET X item {counter + 1}: ')
    raw_list_setx.append(data_entry)
    counter += 1
    if size_of_set == counter:
        run = False
list_set_x = list(set(raw_list_setx))

print('\n')
run = True
counter = 0
raw_list_sety = []
while run:
    data_entry = input(f'Enter SET Y item {counter + 1}: ')
    raw_list_sety.append(data_entry)
    counter += 1
    if size_of_set == counter:
        run = False
list_set_y = list(set(raw_list_sety))

def truth_table_func(list_set_1, list_set_2):
    truth_table = []
    for i in range(len(list_set_2)):
        for x in range(len(list_set_2)):
            if int(list_set_2[int(i)]) % int(list_set_1[int(x)]) == 0:
                truth_table.append(True)
            else:
                truth_table.append(False)

    #If there was a False, the length of the function would be 2 since the list will have a False and True. Otherwise it will be one because the true's will be removed by set function
    if len(set(truth_table)) == 1:
        print("True, for all values of Y, there are divisible by X")

    else:
        print("False, for all values of Y, there are not divisible by X")

truth_table_func(list_set_x, list_set_y)
print("\n\n\n")


print('\nReturns True when X = [1, 2, 3], Y =[2, 6, 12]')
truth_table_func([1, 2, 3], [24,6,12])

print('\nReturns False when X = [1, 2, 3], Y =[2, 6, 10]')
truth_table_func([1, 2, 3], [2,6,10])

