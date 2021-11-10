#The size of the list
size_of_list = int(input('Enter the size of the list: '))


run = True
counter = 0
raw_list = []

while run:
    data_entry = input(f'Enter item {counter + 1}: ')

    raw_list.append(data_entry)
    counter += 1
    if size_of_list == counter:
        run = False
list_set = set(raw_list)
if len(list_set) != len(raw_list):
    print(f'False the set should be {list_set}')
else:
    print(f'True, the set is valid: {list_set}')
