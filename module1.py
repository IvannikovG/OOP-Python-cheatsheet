
# Before python runs a file, it sets some special variables
# __main__ is one of them.
# When python runs a file directly, it sets __name__ equal __main__
# whenever we import a module it sets __name__ to the name of the file

if __name__ == '__main__':
    print("Run directly")
else:
    print("run from import")

# We can use it
# If it is not an imported file - do smth
