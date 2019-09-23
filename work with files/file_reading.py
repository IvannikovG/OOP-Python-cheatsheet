# Working with files
# File Objects

# f = open('test.txt', 'r')
# # pass a path into the open command.
# # Not recommended
# # defaults to reading, we pass a second arg to say what to do with the file
# # 'w', 'r', 'a' - append, 'r+a'

# print(f.mode)
# # file.mode - mode, file.name - name
# # we always close the file explicitly
# f.close()
# Not a recommended method

# Contex manager -> recommended, automatically closes the file
with open('test.txt', 'r') as f:
    # to work with file -> do it inside here
    # f_contents = f.read()
    # f.readline -> next line
    # f.readlines -> returns a list of the lines
    # we can simply iterate through lines to read a big file
    for line in f:
        print(line, end="")  # without newline for line
    # or
    # for x in f.readlines():
    #     print(x, end="")

with open('test.txt', 'r') as f1:
    # it is possible to read a part of a file
    size_to_read = 10

    f1_contents = f1.readlines()
    f2_contents = f1.read(size_to_read)

    for i in range(len(f1_contents)):
        print(f1_contents[i], end="")

    print(f1.tell())  # says current position in the file

    f1.seek(0)  # starts from the position provided
    f2_contents = f1.read(size_to_read)
    f1.tell()
    print(f1.tell())
