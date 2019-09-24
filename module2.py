
import module1
# imported, it runs the code
# the name is now module1. Reason -> not being ran directly
# but imported as module
# we have added main method into the module1, now it is not executed here.

print("Second module`s name is {}".format(__name__))
