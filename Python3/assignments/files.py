with open('demo.txt', mode='r') as f:
#f.write('Hello from Python!\n')
#file_content = f.readlines()
#f.close()
#print(file_content)
# 
    line = f.readline()

    while line:
        print(line)
        line = f.readline()
print('Done!')

#for line in file_content:
    #print(line[:-1])
running = True
while running:
    print('Please choose')
    print('1. Add Input')
    print('2. Output data')
    print('q: Quit')
    user_input = input('Your Choice: ')
    if user_input == '1':
        data_to_store = input('Your text: ')
        with open('assignment.txt', mode='w') as f:
            f.write(data_to_store)
            f.write('\n')
    elif user_input == '2':
        with open('assignment.txt', mode='r') as wsa:
            pop_it = wsa.readlines()
            for line in pop_it:
                print(line)
    elif user_input == 'q':
        running = False


