with open('referat.txt', 'r', encoding = 'utf -8') as test_file:
    read_var = test_file.read()
    print(len(read_var))
    read_var = read_var.replace('.','!')
    print(read_var)
with open('referat2.txt','w', encoding = 'utf -8') as test_file2:
    test_file2.write(read_var)
    