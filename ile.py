with open('my_file.txt', 'x') as f:
    contents = f.read()
    print(contents)

with open('my_file.txt', 'w') as f:
    f.write('Hello, world!\n')

with open('my_file.txt', 'a') as f:
    f.write('This is some additional data.\n')