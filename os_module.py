
import os
from datetime import datetime
# allows to interact with the operating system

print(os.getcwd())
# current directory

# os.chdir()
# change current directory

# print(os.listdir())
# -> ls

# os.mkdir('testdir')
# creates a directory

os.makedirs('testdir/testing')
os.removedirs('testdir/testing')
#os.rename('test.txt', 'demo.txt')
# can rename files/dirs

print(os.stat('face1.png'))
mod_time = (os.stat('face1.png').st_mtime)
# give me the last modification time
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk('/Users/georgiiivannikov/Desktop/pyth'):
    # generator, returns ->
    # tuple(path, directories within, files within)
    # for the directory
    print('directories: ', dirpath)
    print('dir.names: ', dirnames)
    print('files: ', filenames)


print(os.environ.get('HOME'))
# all environment variables
